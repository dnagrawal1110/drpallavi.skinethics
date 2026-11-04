GUIDE = dict(
    slug="kids-skin", trigger="PATCH", emoji="🧒",
    title="Safe Moisturiser and Sunscreen for Kids",
    pill="SAFE SKINCARE FOR KIDS",
    h1="White Patches on Your Child?", h1_em="Moisturise and Protect.",
    subline="What to look for in a moisturiser and sunscreen for your child, how to use them, and when to see a dermatologist.",
    intro=[
        "In the video, I explained that light, slightly rough white patches on a child's cheeks are often pityriasis alba, not calcium deficiency or worms.",
        "The main care is a gentle moisturiser and sunscreen. Here's how to choose safe ones for your child and use them well.",
    ],
    quote="Not every white patch is the same.",
    tagline="Get your child's skin checked",
    disclaimer="Ask your dermatologist or paediatrician for specific product names suited to your child's skin. Babies under 6 months should be kept out of direct sun rather than using sunscreen.",
    sections=[
        ("MOISTURISER: WHAT TO LOOK FOR", ("dosdonts", (
            "Look for",
            ["Fragrance-free", "Ceramides, glycerin or petrolatum", "Cream or ointment, not a thin lotion, for dry skin", "Labelled for sensitive or baby skin"],
            "Avoid",
            ["Added perfume or strong scents", "Steroid or 'fairness' creams", "Harsh soaps that strip the skin", "Home remedies like lemon on the face"],
        ))),
        ("SUNSCREEN: WHAT TO LOOK FOR", ("table", [
            ("Type", "Mineral or physical sunscreen with zinc oxide or titanium dioxide is usually gentler"),
            ("SPF", "SPF 30 or higher, broad spectrum"),
            ("Texture", "Fragrance-free cream or lotion, or a stick for the face"),
            ("Age", "For babies under 6 months, use shade and clothing instead of sunscreen"),
        ])),
        ("HOW TO USE THEM", ("steps", [
            ("Moisturise twice a day", "Apply right after the bath while the skin is slightly damp, and again at night."),
            ("Sunscreen before outdoor play", "Apply 15 minutes before going out, and again every 2 hours outdoors."),
            ("Add a cap", "A cap or hat protects the face better than sunscreen alone."),
        ])),
        ("", ("banner", ("No calcium syrup or worm medicine needed.", "Pityriasis alba is common, isn't contagious, and fades slowly over time with gentle care."))),
        ("", ("derm", dict(h="See a dermatologist if the patch:", items=[
            "Is chalk-white rather than light",
            "Is spreading or getting bigger",
            "Has reduced feeling or numbness",
            "Is itchy, red or scaly",
            "Doesn't improve after a few months of care",
        ]))),
    ],
)
