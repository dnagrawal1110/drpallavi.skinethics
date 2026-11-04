GUIDE = dict(
    slug="lift", trigger="LIFT", emoji="✨",
    title="Non-Surgical Lift Comparison",
    pill="NON-SURGICAL LIFT COMPARISON",
    h1="HIFU, Threads or Filler?", h1_em="Which One Is For You?",
    subline="How each one works, what it's best for, the downtime, and how long results last, all on one page.",
    intro=[
        "In the video, I explained how HIFU uses focused ultrasound to tighten the deeper support layer of the skin.",
        "But HIFU isn't the only non-surgical lift. Threads and fillers lift in different ways and suit different problems. Here's how the three compare.",
    ],
    quote="The right treatment depends on what's actually changing in your face: skin laxity, sagging or lost volume.",
    tagline="Find out which lift suits your face",
    sections=[
        ("FIRST, WHAT'S CHANGING?", ("table", [
            ("Skin is loosening", "Mild laxity along the jawline and neck → HIFU"),
            ("Tissue is sagging", "Cheeks or jowls moving down → threads"),
            ("Volume is lost", "Flat cheeks, hollows, deep folds → filler"),
        ]), ("intro", "Many faces have a mix of all three, which is why treatments are often combined.")),
        ("THE THREE, SIDE BY SIDE", ("concerns", [
            dict(emoji="🔊", tag="HIFU", h="High Intensity Focused Ultrasound", l1="How it works", p1="Ultrasound energy creates tiny heat points at a set depth under the skin, which triggers new collagen. The surface stays intact.", l2="At a glance", p2="<strong>Best for:</strong> early, mild to moderate laxity. <strong>Downtime:</strong> little to none, maybe mild redness or tenderness. <strong>Results:</strong> build gradually over 2–3 months and usually last around a year, with maintenance."),
            dict(emoji="🧵", tag="Thread Lift", h="Dissolvable PDO Threads", l1="How it works", p1="Fine threads with tiny cogs are placed under the skin to hold and lift tissue, and they trigger collagen as they dissolve.", l2="At a glance", p2="<strong>Best for:</strong> mild to moderate sagging of cheeks and jowls. <strong>Downtime:</strong> a few days of swelling or tightness. <strong>Results:</strong> visible soon after and usually last several months to over a year, depending on your skin."),
            dict(emoji="💧", tag="Filler", h="Hyaluronic Acid Filler", l1="How it works", p1="A gel restores lost volume, which can support and lift the face from underneath.", l2="At a glance", p2="<strong>Best for:</strong> volume loss in cheeks, temples and under-eyes. <strong>Downtime:</strong> mild swelling or bruising for a few days. <strong>Results:</strong> immediate and usually last months to about a year or more, and can be dissolved."),
        ])),
        ("WHAT NONE OF THEM CAN DO", ("card", dict(warn=True, h="Not a replacement for a facelift", p=["If the skin has sagged a lot, no non-surgical lift will match a surgical facelift. All three give natural, gradual improvement for early to moderate changes, and all need maintenance because ageing continues."]))),
        ("QUESTIONS TO ASK IN YOUR CONSULTATION", ("checklist", [
            "What's the main change in my face: laxity, sagging or volume?",
            "Would one treatment work, or a combination?",
            "How many sessions, and how long will results last for me?",
            "What's the downtime, and when can I go back to work?",
            "What does maintenance look like over a year?",
        ]), ("xlink", dict(href="guide-filler.html", emoji="💉", h="Considering filler?", p="Read my myths vs facts guide before you book.", go="Read the Filler Guide"))),
    ],
)
