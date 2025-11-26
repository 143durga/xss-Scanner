import html

def report_html(results, out_file='report.html'):
    rows = ""
    for r in results:
        rows += "<tr>"
        rows += f"<td>{html.escape(r.get('method',''))}</td>"
        rows += f"<td>{html.escape(r.get('url',''))}</td>"
        rows += f"<td>{html.escape(r.get('param',''))}</td>"
        rows += f"<td>{html.escape(r.get('context',''))}</td>"
        rows += f"<td>{html.escape(r.get('payload',''))}</td>"
        rows += f"<td><pre>{html.escape(r.get('snippet',''))}</pre></td>"
        rows += "</tr>\n"

    html_doc = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>XSS Scan Report</title></head><body>
<h1>XSS Scan Report</h1>
<table border="1" cellspacing="0" cellpadding="6">
<tr><th>Method</th><th>URL</th><th>Param</th><th>Context</th><th>Payload</th><th>Snippet</th></tr>
{rows}
</table>
</body></html>"""
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html_doc)
    print(f"Saved report to {out_file}")
