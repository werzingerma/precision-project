
#!/usr/bin/env python3
import os, shutil, datetime, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--src", default="notebooks/test_analysis.ipynb")
parser.add_argument("--outdir", default="notebooks/versions")
parser.add_argument("--message", default="CLI Snapshot")
args = parser.parse_args()

os.makedirs(args.outdir, exist_ok=True)
ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
base = os.path.splitext(os.path.basename(args.src))[0]
dst = os.path.join(args.outdir, f"{base}_{ts}.ipynb")

if not os.path.exists(args.src):
    raise SystemExit(f"Quelle nicht gefunden: {args.src}")

shutil.copyfile(args.src, dst)

meta = {"timestamp": ts, "message": args.message}
with open(dst + ".meta.json", "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

print("Snapshot gespeichert:", dst)
