import os

# 1. Rename deliverables/evidence/labels.csv to deliverables/evidence/labels-phuong.csv
src_ev = os.path.join("deliverables", "evidence", "labels.csv")
dst_ev = os.path.join("deliverables", "evidence", "labels-phuong.csv")

if os.path.exists(src_ev):
    if os.path.exists(dst_ev):
        os.remove(dst_ev)
    os.rename(src_ev, dst_ev)
    print("Renamed deliverables/evidence/labels.csv -> deliverables/evidence/labels-phuong.csv")

# 2. Rename root labels.csv to labels-phuong.csv if exists
if os.path.exists("labels.csv"):
    if os.path.exists("labels-phuong.csv"):
        os.remove("labels-phuong.csv")
    os.rename("labels.csv", "labels-phuong.csv")
    print("Renamed root labels.csv -> labels-phuong.csv")
