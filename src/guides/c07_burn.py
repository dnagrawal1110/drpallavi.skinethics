GUIDE = dict(
    slug="burn-first-aid", trigger="BURN", emoji="🧯",
    title="Diwali Night First Aid Card",
    pill="YOUR DIWALI FIRST AID CARD",
    h1="Burn First Aid", h1_em="for Diwali Night",
    subline="What to do in the first minutes after a burn, what never to put on it, and when to go to hospital. Save it and share it with your family.",
    intro=[
        "In the carousel, I explained that toothpaste, ice, ghee and haldi do not cool a burn. Cool running water does.",
        "Save this card on your phone and share it with your family before Diwali night.",
    ],
    quote="Cool running water for 20 minutes is the first and best step.",
    tagline="Wishing you a safe Diwali",
    disclaimer="This card is for first aid only. For serious burns, eye injuries or any burn in a child, go to emergency care immediately.",
    sections=[
        ("FIRST AID IN 4 STEPS", ("steps", [
            ("Stop the burning", "Move away from the fire. If clothes catch fire: stop, drop and roll."),
            ("Cool it", "Hold the burn under cool running tap water for 20 minutes. Not ice, not iced water."),
            ("Remove tight things", "Take off rings, bangles and tight clothing near the burn before it swells, unless they are stuck to the skin."),
            ("Cover it", "Cover loosely with cling film or a clean, non-fluffy cloth."),
        ])),
        ("NEVER PUT THESE ON A BURN", ("myths", [
            ("Toothpaste", "It traps heat and can cause infection."),
            ("Ice", "It can damage the skin further."),
            ("Ghee, butter or oil", "They hold the heat in."),
            ("Haldi or other home pastes", "They can cause infection and make it hard for the doctor to see the burn."),
            ("Popping blisters", "Blisters protect the skin underneath. Leave them alone."),
        ])),
        ("", ("urgent", dict(h="Go to hospital if:", items=[
            "The burn is bigger than the person's palm",
            "It is on the face, hands, feet, genitals or a joint",
            "It looks white, leathery or charred",
            "A child or an elderly person is burned",
            "The person breathed in smoke, or has trouble breathing",
            "Pain is severe, or the burn is from a chemical or electricity",
        ], note="If a firework injures an eye: do not rub it, do not wash it out forcefully, and go to emergency immediately."))),
        ("BEFORE YOU LIGHT THE FIRST DIYA", ("checklist", [
            "Everyone is wearing cotton, not synthetic clothes",
            "A bucket of water is kept nearby",
            "Children are at a safe distance and supervised",
            "Fireworks are lit at arm's length, never held in the hand",
            "Hair and dupattas are tied back near diyas",
        ])),
    ],
)
