import json, sys

routes_file, output_file = sys.argv[1], sys.argv[2]

with open(routes_file, encoding="utf-8") as f:
    content = f.read()

try:
    routes = json.loads(content)
    with open(output_file, "w", encoding="utf-8") as fw:
        fw.write("# Rails Routes Spec (JSON)\n\n")
        for r in routes:
            fw.write(f"- {r.get('verb')} `{r.get('path')}` → {r.get('controller')}#{r.get('action')}\n")
except json.JSONDecodeError:
    # JSONじゃなかった場合、テキストそのまま吐き出す
    with open(output_file, "w", encoding="utf-8") as fw:
        fw.write("# Rails Routes Spec (raw output)\n\n")
        fw.write("```\n")
        fw.write(content)
        fw.write("\n```")
