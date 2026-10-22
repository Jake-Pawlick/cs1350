import json
import pickle
import os
import shutil


# Problem 1

'''
def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.

    Args:
        machines: dict mapping machine name -> log file name

    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {}

    with open("info.log", "w") as info_f, \
         open("warning.log", "w") as warn_f, \
         open("error.log", "w") as err_f:
        outputs = {"INFO": info_f, "WARNING": warn_f, "ERROR": err_f}

        for machine, log_name in machines.items():
            counts[machine] = {"INFO": 0, "WARNING": 0, "ERROR": 0}
            with open(log_name, "r") as log:
                for line in log:
                    line = line.rstrip("\n")
                    if line.strip() == "":          
                        continue
                    for level, out_file in outputs.items():
                        if "[" + level + "]" in line:
                            out_file.write(machine + " | " + line + "\n")
                            counts[machine][level] += 1
                            break
    return counts


def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("SECURITY LOG REPORT")
    print("=" * 40)

    total = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for machine, c in counts.items():
        entries = c["INFO"] + c["WARNING"] + c["ERROR"]
        if c["ERROR"] >= 2:
            status = "CRITICAL"
        elif c["ERROR"] >= 1 or c["WARNING"] >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"
        print(f"{machine}: {entries} entries | INFO {c['INFO']} | "
              f"WARNING {c['WARNING']} | ERROR {c['ERROR']} | Status: {status}")
        for level in total:
            total[level] += c[level]

    print("-" * 40)
    all_entries = sum(total.values())
    print(f"Total: {all_entries} entries | INFO {total['INFO']} | "
          f"WARNING {total['WARNING']} | ERROR {total['ERROR']}")

    print("Errors (see error.log):")
    with open(error_file, "r") as f:
        for line in f:
            print("  " + line.rstrip("\n"))
'''

# Problem 2

'''
def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""
    incidents = []
    with open(csv_file, "r") as f:
        next(f)                                    
        for line in f:
            line = line.strip()
            if line == "":
                continue
            id_, machine, severity, description = line.split(",")
            incidents.append({
                "id": int(id_),
                "machine": machine,
                "severity": severity,
                "description": description,
            })
    return incidents


def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""
    summary = {
        "total": len(incidents),
        "by_machine": {},
        "by_severity": {},
        "high_ids": [],
    }
    for inc in incidents:
        m, s = inc["machine"], inc["severity"]
        summary["by_machine"][m] = summary["by_machine"].get(m, 0) + 1
        summary["by_severity"][s] = summary["by_severity"].get(s, 0) + 1
        if s == "high":
            summary["high_ids"].append(inc["id"])

    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)
    return summary


def archive(incidents, folder):
    """Pickle all incidents and write one JSON file per machine into folder."""
    os.makedirs(folder, exist_ok=True)             

    with open(os.path.join(folder, "incidents.pkl"), "wb") as f:
        pickle.dump(incidents, f)

    by_machine = {}
    for inc in incidents:
        by_machine.setdefault(inc["machine"], []).append(inc)

    for machine, items in by_machine.items():
        with open(os.path.join(folder, machine + ".json"), "w") as f:
            json.dump(items, f)

    return sorted(os.listdir(folder))


def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    with open(os.path.join(folder, "incidents.pkl"), "rb") as f:
        return pickle.load(f)
'''

# Problem 3 (Bonus)

'''
def organize(folder):
    """Move files into logs/, data/, pickles/, other/ by extension."""
    ext_to_sub = {".log": "logs", ".csv": "data", ".json": "data",
                  ".pkl": "pickles"}
    moved = {"logs": [], "data": [], "pickles": [], "other": []}

    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):                
            continue
        ext = os.path.splitext(name)[1]
        sub = ext_to_sub.get(ext, "other")
        dest_dir = os.path.join(folder, sub)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(path, os.path.join(dest_dir, name))
        moved[sub].append(name)

    for sub in moved:
        moved[sub].sort()
    return moved


def create_backup(source_dir, backup_root, label):
    """Copy source_dir to backup_root/backup_<label>; return the new path."""
    os.makedirs(backup_root, exist_ok=True)
    dest = os.path.join(backup_root, "backup_" + label)
    shutil.copytree(source_dir, dest)
    return dest


def verify_backup(source_dir, backup_dir):
    """Return True if every file under source_dir is in backup_dir with the same
    size."""
    for current, _dirs, files in os.walk(source_dir):
        for name in files:
            src_path = os.path.join(current, name)
            rel = os.path.relpath(src_path, source_dir)
            bak_path = os.path.join(backup_dir, rel)
            if not os.path.isfile(bak_path):
                return False
            if os.path.getsize(src_path) != os.path.getsize(bak_path):
                return False
    return True


def cleanup_old_backups(backup_root, keep):
    """Delete all but the newest `keep` backups; return sorted names deleted."""
    names = sorted(n for n in os.listdir(backup_root)
                   if os.path.isdir(os.path.join(backup_root, n)))
    to_delete = names[:max(len(names) - keep, 0)]   
    for name in to_delete:
        path = os.path.join(backup_root, name)
        print("Deleting:", path)                  
        shutil.rmtree(path)
    return sorted(to_delete)

# Test cases

if __name__ == "__main__":
    print("===== Problem 1 =====")
    with open("server_a.log", "w") as f:
        f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
        f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
        f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
        f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
        f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
        f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")
    with open("server_b.log", "w") as f:
        f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
        f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
        f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
        f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
        f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
        f.write("\n")
        f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

    counts = split_logs({"server_a": "server_a.log", "server_b": "server_b.log"})
    print(counts)
    with open("warning.log", "r") as f:
        print(f.read())
    print_report(counts)

    print("\n===== Problem 2 =====")
    with open("incidents.csv", "w") as f:
        f.write("id,machine,severity,description\n")
        f.write("1,server_a,high,Account root locked\n")
        f.write("2,server_b,high,Disk encryption failed\n")
        f.write("3,server_b,low,Unencrypted volume mounted\n")
        f.write("4,server_a,medium,Repeated failed logins\n")
        f.write("5,server_b,high,Unauthorized access on port 22\n")

    incidents = load_incidents("incidents.csv")
    print(len(incidents))
    print(incidents[0])
    summary = save_summary(incidents, "summary.json")
    print(summary)
    with open("summary.json", "r") as f:
        print(json.load(f) == summary)
    print(archive(incidents, "archive"))
    with open(os.path.join("archive", "server_a.json"), "r") as f:
        print([item["id"] for item in json.load(f)])
    restored = load_archive("archive")
    print(restored == incidents)

    print("\n===== Problem 3 (Bonus) =====")
    for old in ["workspace", "backups"]:
        if os.path.exists(old):
            shutil.rmtree(old)
    os.mkdir("workspace")
    for name in ["a.log", "b.log", "incidents.csv", "summary.json",
                 "incidents.pkl", "notes.txt"]:
        with open(os.path.join("workspace", name), "w") as f:
            f.write(f"Test file: {name}\n")

    print(organize("workspace"))
    print(sorted(os.listdir("workspace")))
    for label in ["2026-10-01", "2026-10-02", "2026-10-03"]:
        path = create_backup("workspace", "backups", label)
        print(os.path.basename(path), verify_backup("workspace", path))

    os.remove(os.path.join("backups", "backup_2026-10-03", "logs", "a.log"))
    print(verify_backup("workspace", os.path.join("backups", "backup_2026-10-03")))
    print(cleanup_old_backups("backups", 2))
    print(sorted(os.listdir("backups")))
'''