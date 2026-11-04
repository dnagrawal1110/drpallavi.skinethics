GUIDE = dict(
    slug="spf", trigger="SPF", emoji="☀️",
    title="How to Choose and Use Sunscreen",
    pill="YOUR SUNSCREEN GUIDE",
    h1="Sunscreen Every Day?", h1_em="Yes, Even Indoors.",
    subline="How to choose a sunscreen for your skin type, how much to apply, and when to reapply.",
    intro=[
        "In the video, I explained that window glass blocks most UVB but lets UVA through, and UVA is a big cause of pigmentation and ageing.",
        "Here's how to choose the right sunscreen for your skin type, and how much to actually use.",
    ],
    quote="Sunscreen isn't makeup. It's daily skin protection.",
    tagline="Get a sunscreen recommendation for your skin",
    sections=[
        ("WHAT TO LOOK FOR", ("table", [
            ("SPF 30 or higher", "Protects against UVB, which causes sunburn"),
            ("Broad spectrum", "Protects against UVA too, which causes pigmentation and ageing"),
            ("PA+++ or higher", "A rating for UVA protection, often seen on Asian sunscreens"),
        ])),
        ("CHOOSE BY SKIN TYPE", ("concerns", [
            dict(emoji="💧", tag="Oily / Acne-Prone", h="Light and Non-Comedogenic", l1="Look for", p1="Gel or fluid textures, labelled non-comedogenic or oil-free, with a matte finish."),
            dict(emoji="🌵", tag="Dry", h="Creamy and Hydrating", l1="Look for", p1="Cream textures with hydrating ingredients like glycerin, ceramides or hyaluronic acid."),
            dict(emoji="🌸", tag="Sensitive", h="Gentle and Fragrance-Free", l1="Look for", p1="Mineral sunscreens with zinc oxide or titanium dioxide, fragrance-free."),
            dict(emoji="🎨", tag="Pigmentation / Melasma", h="Tinted With Iron Oxides", l1="Look for", p1="Tinted sunscreens with iron oxides also help protect against visible light, which can worsen pigmentation."),
        ])),
        ("HOW MUCH TO APPLY", ("card", dict(h="The two-finger rule", p=[
            "Squeeze sunscreen along the full length of your index and middle fingers. That's about right for your face and neck.",
            "Most people apply much less, which gives far less protection than the SPF on the bottle.",
        ]))),
        ("WHEN TO APPLY AND REAPPLY", ("timeline", [
            ("Morning", "Last step of skincare", "Apply after moisturiser, about 15 minutes before going out or starting your day by a window."),
            ("Every 2–3 hours", "Reapply", "If you're outdoors, sweating, or sitting near a window or in a car."),
            ("After swimming or sweating", "Reapply again", "Even water-resistant sunscreen needs reapplying.", "grow"),
        ])),
        ("MYTHS", ("myths", [
            ("I'm indoors, I don't need it", "UVA passes through window glass and causes pigmentation, especially on the side facing the window."),
            ("Dark skin doesn't need sunscreen", "Indian skin burns less but gets pigmentation more easily."),
            ("It's cloudy or winter, I can skip it", "UV rays come through clouds and in every season."),
            ("My makeup has SPF, that's enough", "You'd need far more makeup than anyone uses to get that protection."),
        ])),
        ("SAVE THIS ⭐", ("checklist", [
            "SPF 30+, broad spectrum",
            "The right texture for my skin type",
            "Two fingers' worth every morning",
            "Reapply when I'm out or near a window",
        ])),
    ],
)
