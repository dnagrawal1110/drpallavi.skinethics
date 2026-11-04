GUIDE = dict(
    slug="scar-types", trigger="SCAR", emoji="🔍",
    title="Acne Scar Types Guide",
    pill="YOUR ACNE SCAR TYPES GUIDE",
    h1="Know Your Scar.", h1_em="Then Treat It.",
    subline="Ice pick, boxcar, rolling and raised scars: how to recognise each type and the treatments used for it.",
    intro=[
        "In the video, I explained why creams can't fill acne scars: the damage is under the surface, in the collagen.",
        "Every scar type needs a different approach. Use this guide to recognise yours, ideally in side lighting, and bring your notes to your consultation.",
    ],
    quote="Every scar type has a different treatment. Knowing yours is the first step.",
    tagline="Get your scars assessed and a plan made for your skin",
    sections=[
        ("HOW TO CHECK YOUR SCARS", ("card", dict(p=["Stand near a window or use your phone torch from the side. Side lighting shows the depth and edges of scars far better than light from the front. Take photos so you can compare later."]))),
        ("THE MAIN SCAR TYPES", ("concerns", [
            dict(emoji="📍", tag="Type 01", h="Ice Pick Scars", l1="What they look like", p1="Narrow, deep pits, like the skin was pricked with a sharp tool. Small on the surface but deep underneath.", l2="Commonly treated with", p2="TCA CROSS, where a strong acid is applied carefully inside each scar to build collagen. Sometimes punch techniques."),
            dict(emoji="⬜", tag="Type 02", h="Boxcar Scars", l1="What they look like", p1="Round or oval dips with sharp, steep edges, a bit like chickenpox marks. Can be shallow or deep.", l2="Commonly treated with", p2="CO2 fractional laser, MNRF, and TCA CROSS for deeper ones."),
            dict(emoji="🌊", tag="Type 03", h="Rolling Scars", l1="What they look like", p1="Wide, soft dips with sloping edges that make the skin look wavy and uneven. They show most in side light.", l2="Commonly treated with", p2="Subcision, which releases the bands pulling the skin down, often combined with MNRF or CO2 laser."),
            dict(emoji="⛰️", tag="Type 04", h="Raised Scars", l1="What they look like", p1="Firm, raised bumps (hypertrophic scars or keloids), more common on the jawline, chest and back.", l2="Commonly treated with", p2="Steroid injections, silicone gels and some lasers. These are treated very differently from pitted scars."),
        ])),
        ("NOT A SCAR? MARKS VS SCARS", ("table", [
            ("Red or brown marks", "Flat marks left after a pimple heals. They usually fade with time, sunscreen and treatment"),
            ("True scars", "A change in skin texture, either a dip or a bump. They need procedures to remodel"),
        ])),
        ("TREATMENT MAP", ("table", [
            ("CO2 fractional laser", "Boxcar and mixed scars. Has downtime"),
            ("MNRF", "Boxcar, rolling and mixed scars. Lower pigmentation risk"),
            ("Subcision", "Rolling scars that are tethered down"),
            ("TCA CROSS", "Ice pick and deep, narrow boxcar scars"),
        ]), ("intro", "Most people have a mix of types, so a combination plan usually works best.")),
        ("", ("banner", ("Scars don't fill in one session.", "The realistic goal is significant improvement, not perfect skin. And active acne needs to be controlled first."))),
        ("BEFORE YOUR CONSULTATION ⭐", ("checklist", [
            "I've checked my scars in side lighting",
            "I've noted which types I think I have",
            "My active acne is under control, or I'll ask about it",
            "I'm ready for multiple sessions",
            "I'll use sunscreen strictly before and after treatment",
        ]), ("xlink", dict(href="guide-mnrf.html", emoji="🪡", h="MNRF, CO2 or microneedling?", p="Compare downtime, sessions and which skin each one suits.", go="Read the Scar Treatments Guide"))),
    ],
)
