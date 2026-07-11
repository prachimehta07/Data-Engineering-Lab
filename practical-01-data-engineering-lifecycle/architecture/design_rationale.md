# Design Rationale — What the Diagram Doesn't Show

The architecture diagram shows *what* was built. This document is about *why* — the trade-offs, failure modes, and decisions a box-and-arrow picture can't communicate. Read this after you understand the diagram, not instead of it.

## 1. Why Kafka instead of just reading the database directly?

The naive design is: downstream services just query `OLTP PostgreSQL` whenever they need fresh data. This fails at enterprise scale for two concrete reasons:

- **Load coupling** — every downstream consumer hitting the production database directly means analytics traffic can slow down or crash the system customers are actively buying from.
- **No replay** — if a downstream service is down for an hour, direct-query designs have no way to "catch up" on what it missed.

Kafka decouples this: producers write once, any number of consumers read independently, and a consumer that was offline can replay from where it left off (within Kafka's retention window). The cost is added complexity — you now have eventual consistency, not immediate consistency, between the source database and everything downstream.

## 2. Why Bronze / Silver / Gold instead of one clean table?

The instinct is "just clean the data once and store the result." This breaks down for one repeated real-world reason: **cleaning logic itself has bugs and changes over time.** If you only keep the cleaned output and discard the raw input, a bug discovered six months later means the original data is gone — there's nothing to reprocess.

The medallion layers exist to separate two different guarantees:
- **Bronze** — a permanent, replayable record of exactly what arrived, unmodified
- **Silver/Gold** — derived, and therefore *disposable and regenerable* if transformation logic changes

This is the same reasoning behind "immutable infrastructure" — never mutate the source of truth, always regenerate derived state.

## 3. Why both Flink and Spark, not just one?

They solve different points on the latency/cost curve:
- **Flink** keeps state in memory and processes events as they arrive — necessary when the answer needs to be seconds old (fraud detection, live inventory counts).
- **Spark** processes large batches efficiently but with higher latency — cheaper per byte processed, appropriate for nightly aggregation, historical backfills, and ML feature generation over months of data.

Using Flink for everything wastes money on always-on compute for workloads that don't need sub-second freshness. Using Spark for everything means your "real-time" dashboard is actually hours stale. Real systems mix both deliberately, matched to each use case's actual latency requirement — not out of tool fashion.

## 4. The tension nobody puts in the diagram: immutability vs. "right to be forgotten"

Bronze is append-only and immutable — that's the whole point of it. But GDPR gives customers the right to have their personal data deleted. These two requirements directly conflict.

In practice this is solved by **not storing raw PII in Bronze at all**, or by **crypto-shredding**: encrypting each customer's data with a per-customer key, and "deleting" the data by discarding the key rather than rewriting immutable files. This is a genuinely hard problem in real systems — worth naming explicitly rather than pretending immutability and deletability coexist for free.

## 5. Schema evolution is the silent killer of pipelines

Producers (the app team shipping the mobile app) will add, rename, or change the type of a field without warning a data engineering team. If Silver blindly trusts Bronze's shape, one upstream deploy breaks every downstream job simultaneously.

The real mitigation: a **schema registry** sitting between Ingestion and Storage that enforces backward/forward compatibility rules before a message is accepted — not a "we'll catch it in code review" hope.

## 6. What this diagram intentionally does NOT show

A logical architecture diagram like this one deliberately leaves out:
- **Physical/network topology** — which services sit in which VPC, what's public vs. private
- **Orchestration** — what schedules/triggers each job (Airflow, cron, event-driven)
- **CI/CD** — how code changes to any of these services get tested and deployed
- **Alerting thresholds** — Observability is shown as a category, not "alert if consumer lag > 60s"

None of these are missing by accident — a diagram trying to show all of them stops being readable. They belong in separate, focused documents once this practical's scope expands.

---

*This document exists because the diagram alone invites a shallow reading ("Kafka goes here, Spark goes there"). The trade-offs above are what actually separate a diagram from an architecture.*
