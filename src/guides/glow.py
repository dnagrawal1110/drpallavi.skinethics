GUIDE = dict(
    slug="event-glow", trigger="GLOW", emoji="✨",
    title="Event-Ready Skin Guide",
    pill="YOUR EVENT-READY SKIN GUIDE",
    h1="Big Day Coming?", h1_em="Your 7-Day Glow Plan.",
    subline="When to book your HydraFacial, what to pause, and a simple day-by-day plan for fresh, hydrated skin on the day.",
    intro=[
        "In the video, I explained what a HydraFacial really does: it exfoliates, cleans out the pores and pushes hydration back into the skin.",
        "Timing matters as much as the treatment. This guide gives you a simple 7-day plan, so your skin looks its best on the day and not the day after.",
    ],
    quote="Great for glow, not a cure for problems. And for an event, the plan matters as much as the facial.",
    tagline="Plan your event-ready skin with a dermatologist",
    sections=[
        ("WHAT A HYDRAFACIAL DOES", ("steps", [
            ("Gentle exfoliation", "The dull top layer of dead skin is lifted away, so light reflects better off your skin."),
            ("Pore cleaning", "A suction tip helps pull out oil and debris from inside the pores. That's what you see in the container."),
            ("Hydration", "Hydrating serums are infused into fresh skin, which is why it looks plump and glowing right after."),
        ])),
        ("GOOD FOR — AND NOT FOR", ("dosdonts", (
            "Great for",
            ["Fresh, hydrated skin before an event", "Dull, tired-looking skin", "Routine skin maintenance", "Mild congestion and clogged pores"],
            "Not a treatment for",
            ["Melasma", "Deep acne scars", "Active, painful acne", "Long-term pigmentation"],
        )), ("card", dict(warn=True, h="The glow isn't permanent", p=["Your skin keeps renewing itself, so the effect fades over a few weeks. That's why HydraFacial works best as regular maintenance."]))),
        ("WHEN TO BOOK IT", ("card", dict(p=[
            "<strong>Book your HydraFacial 2–5 days before the event.</strong> That's close enough for the glow to show and leaves time for any mild redness to settle.",
            "Trying it for the first time? Do a trial session a few weeks earlier, so you know how your skin responds before the big day.",
        ]))),
        ("YOUR 7-DAY PLAN", ("intro", "A simple timeline. Your dermatologist may adjust it for your skin."), ("timeline", [
            ("Day 7", "Freeze your routine", "No new products from today. Stick to what your skin already knows. Ask your doctor whether to pause strong actives like retinoids or exfoliating acids."),
            ("Day 6–5", "Finish hair removal", "Get facial waxing, threading or bleach done now, not in the last 2 days, and never on the same day as your facial."),
            ("Day 5–2", "HydraFacial window", "Book your session in this window. Skip makeup for the rest of that day and let your skin breathe.", "grow"),
            ("Day 2", "Gentle only", "Cleanser, moisturiser and sunscreen. No scrubs, no peels, no home face packs."),
            ("Day 1", "Hydrate and rest", "Drink enough water, keep salty and fried food light, and get a full night's sleep."),
            ("Event day", "Prep and glow", "Gentle cleanse, a light moisturiser, then sunscreen. Let it set for a few minutes before makeup.", "grow"),
        ])),
        ("WHAT TO AVOID IN THE LAST WEEK", ("myths", [
            ("Let me try a new serum for extra glow", "A new product this close to the event can cause breakouts or irritation. Save experiments for after."),
            ("A peel the day before will make me brighter", "Peels can leave redness and flaking for days. They need to be planned weeks ahead, not the night before."),
            ("I'll do a home scrub before makeup", "Scrubbing the morning of the event can leave your skin red and sensitive under makeup."),
            ("Sunscreen isn't needed, I'm wearing makeup", "Makeup isn't sun protection. A tan before the event undoes the glow."),
        ])),
        ("SAVE THIS CHECKLIST ⭐", ("checklist", [
            "No new products in the last 7 days",
            "Waxing or threading done at least 2 days before",
            "HydraFacial booked 2–5 days before the event",
            "Gentle routine only for the last 2 days",
            "Sunscreen every day, including event day",
            "Water and sleep on the day before",
        ])),
        ("", ("banner", ("Glow for great skin days. Diagnosis for skin problems.",
                         "If you have acne, pigmentation or scars, a facial alone won't fix them. Start treatment a few months before a big event, not a few days."))),
    ],
)
