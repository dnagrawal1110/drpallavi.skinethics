GUIDE = dict(
    slug="freeze", trigger="FREEZE", emoji="❄️",
    title="Cryolipolysis Candidate Checklist",
    pill="CRYOLIPOLYSIS CANDIDATE CHECKLIST",
    h1="Fat Freezing?", h1_em="Check If It's For You.",
    subline="The pinch test, which kind of fat responds, a realistic timeline, and when this treatment isn't for you.",
    intro=[
        "In the video, I explained that cryolipolysis is body contouring, not a weight-loss shortcut.",
        "It works best for a specific kind of person and a specific kind of fat. Use this checklist to see if you're likely to be a good candidate.",
    ],
    quote="Cryolipolysis is body contouring, not a shortcut to weight loss.",
    tagline="Find out if fat freezing suits your body",
    disclaimer="This checklist is a guide only. Suitability is decided by a doctor after an in-person evaluation.",
    sections=[
        ("STEP 1: THE PINCH TEST", ("card", dict(p=[
            "Gently pinch the area, like the lower belly or love handles, between your thumb and fingers.",
            "<strong>If you can hold a soft roll of fat</strong>, it's pinchable fat that sits under the skin. That's the kind cryolipolysis targets.",
            "<strong>If the belly feels firm and you can't pinch much</strong>, the fat may be deeper, around the organs. Cryolipolysis doesn't treat that.",
        ]))),
        ("STEP 2: WHICH FAT RESPONDS", ("dosdonts", (
            "Responds well",
            ["Pinchable lower belly fat", "Love handles", "Back or bra-line rolls", "Inner thighs or under the chin"],
            "Doesn't respond",
            ["Deep belly fat around the organs", "Overall weight gain", "Loose skin without much fat", "Cellulite on its own"],
        ))),
        ("STEP 3: ARE YOU CLOSE TO A HEALTHY WEIGHT?", ("card", dict(p=["Cryolipolysis works best for people who are at or near a healthy weight but have stubborn pockets that don't shift with diet and exercise. If your weight is well above a healthy range, a lifestyle and medical evaluation should come first. Your doctor may check your BMI as part of this."]))),
        ("WHO SHOULD NOT HAVE IT", ("signs", [
            "Pregnant or breastfeeding women",
            "People with cold-related conditions like cryoglobulinaemia or cold urticaria",
            "Anyone with a hernia in or near the area",
            "Anyone with an open wound, rash or skin problem at the area",
            "Anyone looking for weight loss rather than contouring",
        ])),
        ("A REALISTIC TIMELINE", ("timeline", [
            ("Day of treatment", "Cold and numb", "The area feels cold and numb. Redness, mild swelling or tenderness afterwards is common."),
            ("Weeks 1–3", "Body starts clearing", "Treated fat cells are slowly cleared by the body. Some numbness or tingling can last a few weeks."),
            ("Months 2–3", "Visible change", "Most people see the change now. Some areas need a second session.", "grow"),
        ])),
        ("", ("banner", ("Remaining fat cells can still grow.", "If diet and activity slip, the fat cells left behind can get bigger again. Results last best with a healthy lifestyle."))),
        ("YOUR CHECKLIST ⭐", ("checklist", [
            "The area passes the pinch test",
            "I'm at or near a healthy weight",
            "I've tried diet and exercise and this pocket won't shift",
            "None of the 'should not have it' points apply to me",
            "I'm happy to wait 2–3 months for results",
        ])),
    ],
)
