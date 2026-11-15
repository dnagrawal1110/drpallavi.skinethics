GUIDE = dict(
    slug="peel-types", trigger="PEEL", emoji="🧪",
    title="How Peels Differ by Skin Type",
    pill="YOUR PEEL TYPES GUIDE",
    h1="Not All Peels", h1_em="Are the Same",
    subline="The common peel acids, how depth changes downtime and risk, what suits Indian skin, and why strong peels don't belong at home.",
    intro=[
        "In the carousel, I explained that the acid, its strength and its depth all change what a peel does.",
        "This guide explains the common peels in simple words, so you know what to ask your dermatologist.",
    ],
    quote="A peel should be chosen for your skin, never copied from someone else's routine.",
    tagline="Find out which peel, if any, suits your skin",
    disclaimer="Peels are a medical procedure. The right acid, strength and number of sessions can only be decided after your skin is examined.",
    sections=[
        ("THE COMMON PEEL ACIDS", ("table", [
            ("Glycolic acid", "A small AHA that works on dullness, uneven tone and texture"),
            ("Lactic acid", "A gentler AHA, often chosen for dry or sensitive skin"),
            ("Mandelic acid", "A larger, slower AHA, often chosen for darker and sensitive skin"),
            ("Salicylic acid", "Oil-soluble, works inside pores. Often used for oily and acne-prone skin"),
            ("TCA and combination peels", "Stronger peels for deeper concerns, done only by a dermatologist"),
        ]), ("intro", "These are examples. Your dermatologist may use other acids or combinations.")),
        ("HOW DEEP THE PEEL GOES", ("concerns", [
            dict(emoji="🌤️", tag="SUPERFICIAL", h="Light peels", l1="What to expect", p1="Little or no visible peeling. Mild redness that settles quickly. Usually several sessions.", l2="Often used for", p2="Dullness, mild tan, oily skin and mild acne."),
            dict(emoji="🌗", tag="MEDIUM", h="Stronger peels", l1="What to expect", p1="Visible peeling for several days and more downtime.", l2="Good to know", p2="More effect, but more risk of irritation and dark patches on brown skin, so careful selection matters."),
            dict(emoji="🌑", tag="DEEP", h="Deep peels", l1="What to expect", p1="Significant downtime and the highest risk.", l2="Good to know", p2="Rarely chosen for brown skin because of the risk of pigment changes."),
        ])),
        ("WHY INDIAN SKIN NEEDS CARE", ("intro", "Brown skin makes pigment easily when it is irritated. An aggressive peel can leave dark patches that take months to fade. That's why dermatologists often start mild, test, prepare the skin and build up slowly.")),
        ("MYTHS VS FACTS", ("mythfact", [
            ("More peeling means a better result.", "Many effective peels cause little visible peeling. Heavy peeling is not a sign of success."),
            ("A strong peel from online is the same thing.", "Strong acids used at home are a common cause of burns and dark patches."),
            ("One peel will fix my pigmentation.", "Most concerns need a course of sessions, plus daily sunscreen to hold the result."),
        ])),
        ("AFTER A PEEL", ("dosdonts", (
            "Do",
            ["Use sunscreen every day", "Moisturise with something gentle", "Follow the aftercare you were given"],
            "Don't",
            ["Pick or pull peeling skin", "Use scrubs or strong actives until your doctor says so", "Wax or thread the area for a few days"],
        )), ("xlink", dict(href="guide-peel.html", emoji="🌿", h="Wondering if a peel hurts?", p="What a peel feels like and what happens in a session.", go="Read the Peel Basics Guide"))),
        ("SAVE THIS ⭐", ("checklist", [
            "My peel was chosen after my skin was examined",
            "I know how much downtime to expect",
            "I'm not using strong acids at home",
            "Sunscreen every day after a peel",
        ])),
    ],
)
