import markdown, pathlib, subprocess, datetime

root = pathlib.Path(__file__).parent
papers = ["paper1_bnk221.md", "paper2_bnk209.md", "paper3_bnk202.md"]
md_ext = ["tables", "fenced_code", "sane_lists", "attr_list"]

css = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.6pt; line-height: 1.42; color: #111; }
h1 { font-size: 19pt; color: #0b3d6b; border-bottom: 3px solid #0b3d6b; padding-bottom: 4px; margin: 0 0 4px 0; page-break-before: always; }
h1.first { page-break-before: auto; }
.subtitle { color: #444; font-style: italic; margin-bottom: 14px; font-size: 9.8pt; }
h2 { font-size: 14pt; color: #fff; background: #0b3d6b; padding: 5px 9px; margin: 20px 0 10px 0; border-radius: 3px; page-break-after: avoid; }
h3 { font-size: 11.3pt; background: #eef3f9; border-left: 5px solid #0b3d6b; padding: 6px 8px; margin: 16px 0 6px 0; page-break-after: avoid; page-break-inside: avoid; }
h4 { font-size: 10.8pt; color: #0b3d6b; margin: 10px 0 4px 0; page-break-after: avoid; }
p { margin: 4px 0 6px 0; text-align: justify; }
ul, ol { margin: 3px 0 6px 0; padding-left: 22px; }
li { margin-bottom: 2px; }
table { border-collapse: collapse; margin: 6px 0 10px 0; font-size: 9.6pt; page-break-inside: auto; }
th, td { border: 1px solid #999; padding: 3px 6px; vertical-align: top; }
th { background: #dde7f3; }
tr { page-break-inside: avoid; }
blockquote { background: #fff8e1; border: 1px solid #f0c36d; border-left: 6px solid #e6a100; padding: 6px 10px; margin: 8px 0 12px 0; page-break-inside: avoid; }
blockquote p { margin: 2px 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 9.3pt; background: #f3f3f3; padding: 0 2px; }
pre { background: #f6f6f6; border: 1px solid #ccc; padding: 6px; font-size: 8.8pt; line-height: 1.25; page-break-inside: avoid; overflow: hidden; }
pre code { background: none; padding: 0; }
hr { border: 0; border-top: 1px solid #bbb; margin: 10px 0; }
.cover { text-align: center; padding-top: 120px; }
.cover h1 { border: 0; font-size: 26pt; page-break-before: auto; }
.cover .big { font-size: 15pt; margin: 20px 0; }
.cover table { margin: 30px auto; font-size: 11pt; }
.cover p { text-align: center; }
.toc { margin-top: 30px; }
.toc li { margin-bottom: 4px; }
"""

cover = f"""
<div class="cover">
<h1>Model Question Papers 2026 — Complete Solutions</h1>
<p class="big">Tribhuvan University · Faculty of Management · BBA Eighth Semester</p>
<table>
<tr><th>Paper</th><th>Course</th><th>Full Marks</th></tr>
<tr><td>1</td><td>BNK 221: Corporate Financing Decision</td><td>100</td></tr>
<tr><td>2</td><td>BNK 209: Insurance and Risk Management</td><td>100</td></tr>
<tr><td>3</td><td>BNK 202: Financial Derivatives</td><td>100</td></tr>
</table>
<p>Every question (Group A to Group D, including all optional questions) is reproduced with its question text followed by a full solution. Numerical questions show step-by-step working and end with an <b>Exam Hint</b> box listing the formula to remember and the common trap.</p>
<p style="margin-top:40px;color:#666">Prepared {datetime.date.today():%d %B %Y}</p>
</div>
<div class="toc">
<h2>Contents</h2>
<ol>
<li>Paper 1 — BNK 221: Corporate Financing Decision (Q1–Q22)</li>
<li>Paper 2 — BNK 209: Insurance and Risk Management (Q1–Q22)</li>
<li>Paper 3 — BNK 202: Financial Derivatives (Q1–Q22)</li>
</ol>
</div>
"""

parts = []
for p in papers:
    text = (root / p).read_text(encoding="utf-8")
    lines = text.split("\n")
    # second non-empty line is the subtitle
    html = markdown.markdown(text, extensions=md_ext)
    # style the subtitle line following h1
    html = html.replace("</h1>\n<p>", "</h1>\n<p class=\"subtitle\">", 1)
    parts.append(html)

doc = f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>BBA 8th Sem Model Question Solutions</title><style>{css}</style></head><body>{cover}{''.join(parts)}</body></html>"
out_html = root / "combined_solutions.html"
out_html.write_text(doc, encoding="utf-8")
out_pdf = root / "BBA_8th_Sem_Model_Question_Solutions_2026.pdf"
cmd = ["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
       f"--print-to-pdf={out_pdf}", f"file://{out_html}"]
subprocess.run(cmd, check=True, capture_output=True)
print("wrote", out_pdf, out_pdf.stat().st_size, "bytes")
