import csv, os
from datetime import datetime

def log_journal(entry, file="journal.csv"):
    entry["timestamp"] = datetime.utcnow().isoformat()
    exists = os.path.isfile(file)
    with open(file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=entry.keys())
        if not exists:
            writer.writeheader()
        writer.writerow(entry)
