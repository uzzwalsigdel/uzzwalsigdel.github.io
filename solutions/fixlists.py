import re, pathlib
for p in ["paper1_bnk221.md", "paper2_bnk209.md", "paper3_bnk202.md"]:
    lines = pathlib.Path(p).read_text(encoding="utf-8").split("\n")
    out = []; n = 0; in_code = False
    for l in lines:
        if l.startswith("```"):
            in_code = not in_code
        is_item = re.match(r"^\s*([-*+]|\d+\.)\s+", l)
        if is_item and out and not in_code:
            prev = out[-1]
            prev_ok = (re.match(r"^\s*([-*+]|\d+\.)\s+", prev) or prev.strip() == ""
                       or prev.startswith("|") or prev.lstrip().startswith(">") or prev.lstrip().startswith("<"))
            if not prev_ok:
                out.append(""); n += 1
        out.append(l)
    pathlib.Path(p).write_text("\n".join(out), encoding="utf-8")
    print(p, "inserted blank lines:", n)
