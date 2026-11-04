GUIDE = dict(
    slug="mnrf", trigger="MNRF", emoji="🪡",
    title="Scar Treatments Compared",
    pill="SCAR TREATMENTS COMPARED",
    h1="MNRF, CO2 or Microneedling?", h1_em="All on One Page.",
    subline="Downtime, pigmentation risk, number of sessions and which skin each treatment suits.",
    intro=[
        "In the video, I explained that MNRF is microneedling plus radiofrequency heat: the same idea, with deeper action.",
        "Here's how it compares with CO2 laser and simple microneedling, so you know what to ask about in your consultation.",
    ],
    quote="MNRF = needles + heat. Same idea, deeper action.",
    tagline="Find the right scar treatment for your skin",
    sections=[
        ("THE THREE, SIDE BY SIDE", ("concerns", [
            dict(emoji="📌", tag="Microneedling", h="Needles Only", l1="How it works", p1="Fine needles create controlled micro-injuries that start the skin's repair process and new collagen.", l2="At a glance", p2="<strong>Downtime:</strong> 1–2 days of redness. <strong>Pigmentation risk:</strong> low. <strong>Sessions:</strong> usually several, a few weeks apart. <strong>Best for:</strong> mild scars, texture and pores."),
            dict(emoji="🪡", tag="MNRF", h="Needles + Radiofrequency", l1="How it works", p1="Needles deliver heat at a set depth inside the skin, for more collagen remodelling and tightening, with less surface damage.", l2="At a glance", p2="<strong>Downtime:</strong> 2–3 days of redness or tiny marks. <strong>Pigmentation risk:</strong> relatively low, often preferred for Indian skin. <strong>Sessions:</strong> usually 3–5, about a month apart. <strong>Best for:</strong> acne scars, open pores, mild laxity."),
            dict(emoji="🔥", tag="CO2 Laser", h="Ablative Fractional Laser", l1="How it works", p1="The laser treats tiny columns of skin. The untreated skin in between speeds healing as new collagen forms.", l2="At a glance", p2="<strong>Downtime:</strong> about 5–7 days of redness, scabbing and peeling. <strong>Pigmentation risk:</strong> higher in Indian skin, needs careful settings. <strong>Sessions:</strong> usually fewer, with longer gaps. <strong>Best for:</strong> moderate to deep boxcar and mixed scars."),
        ])),
        ("QUICK COMPARISON", ("table", [
            ("Least downtime", "Microneedling, then MNRF"),
            ("Lowest pigmentation risk", "Microneedling and MNRF"),
            ("Strongest single session", "CO2 laser"),
            ("Pores and mild laxity too", "MNRF"),
        ])),
        ("WHAT ALL THREE NEED", ("dosdonts", (
            "Do",
            ["Control active pimples first", "Follow pre-care and post-care exactly", "Use sunscreen strictly", "Keep the gap between sessions your doctor advises"],
            "Don't",
            ["Use at-home dermarollers on scars", "Pick at scabs or peeling skin", "Start strong actives right after a session", "Expect results after one session"],
        ))),
        ("", ("banner", ("Depth, energy and the gap between sessions are decided for your skin.",
                         "Your skin type and your scar type both matter. Often the best plan combines treatments, such as subcision with MNRF."))),
        ("ASK IN YOUR CONSULTATION ⭐", ("checklist", [
            "Which scar types do I have?",
            "Which treatment, or combination, suits my skin?",
            "How many sessions, and how far apart?",
            "How much downtime should I plan for?",
            "How do we reduce my pigmentation risk?",
        ]), ("xlink", dict(href="guide-scar-types.html", emoji="🔍", h="Not sure what type your scars are?", p="Learn to recognise ice pick, boxcar and rolling scars.", go="Read the Scar Types Guide"))),
    ],
)
