GUIDE = dict(
    slug="boost", trigger="BOOST", emoji="💧",
    title="Botox vs Filler vs Skin Booster",
    pill="BOTOX VS FILLER VS SKIN BOOSTER",
    h1="Which One Do You Need?", h1_em="Match the Problem.",
    subline="A simple chart: which problem each one treats, how it works, and how long it lasts.",
    intro=[
        "In the video, I explained that skin boosters improve skin quality from within, while fillers add volume in one place.",
        "Most confusion comes from mixing up three different problems. Find yours below, and the right treatment becomes clear.",
    ],
    quote="Right problem, right treatment.",
    tagline="Find out what your skin actually needs",
    sections=[
        ("THE PROBLEM → TREATMENT CHART", ("table", [
            ("Lines when you make expressions", "Frown lines, forehead lines, crow's feet → Botox"),
            ("Volume loss", "Flat cheeks, hollow under-eyes, deep folds → Filler"),
            ("Dull, dry, crepey skin", "Tired-looking skin with fine texture → Skin booster"),
        ])),
        ("HOW EACH ONE WORKS", ("concerns", [
            dict(emoji="😌", tag="Botox", h="Relaxes the Muscle", l1="How it works", p1="Softens the muscles that fold the skin into lines when you frown, smile or raise your eyebrows.", l2="Good to know", p2="Results show over a week or two and usually last a few months."),
            dict(emoji="💉", tag="Filler", h="Restores Volume", l1="How it works", p1="A hyaluronic acid gel is placed in a specific spot to replace lost volume and support the face.", l2="Good to know", p2="Results are immediate and usually last months to about a year or more. Hyaluronic acid fillers can be dissolved."),
            dict(emoji="💧", tag="Skin Booster", h="Improves Skin Quality", l1="How it works", p1="Hyaluronic acid spreads evenly through the skin to hydrate it from within and improve firmness and texture, without changing your face shape.", l2="Good to know", p2="Usually given as 2 sessions a few weeks apart, then maintenance."),
        ])),
        ("COMMON MIX-UPS", ("mythfact", [
            ("A skin booster will fill my hollows.", "Boosters improve skin quality. Real volume loss needs filler."),
            ("Filler will remove my forehead lines.", "Lines from muscle movement usually respond better to Botox."),
            ("One session of a booster will give a glow forever.", "Boosters need a course and maintenance, because skin keeps ageing."),
        ])),
        ("", ("banner", ("Is your problem volume, muscle movement or skin quality?", "Many people have a bit of all three, so the best results often come from a combination planned by your doctor."))),
        ("ASK YOURSELF ⭐", ("checklist", [
            "Do my lines appear mainly when I make expressions?",
            "Do my cheeks or under-eyes look hollow or flat?",
            "Does my skin look tired, dry or crepey even when I rest?",
            "Do I want to look fresher, not different?",
        ]), ("xlink", dict(href="guide-filler.html", emoji="💉", h="Thinking about filler?", p="How long it lasts, dissolving, and who shouldn't get it.", go="Read the Filler Guide"))),
    ],
)
