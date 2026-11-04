GUIDE = dict(
    slug="itch", trigger="ITCH", emoji="🩹",
    title="Itching and Rash Guide",
    pill="YOUR ITCHING &amp; RASH GUIDE",
    h1="Itchy Underarms or Groin?", h1_em="Don't Grab Any Cream.",
    subline="Common causes of itchy rashes in skin folds, the creams to avoid, daily habits that help, and when to see a dermatologist.",
    intro=[
        "In the video, I explained that not every red, itchy rash is fungal, and that steroid combination creams can make a fungal infection spread.",
        "This guide covers the common causes, what helps at home, and the signs that mean you should see a dermatologist.",
    ],
    quote="First diagnosis, then the right cream.",
    tagline="Get your rash diagnosed and treated properly",
    disclaimer="This guide doesn't diagnose your rash. Please see a dermatologist before starting any medicated cream.",
    sections=[
        ("COMMON CAUSES IN SKIN FOLDS", ("concerns", [
            dict(emoji="🍄", tag="Cause 1", h="Fungal Infection (Daad)", l1="What it looks like", p1="Itchy, red, ring-like patches with a raised edge that slowly spread outwards.", l2="Needs", p2="The right antifungal for the full course."),
            dict(emoji="🔥", tag="Cause 2", h="Intertrigo (Friction Rash)", l1="What it looks like", p1="Red, raw, sometimes moist skin where folds rub together, worse with heat and sweat.", l2="Needs", p2="Keeping the area dry, and sometimes a mild prescribed cream."),
            dict(emoji="🧴", tag="Cause 3", h="Contact Dermatitis", l1="What it looks like", p1="Itchy redness where a deodorant, soap, detergent or hair-removal cream touched the skin.", l2="Needs", p2="Stopping the trigger, and treatment from a doctor."),
            dict(emoji="🌊", tag="Cause 4", h="Other Conditions", l1="What it looks like", p1="Psoriasis, eczema and bacterial infections can also cause rashes in skin folds.", l2="Needs", p2="A proper examination, as treatments are very different."),
        ])),
        ("", ("card", dict(warn=True, h="Don't start these creams on your own", p=[
            "Betnovate, Panderm, Fourderm and other steroid or steroid combination creams can make a fungal infection spread, change how it looks, and make it harder to diagnose and treat.",
        ]))),
        ("DAILY HABITS THAT HELP", ("dosdonts", (
            "Do",
            ["Keep the area clean and fully dry", "Wear loose cotton clothes and innerwear", "Change out of sweaty clothes quickly", "Use your own towel"],
            "Don't",
            ["Wear tight, synthetic clothes", "Scratch, as it spreads infection and damages the skin", "Use random creams from the chemist", "Stop treatment when the itch stops"],
        ))),
        ("", ("derm", dict(h="See a dermatologist if the rash:", items=[
            "Keeps coming back",
            "Is spreading or getting bigger",
            "Hasn't improved in 1–2 weeks",
            "Is oozing, painful or has pus",
            "Appeared after using a steroid cream",
        ]))),
        ("SAVE THIS ⭐", ("checklist", [
            "I'm keeping the area clean and dry",
            "I've switched to loose cotton",
            "I've stopped any steroid combination cream, and will tell my doctor",
            "I'll get it diagnosed before using a new cream",
        ]), ("xlink", dict(href="guide-daad.html", emoji="🏠", h="Daad keeps coming back?", p="7 habits that stop ringworm spreading at home.", go="Read the Daad Guide"))),
    ],
)
