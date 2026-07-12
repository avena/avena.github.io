#!/usr/bin/env python3
import os, re, urllib.parse
from html import escape

WIKI_DIR = "ltsp/tar.gz.files/wiki.d"
OUT_DIR = "ltsp"

TEMPLATE = """<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — LTSP</title>
<link rel="stylesheet" href="/css/bootstrap.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>
body{{background:#f5f5f5;font-family:'Poppins',sans-serif;}}
.ltsp-header{{background:#1a237e;color:#fff;padding:20px 0;}}
.ltsp-header h1{{margin:0;font-size:1.5rem;}}
.ltsp-sidebar{{background:#fff;border-right:1px solid #e0e0e0;padding:20px;min-height:calc(100vh - 120px);font-size:0.9rem;}}
.ltsp-sidebar ul{{list-style:none;padding:0;margin:0;}}
.ltsp-sidebar li{{margin-bottom:6px;}}
.ltsp-sidebar a{{color:#333;text-decoration:none;}}
.ltsp-sidebar a:hover{{color:#1a237e;text-decoration:underline;}}
.ltsp-sidebar .sidehead{{font-weight:700;margin-top:16px;margin-bottom:8px;font-size:0.85rem;text-transform:uppercase;color:#1a237e;}}
.ltsp-content{{background:#fff;padding:30px;min-height:calc(100vh - 120px);}}
.ltsp-content h2{{color:#1a237e;margin-top:24px;margin-bottom:12px;font-size:1.4rem;}}
.ltsp-content h3{{color:#333;margin-top:20px;margin-bottom:10px;font-size:1.2rem;}}
.ltsp-content p{{margin-bottom:12px;line-height:1.6;}}
.ltsp-content pre{{background:#f5f5f5;border:1px solid #e0e0e0;padding:12px;overflow-x:auto;font-size:0.85rem;border-radius:4px;}}
.ltsp-content code{{background:#f5f5f5;padding:2px 6px;font-size:0.85rem;border-radius:3px;}}
.ltsp-content ul{{margin-bottom:12px;padding-left:20px;}}
.ltsp-content li{{margin-bottom:4px;}}
.ltsp-breadcrumb{{font-size:0.85rem;color:#666;margin-bottom:16px;}}
.ltsp-breadcrumb a{{color:#1a237e;}}
.ltsp-content hr{{margin:24px 0;border:0;border-top:1px solid #e0e0e0;}}
</style>
</head>
<body>
<div class="ltsp-header">
<div class="container">
<div class="row align-items-center">
<div class="col"><a href="/ltsp/" style="color:#fff;text-decoration:none"><h1>LTSP · Documentação em português</h1></a></div>
<div class="col-auto"><a href="/" class="text-white-50">← Voltar</a></div>
</div></div></div>
<div class="container"><div class="row">
<div class="col-md-3"><div class="ltsp-sidebar">{sidebar}</div></div>
<div class="col-md-9"><div class="ltsp-content">
<div class="ltsp-breadcrumb"><a href="/ltsp/">LTSP</a> &raquo; {group}</div>
{content}
</div></div></div></div>
<script src="/js/bootstrap.bundle.min.js"></script>
</body></html>"""

SIDEBAR = None


def get_sidebar():
    global SIDEBAR
    if SIDEBAR:
        return SIDEBAR
    p = os.path.join(WIKI_DIR, "Site.SideBar")
    if not os.path.exists(p):
        SIDEBAR = ""
        return SIDEBAR
    text = extract(p)
    if not text:
        SIDEBAR = ""
        return SIDEBAR
    SIDEBAR = conv(text, True)
    return SIDEBAR


def extract(path):
    try:
        with open(path, "r", encoding="iso-8859-1", errors="replace") as f:
            c = f.read()
    except:
        return None
    m = re.search(r'^text=(.*?)(?:\ntime=|\nctime=|\nhost=|\Z)', c, re.DOTALL | re.MULTILINE)
    if m:
        try:
            return urllib.parse.unquote(m.group(1).strip(), encoding="iso-8859-1")
        except:
            return m.group(1).strip()
    return None


def inline(t):
    t = re.sub(r"'''(.*?)'''", r'<strong>\1</strong>', t)
    t = re.sub(r"''(.*?)''", r'<em>\1</em>', t)
    t = re.sub(r'\[\[(https?://[^\s|\[\]]+)\|([^\[\]]+?)\]\]', r'<a href="\1" target="_blank" rel="noopener">\2</a>', t)
    t = re.sub(r'\[\[(https?://[^\s|\[\]]+?)\]\]', lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener">{m.group(1)}</a>', t)
    t = re.sub(r'\[\[([^|\[\]]+)\|([^\[\]]+?)\]\]', lambda m: f'<a href="/ltsp/{m.group(1)}.html">{m.group(2)}</a>', t)
    t = re.sub(r'\[\[([^|\[\]]+?)\]\]', lambda m: f'<a href="/ltsp/{m.group(1)}.html">{m.group(1).split("/")[-1]}</a>', t)
    t = re.sub(r'@@(.*?)@@', r'<code>\1</code>', t)
    t = re.sub(r"'''(.*?)'''", r'<strong>\1</strong>', t)
    return t


def conv(text, sb=False):
    if not text:
        return ""
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s == "@@" or s == "[@":
            buf = []
            i += 1
            while i < len(lines) and lines[i].strip() not in ("@@", "@]"):
                buf.append(lines[i])
                i += 1
            out.append(f"<pre>{escape(chr(10).join(buf))}</pre>")
            i += 1
            continue
        if s.startswith("(:") and s.endswith(":)"):
            i += 1
            continue
        if not s:
            i += 1
            continue
        if sb:
            if s.startswith("%") and ("sidehead" in s or "right" in s):
                if "sidehead" in s:
                    t = re.sub(r'%\w+%', '', s).strip()
                    out.append(f'<div class="sidehead">{inline(t)}</div>')
                elif "right" in s:
                    t = re.sub(r'%\w+%', '', s).strip()
                    t = re.sub(r'\[-(.*?)-\]', r'\1', t)
                    out.append(f'<div style="text-align:right;font-size:0.8rem;">{inline(t)}</div>')
            elif s.startswith("*"):
                out.append(f"<li>{inline(s.lstrip('*').strip())}</li>")
            else:
                out.append(inline(s))
        else:
            if s.startswith("!!!!!"):
                out.append(f"<h5>{inline(s[5:].strip())}</h5>")
            elif s.startswith("!!!!"):
                out.append(f"<h4>{inline(s[4:].strip())}</h4>")
            elif s.startswith("!!!"):
                out.append(f"<h3>{inline(s[3:].strip())}</h3>")
            elif s.startswith("!!"):
                out.append(f"<h2>{inline(s[2:].strip())}</h2>")
            elif s.startswith("!"):
                out.append(f"<h4>{inline(s[1:].strip())}</h4>")
            elif re.match(r'^-{4,}$', s):
                out.append("<hr>")
            elif s.startswith("*"):
                items = []
                while i < len(lines) and lines[i].strip().startswith("*"):
                    items.append(f"<li>{inline(lines[i].strip().lstrip('*').strip())}</li>")
                    i += 1
                out.append("<ul>\n" + "\n".join(items) + "\n</ul>")
                continue
            else:
                out.append(f"<p>{inline(s)}</p>")
        i += 1
    r = "\n".join(out)
    if sb:
        r = r.replace('\n', '')
        r = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', r)
    return r


def main():
    os.makedirs(os.path.join(OUT_DIR, "Main"), exist_ok=True)
    if not os.path.isdir(WIKI_DIR):
        print(f"Erro: {WIKI_DIR} não encontrado"); return
    skip = ["RecentChanges", ".pageindex", ".flock", ".htaccess", "SiteAdmin", "Site.Analyze"]
    files = sorted([f for f in os.listdir(WIKI_DIR) if not any(x in f for x in skip) and not f.startswith(".")])
    for fname in files:
        fp = os.path.join(WIKI_DIR, fname)
        if not os.path.isfile(fp):
            continue
        name = os.path.basename(fp)
        text = extract(fp)
        if not text:
            print(f"  [ERR] {name}"); continue
        html = conv(text)
        sb = get_sidebar()
        group = name.rsplit(".", 1)[0] if "." in name else "Main"
        tl = re.search(r'<h2>(.*?)</h2>', html)
        t = re.sub(r'<[^>]+>', '', tl.group(1)) if tl else name.split(".")[-1]
        page = TEMPLATE.format(title=t, group=group, content=html, sidebar=sb)
        if name.endswith("HomePage"):
            op = os.path.join(OUT_DIR, "index.html")
        elif name.endswith("SideBar"):
            op = os.path.join(OUT_DIR, "_sidebar.html")
        else:
            gn, pg = name.rsplit(".", 1) if "." in name else ("Main", name)
            op = os.path.join(OUT_DIR, gn, f"{pg}.html")
        os.makedirs(os.path.dirname(op), exist_ok=True)
        with open(op, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  [OK] {name}")
    print("Concluído!")


if __name__ == "__main__":
    main()
