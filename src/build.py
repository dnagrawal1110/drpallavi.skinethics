#!/usr/bin/env python3
"""Build Dr Pallavi CTA guide pages from src/guides/*.py content.

Usage: python3 src/build.py [slug ...]   (no args = build every guide)
Each guide module defines GUIDE = dict(slug, trigger, title, pill, h1, h1_em,
subline, intro, quote, sections, tagline). Sections are (kind, data) tuples.
"""
import html, importlib.util, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
CSS = (SRC / "guide.css").read_text()
e = html.escape

BYLINE = "Dr. Pallavi Ahire-Shelke · MBBS, MD, DNB, DDV · Gold Medalist Dermatologist · Skin Ethics Clinic, Baner, Pune"


def label(t):
    return f'<div class="section-label">{t}</div>'


def wrap(inner):
    return f'  <section>\n    <div class="wrapper">\n{inner}\n    </div>\n  </section>\n'


def r_card(d):
    h = f"<h2>{d['h']}</h2>" if d.get("h") else ""
    ps = "".join(f"<p>{p}</p>" for p in d["p"])
    cls = "card card-warn" if d.get("warn") else "card card-accent"
    return f'<div class="{cls}">{h}{ps}</div>'


def r_steps(d):
    return '<div class="stat-grid">' + "".join(
        f'<div class="stat-card"><div class="stat-num">{i}</div><h3>{h}</h3><p>{p}</p></div>'
        for i, (h, p) in enumerate(d, 1)) + "</div>"


def r_concerns(d):
    out = ""
    for c in d:
        out += (f'<div class="concern-card"><div class="concern-header"><div class="concern-emoji">{c["emoji"]}</div>'
                f'<div class="concern-title-block"><div class="concern-tag">{c["tag"]}</div><h2>{c["h"]}</h2></div></div>'
                f'<div class="concern-body"><div class="why-block"><div class="why-label">{c.get("l1", "What It Is")}</div><p>{c["p1"]}</p></div>')
        if c.get("p2"):
            out += f'<div class="look-block"><div class="look-label">{c.get("l2", "Good To Know")}</div><p>{c["p2"]}</p></div>'
        out += "</div></div>"
    return out


def r_signs(d, dot="●"):
    return '<div class="signs-list">' + "".join(
        f'<div class="sign-item"><span class="sign-dot">{dot}</span><span>{s}</span></div>' for s in d) + "</div>"


def r_dosdonts(d):
    do_h, do, dont_h, dont = d
    return ('<div class="dos-donts"><div class="do-col">' + f'<div class="col-head">✔ {do_h}</div>' +
            "".join(f'<div class="do-item"><span class="chk">✔</span><span>{x}</span></div>' for x in do) +
            '</div><div class="dont-col">' + f'<div class="col-head">✕ {dont_h}</div>' +
            "".join(f'<div class="dont-item"><span class="x">✕</span><span>{x}</span></div>' for x in dont) + "</div></div>")


def r_table(d):
    return '<div class="ing-table">' + "".join(
        f'<div class="ing-row"><span class="ir-name">{n}</span><span class="ir-desc">{x}</span></div>' for n, x in d) + "</div>"


def r_timeline(d):
    return '<div class="timeline">' + "".join(
        f'<div class="tl-item{(" " + t[3]) if len(t) > 3 else ""}"><div class="tl-when">{t[0]}</div><h3>{t[1]}</h3><p>{t[2]}</p></div>'
        for t in d) + "</div>"


def r_myths(d):
    return "".join(
        f'<div class="mistake-card"><span class="mx">✕</span><div class="mb"><h4>"{m}"</h4><p>{f}</p></div></div>' for m, f in d)


def r_mythfact(d):
    return "".join(
        f'<div class="mf-card"><div class="mf-myth"><b>MYTH</b><span>{m}</span></div><div class="mf-fact"><b>FACT</b><span>{f}</span></div></div>'
        for m, f in d)


def r_checklist(d):
    return '<div class="checklist">' + "".join(
        f'<div class="check-item"><div class="check-box">✓</div><span>{c}</span></div>' for c in d) + "</div>"


def r_banner(d):
    return f'<div class="dark-banner"><blockquote>"{d[0]}"</blockquote><p>{d[1]}</p></div>'


def r_urgent(d):
    note = f"<p>{d['note']}</p>" if d.get("note") else ""
    return f'<div class="urgent"><h2>{d["h"]}</h2>{r_signs(d["items"], "⚠")}{note}</div>'


def r_derm(d):
    return (f'<div class="card card-warn"><h2 style="font-size:16px;margin-bottom:12px;">{d.get("h", "See a dermatologist if you notice:")}</h2>'
            f'{r_signs(d["items"], "⚠")}</div>')


def r_xlink(d):
    return (f'<a class="xlink" href="{d["href"]}"><div class="xl-emoji">{d["emoji"]}</div><div><h4>{d["h"]}</h4>'
            f'<p>{d["p"]}</p><span class="xl-go">{d["go"]} →</span></div></a>')


def r_intro(d):
    return f'<p class="section-intro">{d}</p>'


R = {k[2:]: v for k, v in globals().items() if k.startswith("r_")}


def render(g):
    body = ""
    for sec in g["sections"]:
        lab, parts = sec[0], sec[1:]
        inner = label(lab) if lab else ""
        for kind, data in parts:
            inner += R[kind](data)
        body += wrap(inner)
    intro = "".join(f"<p>{p}</p>" for p in g["intro"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{g['title']} · Dr. Pallavi Ahire-Shelke</title>
  <meta name="description" content="{e(g['subline'])}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet" />
  <style>
{CSS}
  </style>
</head>
<body>

  <nav class="back-nav"><a href="index.html">← All Guides</a></nav>

  <header class="site-header">
    <div class="pill">{g['pill']}</div>
    <h1>{g['h1']}<br><em>{g['h1_em']}</em></h1>
    <p class="subline">{g['subline']}</p>
    <p class="byline">{BYLINE}</p>
    <p class="philosophy">Inner &amp; Outer Beauty · Wholesome Beauty</p>
    <div class="dots">· · ·</div>
  </header>

  <section>
    <div class="wrapper">
      <div class="card card-accent">
        <h2>You commented "{g['trigger']}" — here's your guide {g.get('emoji', '🌿')}</h2>
        {intro}
      </div>
      <div class="quote-banner">
        <blockquote>"{g['quote']}"</blockquote>
        <cite>— Dr. Pallavi Ahire-Shelke</cite>
      </div>
    </div>
  </section>

{body}
  <section>
    <div class="wrapper">
      <div class="section-label">BOOK A CONSULTATION</div>
      <div class="contact-card">
        <div class="contact-header">
          <h2>Dr. Pallavi Ahire-Shelke</h2>
          <p class="creds">MBBS, MD, DNB, DDV · Gold Medalist Dermatologist</p>
          <p class="tagline">{g['tagline']}</p>
        </div>
        <div class="contact-grid">
          <div class="contact-cell"><div class="cc-icon">📍</div><div class="cc-label">Clinic</div><div class="cc-detail">Skin Ethics Clinic, Baner, Pune</div></div>
          <a class="contact-cell" href="tel:+919028291234"><div class="cc-icon">📞</div><div class="cc-label">Phone</div><div class="cc-detail">+91 90282 91234</div><div class="cc-action">Book a consultation</div></a>
          <a class="contact-cell" href="https://www.instagram.com/drpallaviahireshelke/" target="_blank"><div class="cc-icon">📸</div><div class="cc-label">Instagram</div><div class="cc-detail">@drpallaviahireshelke</div><div class="cc-action">Daily skin education</div></a>
          <a class="contact-cell" href="https://wa.me/919028291234" target="_blank"><div class="cc-icon">💬</div><div class="cc-label">WhatsApp</div><div class="cc-detail">Quick queries welcome</div><div class="cc-action">Message us</div></a>
        </div>
      </div>
    </div>
  </section>

  <div class="disclaimer">
    This guide is for educational purposes only and does not constitute medical advice. {g.get('disclaimer', 'Results vary from person to person. Please consult a qualified dermatologist before starting any treatment.')}
  </div>

  <footer>
    <div class="footer-grid">
      <div class="footer-col"><h4>Contact</h4><p>Skin Ethics Clinic<br>Baner, Pune<br>+91 90282 91234</p></div>
      <div class="footer-col"><h4>Follow Us</h4><p>@drpallaviahireshelke<br>Instagram<br><em>Wholesome Beauty · Inner &amp; Outer</em></p></div>
    </div>
    <hr class="footer-divider" />
    <div class="footer-bottom">
      <span>Dr. Pallavi Ahire-Shelke · MBBS, MD, DNB, DDV</span>
      <span>Skin Ethics Clinic, Baner, Pune</span>
    </div>
  </footer>

</body>
</html>
"""


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.GUIDE


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for p in sorted((SRC / "guides").glob("*.py")):
        g = load(p)
        if want and g["slug"] not in want:
            continue
        out = ROOT / f"guide-{g['slug']}.html"
        out.write_text(render(g))
        print("built", out.name)
