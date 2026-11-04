GUIDE = dict(
    slug="prp-check", trigger="PRP", emoji="🩸",
    title="Hair Loss Self-Check",
    pill="YOUR HAIR LOSS SELF-CHECK",
    h1="Is PRP Right for You?", h1_em="Start With 6 Questions.",
    subline="The 6 questions your dermatologist will ask, so you walk into your consultation prepared.",
    intro=[
        "In the video, I explained that PRP works best when the hair follicles are still alive, like in early pattern hair loss.",
        "Whether you're a good candidate depends on the type and cause of your hair loss. These 6 questions are the same ones I ask in clinic. Note your answers and bring them to your consultation.",
    ],
    quote="The question isn't whether to do PRP. It's what type of hair loss you have, and whether you're the right candidate.",
    tagline="Find out what's causing your hair loss",
    disclaimer="This self-check helps you prepare for a consultation. It is not a diagnosis. Diagnosis happens in clinic.",
    sections=[
        ("HOW PRP WORKS", ("steps", [
            ("A little blood is drawn", "A small amount of your own blood is taken, just like a routine blood test."),
            ("It's spun in a centrifuge", "Spinning separates the blood into layers. The yellow, platelet-rich layer is collected."),
            ("It's injected into thinning areas", "Platelets carry growth factors that may help support weak hair follicles."),
        ])),
        ("THE 6 QUESTIONS", ("concerns", [
            dict(emoji="🧭", tag="Question 1", h="What does your hair loss look like?", l1="Ask yourself", p1="Is it a widening parting, a receding hairline, a thinning crown, overall shedding, or round bald patches?", l2="Why it matters", p2="The pattern points to the type of hair loss. PRP is mainly used for pattern hair loss, not patchy hair loss."),
            dict(emoji="⏳", tag="Question 2", h="How long has it been happening?", l1="Ask yourself", p1="Did it start suddenly a few weeks ago, or has it been slowly getting thinner over months or years?", l2="Why it matters", p2="Sudden shedding often has a trigger. Slow thinning is more typical of pattern hair loss."),
            dict(emoji="👨‍👩‍👧", tag="Question 3", h="Does it run in your family?", l1="Ask yourself", p1="Do your parents, grandparents or siblings have thinning hair or baldness?", l2="Why it matters", p2="A family history makes pattern hair loss more likely."),
            dict(emoji="🤒", tag="Question 4", h="Any recent illness, stress or big change?", l1="Ask yourself", p1="In the last 3–6 months, did you have a high fever, surgery, childbirth, crash dieting, major stress or new medicines?", l2="Why it matters", p2="These can trigger temporary shedding that usually needs the trigger fixed, not PRP."),
            dict(emoji="🥗", tag="Question 5", h="How is your diet?", l1="Ask yourself", p1="Do you eat enough protein? Are you vegetarian, on a strict diet, or do you have heavy periods?", l2="Why it matters", p2="Low iron, vitamin D or B12 and low protein are common reasons for hair fall, and PRP won't fix them."),
            dict(emoji="⚠️", tag="Question 6", h="Any warning signs?", l1="Ask yourself", p1="Irregular periods, acne or extra facial hair? Feeling tired or cold, or weight changes? An itchy, scaly or painful scalp?", l2="Why it matters", p2="These can point to hormones, thyroid or a scalp condition that needs its own treatment."),
        ])),
        ("WHO PRP SUITS", ("dosdonts", (
            "Usually a good fit",
            ["Early pattern hair loss", "Hair that's getting thinner, not gone", "Alongside medicines your doctor prescribes", "Ready for a course of several sessions"],
            "Usually not the answer",
            ["Completely bald, shiny scalp", "Shedding from an untreated cause like thyroid or low iron", "Patchy hair loss (alopecia areata), unless your doctor advises it", "Expecting results after one session"],
        ))),
        ("", ("banner", ("PRP can't create new follicles where the scalp is fully bald.",
                         "It supports follicles that are still alive. That's why starting early, and finding the cause first, matters so much."))),
        ("BRING THIS TO YOUR CONSULTATION ⭐", ("checklist", [
            "My answers to the 6 questions",
            "Photos of my hair from a few months ago, if I have them",
            "Any recent blood test reports",
            "A list of medicines and supplements I take",
            "My questions about PRP and other treatments",
        ]), ("xlink", dict(href="guide-hairfall.html", emoji="🌳", h="Want to understand the hair cycle?", p="Read my guide on why hair falls and what's normal.", go="Read the Hair Fall Guide"))),
    ],
)
