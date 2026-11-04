GUIDE = dict(
    slug="glow-compare", trigger="CARBON", emoji="✨",
    title="Glow Treatments Compared",
    pill="GLOW TREATMENTS COMPARED",
    h1="Carbon Peel, HydraFacial", h1_em="or Chemical Peel?",
    subline="Which glow treatment fits oily, dry or sensitive skin, with downtime and what each one can and can't do.",
    intro=[
        "In the video, I explained that a carbon peel is a glow and oil-control treatment, not a fix for every skin problem.",
        "Carbon peel, HydraFacial and chemical peels all brighten the skin, but they suit different skin types. Here's how to choose.",
    ],
    quote="A glow treatment is great for glow. Skin problems need a diagnosis first.",
    tagline="Find the right glow treatment for your skin",
    sections=[
        ("SKIN TYPE × TREATMENT", ("table", [
            ("Oily, large pores", "Carbon peel is a great fit. A salicylic chemical peel can also help"),
            ("Dry, dehydrated", "HydraFacial is the best fit, because it adds hydration"),
            ("Sensitive", "HydraFacial with gentle settings. Peels only after a doctor's assessment"),
            ("Dull, uneven tone", "Chemical peel, chosen and planned by your doctor"),
            ("Before an event", "HydraFacial or carbon peel, as both have little or no downtime"),
        ])),
        ("THE THREE, SIDE BY SIDE", ("concerns", [
            dict(emoji="⚫", tag="Carbon Peel", h="Hollywood Facial", l1="How it works", p1="A fine carbon lotion settles into the pores and binds to oil. A laser then targets the carbon, creating gentle, controlled heat.", l2="At a glance", p2="<strong>Best for:</strong> oily skin, large pores, dullness. <strong>Downtime:</strong> almost none."),
            dict(emoji="💧", tag="HydraFacial", h="Cleanse + Hydrate", l1="How it works", p1="Gentle exfoliation, suction to clean the pores, then hydrating serums infused into the skin.", l2="At a glance", p2="<strong>Best for:</strong> dry, dull or tired skin and pre-event glow. <strong>Downtime:</strong> none."),
            dict(emoji="🧪", tag="Chemical Peel", h="Controlled Exfoliation", l1="How it works", p1="An acid solution removes damaged surface layers so fresher skin grows back. The acid and strength are chosen for your skin.", l2="At a glance", p2="<strong>Best for:</strong> uneven tone, mild pigmentation, acne-prone skin. <strong>Downtime:</strong> none to a few days of peeling, depending on the strength."),
        ])),
        ("WHAT THEY'RE NOT", ("card", dict(warn=True, h="Not the main treatment for:", p=["Melasma, deep pigmentation and acne scars. These need a proper diagnosis and a targeted plan. Glow treatments can support that plan, but they don't replace it."]))),
        ("", ("banner", ("All three need maintenance.", "Your skin keeps renewing itself, so the glow fades over weeks. Regular sessions and sunscreen keep it going."))),
        ("BEFORE YOU BOOK ⭐", ("checklist", [
            "I know my skin type: oily, dry, combination or sensitive",
            "I want glow and maintenance, not a cure for a skin condition",
            "I've told my doctor about any actives I use",
            "I'll use sunscreen after every session",
        ]), ("xlink", dict(href="guide-event-glow.html", emoji="✨", h="Have a function coming up?", p="Follow my 7-day event-ready skin plan.", go="Read the Event Glow Guide"))),
    ],
)
