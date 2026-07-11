# Data Engineering Laboratory

A working repository of Data Engineering lab practicals. Each practical lives in its own folder, self-contained: open one, understand one, no dependency on the others.

This repo doesn't pre-commit to a fixed number of practicals — folders are added as work is completed, not scaffolded in advance.

---

## Start here

The recurring idea across this lab is a five-step cycle that almost every data platform is built around:

```
Generation → Ingestion → Storage → Transformation → Serving
   (born)      (moves)     (rests)     (reshaped)    (used)
```

Individual practicals zoom into one part of this cycle at a time. Whatever tools appear (Kafka, Spark, dbt, Power BI...) exist to make one of those five steps work at real scale — that's the lens to view every practical through.

---

## Structure

```
Data-Engineering-Lab/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── tools.md          ← tools used so far, explained plainly
│   └── references.md     ← sources/docs referenced while building this repo
└── practical-01-data-engineering-lifecycle/
    ├── README.md
    ├── architecture/
    └── manifesto/
```

Each practical folder documents itself in its own `README.md` — that's the single entry point per practical.

---

## Practicals

| # | Practical | Summary |
|---|-----------|---------|
| 1 | [Enterprise Data Engineering Lifecycle](./practical-01-data-engineering-lifecycle) | End-to-end architecture diagram + design rationale + manifesto for an e-commerce platform |


---

## Objectives

- Understand enterprise data engineering architecture end to end
- Design pipelines that scale from prototype to production
- Practice professional technical documentation
- Apply real version control workflow

---

## Author

**Name: Prachi**

