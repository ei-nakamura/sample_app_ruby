import json, sys

with open(sys.argv[1], encoding="utf-8") as f:
    routes = json.load(f)

with open(sys.argv[2], "w", encoding="utf-8") as fw:
    fw.write("# Rails Routes Spec\n\n")
    for r in routes:
        verb = r.get("verb")
        path = r.get("path")
        ctrl = r.get("controller")
        action = r.get("action")
        fw.write(f"- {verb} `{path}` → {ctrl}#{action}\n")
