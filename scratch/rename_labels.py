import os

# Delete labels.csv in root if exists
if os.path.exists("labels.csv"):
    os.remove("labels.csv")
    print("Deleted root labels.csv")

# Delete deliverables/evidence/labels.csv if exists
ev_labels = os.path.join("deliverables", "evidence", "labels.csv")
if os.path.exists(ev_labels):
    os.remove(ev_labels)
    print("Deleted deliverables/evidence/labels.csv")
