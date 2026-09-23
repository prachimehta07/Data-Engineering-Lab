import csv
import json
import shutil
from pathlib import Path
from datetime import date


BASE_DIR = Path(__file__).resolve().parent.parent

MANIFEST_FILE = BASE_DIR / "data" / "access_manifest.csv"
POLICY_FILE = BASE_DIR / "policies" / "lifecycle.json"
RESULTS_DIR = BASE_DIR / "results"


def load_policy():
    with open(POLICY_FILE, encoding="utf-8") as file:
        return json.load(file)


def find_object(object_name):
    log_file = BASE_DIR / "data" / "logs" / object_name
    audit_file = BASE_DIR / "data" / "audit" / object_name

    if log_file.exists():
        return log_file

    if audit_file.exists():
        return audit_file

    return None


def decide_tier(age_days, access_count, policy):
    hot = policy["tiers"]["HOT"]
    warm = policy["tiers"]["WARM"]

    if age_days <= hot["max_age_days"] and access_count >= hot["min_access_count"]:
        return "HOT"

    if age_days <= warm["max_age_days"]:
        return "WARM"

    return "COLD"


def run_lifecycle():
    policy = load_policy()
    today = date.today()

    results = []

    with open(MANIFEST_FILE, encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            created_date = date.fromisoformat(row["created_date"])
            last_access = date.fromisoformat(row["last_access"])

            age_days = (today - created_date).days
            days_since_access = (today - last_access).days
            access_count = int(row["access_count"])
            size_mb = float(row["size_mb"])

            tier = decide_tier(age_days, access_count, policy)

            source = find_object(row["object_name"])

            if source is not None:
                tier_dir = RESULTS_DIR / "tiers" / tier
                tier_dir.mkdir(parents=True, exist_ok=True)

                shutil.copy2(source, tier_dir / source.name)

            results.append({
                "object_name": row["object_name"],
                "age_days": age_days,
                "days_since_access": days_since_access,
                "access_count": access_count,
                "size_mb": size_mb,
                "assigned_tier": tier
            })

    RESULTS_DIR.mkdir(exist_ok=True)

    result_file = RESULTS_DIR / "lifecycle_results.csv"

    with open(result_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "object_name",
            "age_days",
            "days_since_access",
            "access_count",
            "size_mb",
            "assigned_tier"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("Lifecycle processing completed.")
    print(f"Results saved to: {result_file}")


if __name__ == "__main__":
    run_lifecycle()