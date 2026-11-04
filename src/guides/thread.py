GUIDE = dict(
    slug="thread-recovery", trigger="THREAD", emoji="🧵",
    title="Thread Lift Recovery Guide",
    pill="YOUR THREAD LIFT RECOVERY GUIDE",
    h1="After Your Thread Lift.", h1_em="Day by Day.",
    subline="What to expect each day, how to sleep, what to avoid for a few weeks, and when to call the clinic.",
    intro=[
        "In the video, I explained how dissolvable threads give a subtle lift and help collagen form.",
        "The next question is always: how much will it hurt, and when will I look normal? Here's what recovery usually looks like.",
    ],
    quote="A subtle lift without surgery, with a few days of care afterwards.",
    tagline="Find out if a thread lift suits your face",
    disclaimer="Recovery varies from person to person. Always follow the instructions your doctor gives you.",
    sections=[
        ("ABOUT THE DISCOMFORT", ("card", dict(p=["The area is numbed before the procedure, so most people feel pressure rather than pain. Afterwards, mild soreness, tightness or swelling is common and usually settles with the medicines your doctor advises."]))),
        ("RECOVERY, DAY BY DAY", ("timeline", [
            ("Day 1–2", "Swelling and tightness", "Mild swelling, tenderness and a pulling feeling are normal. Use cold compresses if advised."),
            ("Day 3–5", "Settling down", "Swelling starts to reduce. Small dimples or bunching can appear and usually smooth out."),
            ("Week 1–2", "Looking normal", "Most people are back to work and social plans. Some tightness when you yawn or smile is normal.", "grow"),
            ("Weeks 2–4", "Stay careful", "Keep avoiding big facial movements and pressure on the face."),
            ("Months 1–3", "Collagen builds", "As the threads dissolve, collagen forms around them and supports the skin.", "grow"),
        ])),
        ("HOW TO SLEEP", ("signs", [
            "Sleep on your back with your head slightly raised for the first week",
            "Avoid sleeping on your face or side",
            "Use a soft pillow and avoid pressing your face into it",
        ])),
        ("AVOID FOR A FEW WEEKS", ("dosdonts", (
            "Do",
            ["Eat soft foods for the first few days", "Keep your face clean and dry", "Take medicines as prescribed", "Keep your follow-up appointment"],
            "Don't",
            ["Open your mouth very wide, chew hard or chew gum", "Have facial massages, facials or dental work", "Do heavy workouts or use saunas", "Rub, press or pull your skin"],
        ))),
        ("", ("urgent", dict(h="Call the clinic if you notice:", items=[
            "Pain that keeps getting worse instead of better",
            "Redness, heat, pus or fever",
            "A thread end poking through the skin",
            "Swelling on one side that keeps increasing",
        ]))),
        ("SAVE THIS CHECKLIST ⭐", ("checklist", [
            "I'm sleeping on my back with my head raised",
            "I'm eating soft foods for the first few days",
            "I'm avoiding wide mouth movements and facial massage",
            "No gym, sauna or dental work for now",
            "I know when to call the clinic",
        ]), ("xlink", dict(href="guide-lift.html", emoji="✨", h="Thread lift, HIFU or filler?", p="Compare how they work and how long results last.", go="Read the Lift Comparison"))),
    ],
)
