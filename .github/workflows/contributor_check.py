import json, sys
def get_structure(obj):
  if isinstance(obj, dict):
    return {k: get_structure(v) for k, v in obj.items()}
  elif isinstance(obj, list):
    return [get_structure(obj[0])] if obj else []
  else:
    return type(obj).__name__
with open("src/Contributors.json") as f1, open("base_Contributors.json") as f2:
  pr_data = json.load(f1)
  base_data = json.load(f2)
  pr_count = len(pr_data.get("contributors", []))
  base_count = len(base_data.get("contributors", []))
  if pr_count < base_count:
    print(f"Contributors were removed! PR: {pr_count}, Base: {base_count}")
    sys.exit(1)
  else:
    print(f"Contributors in PR: {pr_count}, Base: {base_count}")
  s1 = get_structure(pr_data)
  s2 = get_structure(base_data)
  if s1 != s2:
    print("Json structure does not match origin")
    sys.exit(1)