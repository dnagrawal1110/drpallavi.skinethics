GUIDE = dict(
    slug="laser-aftercare", trigger="TONE", emoji="☀️",
    title="Laser Aftercare Guide",
    pill="YOUR LASER AFTERCARE GUIDE",
    h1="Keep Your Results.", h1_em="Aftercare Is Half the Work.",
    subline="How much sunscreen to use and how, what to pause, and what to avoid in the first 7 days after laser toning.",
    intro=[
        "In the video, I explained that laser toning evens out extra pigment. It doesn't change your natural skin colour.",
        "The most common question is whether pigmentation will come back. A lot of the answer is in your aftercare. Here's exactly what to do.",
    ],
    quote="Skip sunscreen after laser, and the improvement you've gained can go back.",
    tagline="Get your pigmentation type checked before laser",
    disclaimer="Always follow the specific aftercare instructions your doctor gives you, as they depend on your skin and the settings used.",
    sections=[
        ("SUNSCREEN: HOW MUCH", ("card", dict(h="The two-finger rule", p=[
            "Squeeze sunscreen along the full length of your index and middle fingers. That's about the right amount for your face and neck.",
            "Most people use far less than this, which gives much less protection than the SPF on the label.",
        ])), ("table", [
            ("SPF", "SPF 30 or higher, broad spectrum (protects from UVA and UVB)"),
            ("When", "Every morning, about 15 minutes before stepping out, even indoors near windows"),
            ("Reapply", "Every 2–3 hours if you're outdoors, sweating or near a window"),
            ("Extra cover", "Cap, umbrella or dupatta when you're in direct sun"),
        ])),
        ("THE FIRST 7 DAYS", ("timeline", [
            ("Day 1–2", "Calm and soothe", "Mild redness or warmth is common. Wash with a gentle cleanser and use a plain moisturiser and sunscreen."),
            ("Day 3–4", "Stay gentle", "Your skin may feel slightly dry. Keep your routine simple and avoid rubbing or scrubbing."),
            ("Day 5–7", "Slowly back to normal", "Restart actives only when your doctor says so. Keep sunscreen strict.", "grow"),
        ])),
        ("PAUSE THESE (UNTIL YOUR DOCTOR SAYS)", ("table", [
            ("Retinoids", "Retinol, tretinoin, adapalene"),
            ("Exfoliating acids", "Glycolic, salicylic, lactic acid"),
            ("Scrubs and peels", "Physical scrubs, home peels, peel-off masks"),
            ("Waxing and threading", "On the treated area for a few days"),
        ])),
        ("AVOID IN THE FIRST WEEK", ("dosdonts", (
            "Do",
            ["Use sunscreen generously, every day", "Moisturise twice a day", "Drink enough water", "Keep your next session date"],
            "Don't",
            ["Sit in direct sun or go for a beach holiday", "Use saunas, steam or very hot showers", "Do heavy workouts that make you sweat a lot", "Pick or rub your skin"],
        ))),
        ("", ("banner", ("Laser toning gives even, clear skin. It's not a fairness treatment.", "Results build over multiple sessions, and sun protection is what keeps them."))),
        ("SAVE THIS CHECKLIST ⭐", ("checklist", [
            "I use two fingers' worth of sunscreen every morning",
            "I reapply when I'm out or sweating",
            "I've paused retinoids and acids for now",
            "I'm avoiding saunas, steam and harsh sun this week",
            "I'll call the clinic if I see blisters or dark patches",
        ])),
    ],
)
