"""ParkiCup - an assistive cup holder for people living with Parkinson's disease.

Multi-page Streamlit site: Home, The Problem, Our Mission, The Design, About the Designer.
"""

from pathlib import Path

import streamlit as st

ASSETS = Path(__file__).parent / "assets"

BRAND_BLUE = "#0F0FE0"

st.set_page_config(
    page_title="ParkiCup",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap');

      .pc-hero {{
        text-align: center;
        padding: 3.5rem 1rem 2.5rem 1rem;
      }}
      .pc-hero h1 {{
        font-family: 'Libre Baskerville', Georgia, 'Times New Roman', serif;
        font-weight: 400;
        font-size: clamp(2.2rem, 6vw, 4.6rem);
        line-height: 1.1;
        color: {BRAND_BLUE};
        margin: 0 0 2rem 0;
      }}
      .pc-serif, .stMarkdown h1.pc-serif, .stMarkdown h2.pc-serif {{
        font-family: 'Libre Baskerville', Georgia, 'Times New Roman', serif !important;
        font-weight: 400 !important;
        color: {BRAND_BLUE} !important;
        font-size: 2rem;
        padding: 0;
        margin: 0.2rem 0 0.8rem 0;
      }}
      .pc-body {{
        color: {BRAND_BLUE};
        font-size: 1.05rem;
        line-height: 1.7;
      }}
      .pc-label {{
        display: inline-block;
        background: {BRAND_BLUE};
        color: white;
        font-weight: 600;
        letter-spacing: 0.04em;
        padding: 0.45rem 1.4rem;
        margin-bottom: 1.2rem;
      }}
      .pc-ticker {{
        border-top: 1px solid {BRAND_BLUE};
        border-bottom: 1px solid {BRAND_BLUE};
        overflow: hidden;
        white-space: nowrap;
        padding: 0.6rem 0;
        margin: 1rem 0 2rem 0;
      }}
      .pc-ticker span {{
        display: inline-block;
        font-family: 'Libre Baskerville', Georgia, serif;
        color: {BRAND_BLUE};
        font-size: 1.3rem;
        padding-left: 100%;
        animation: pc-scroll 28s linear infinite;
      }}
      @keyframes pc-scroll {{
        from {{ transform: translateX(0); }}
        to   {{ transform: translateX(-100%); }}
      }}
      .pc-step {{
        background: #EEF1FB;
        border-radius: 12px;
        padding: 1rem 1rem 1.2rem 1rem;
        text-align: center;
        height: 100%;
      }}
      .pc-step .num {{
        display: inline-block;
        width: 2.2rem; height: 2.2rem; line-height: 2.2rem;
        border-radius: 50%;
        background: #3F7FD6;
        color: white;
        font-weight: 700;
        margin-bottom: 0.5rem;
      }}
      .pc-step .title {{
        font-weight: 700;
        color: #12233F;
        margin-bottom: 0.4rem;
      }}
      .pc-step .desc {{
        color: #3B4A66;
        font-size: 0.92rem;
        line-height: 1.5;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)


def serif(text: str) -> None:
    st.markdown(f'<h2 class="pc-serif">{text}</h2>', unsafe_allow_html=True)


def body(text: str) -> None:
    st.markdown(f'<div class="pc-body">{text}</div>', unsafe_allow_html=True)


def label(text: str) -> None:
    st.markdown(f'<span class="pc-label">{text}</span>', unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Pages
# --------------------------------------------------------------------------- #
def home() -> None:
    st.markdown(
        """
        <div class="pc-hero">
          <h1>ParkiCup: A Steadier Sip.<br>Greater Independence</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    _, mid, _ = st.columns([2, 1, 2])
    with mid:
        if st.button("Discover Our Mission", use_container_width=True):
            st.switch_page(mission_page)

    ticker = " &bull; ".join(["Stability", "Comfort", "Independence", "Accessibility"])
    st.markdown(
        f'<div class="pc-ticker"><span>{ticker} &nbsp;&nbsp;&#9711;&nbsp;&nbsp; {ticker} '
        f'&nbsp;&nbsp;&#9711;&nbsp;&nbsp; {ticker}</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown("")
    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        st.image(ASSETS / "problem_cup.jpg", use_container_width=True)
        serif("The Problem")
        body(
            "Tremors, stiffness and reduced grip strength can turn a simple sip "
            "into a frustrating, spill-prone task."
        )
        st.page_link(problem_page, label="Read more →")
    with c2:
        st.image(ASSETS / "design_process.jpg", use_container_width=True)
        serif("The Design")
        body(
            "A larger, more comfortable grip, added stability and a foldable-straw "
            "attachment, taken from CAD model to 3D-printed prototype."
        )
        st.page_link(design_page, label="See the process →")
    with c3:
        st.image(ASSETS / "mission_vision.jpg", use_container_width=True)
        serif("Our Mission")
        body(
            "Make everyday drinking safer, more comfortable and more independent "
            "for people living with Parkinson's disease."
        )
        st.page_link(mission_page, label="Our mission →")


def problem() -> None:
    label("The Problem")
    left, right = st.columns([1, 1.4], gap="large")
    with left:
        st.image(ASSETS / "problem_cup.jpg", use_container_width=True)
    with right:
        st.markdown("#### What we are solving")
        body(
            "For many people, drinking from a cup is a simple everyday activity.<br>"
            "However, for someone living with Parkinson's disease, symptoms such as hand "
            "tremors, muscle stiffness, slow movement, and reduced grip strength can make "
            "this task much more challenging."
        )
        st.markdown("")
        body(
            "A standard cup may be difficult to hold securely, especially when the handle "
            "is small or uncomfortable. Tremors can cause the cup to shake, increasing the "
            "risk of spills. Some users may also find it difficult to lift or tilt the cup "
            "toward their mouth, which can reduce confidence and make them rely on support "
            "from others. These difficulties may affect more than convenience."
        )
        st.markdown("")
        body(
            "They can make people feel frustrated, self-conscious, or less independent "
            "during daily routines.<br>"
            "ParkiCup was created in response to this problem. It is an assistive cup "
            "holder designed to provide a larger, more comfortable grip, improve stability, "
            "and offer an easier drinking option through a foldable-straw attachment."
        )


def mission() -> None:
    label("Our Mission")
    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        st.image(ASSETS / "mission_walker.jpg", use_container_width=True)
        serif("Our Mission")
        body(
            "At ParkiCup, our mission is to make everyday drinking safer, more comfortable, "
            "and more independent for people living with Parkinson's disease.<br>"
            "Parkinson's can cause tremors, stiffness, reduced grip strength, and difficulty "
            "controlling movement.<br>"
            "These symptoms can make holding and using an ordinary cup challenging.<br>"
            "ParkiCup was created to respond to these difficulties through a simple, "
            "practical, and user-focused design."
        )
    with c2:
        serif("Our Goal")
        body(
            "Our goal is to develop an assistive cup holder that helps people with "
            "Parkinson's feel more confident and independent during everyday drinking. "
            "The design focuses on improving grip, stability, comfort, and ease of use "
            "while remaining simple, practical, and visually appealing."
        )
        st.markdown("")
        st.image(ASSETS / "mission_care.jpg", use_container_width=True)
    with c3:
        st.image(ASSETS / "mission_vision.jpg", use_container_width=True)
        serif("Our Vision")
        body(
            "We believe thoughtful design can improve small but meaningful moments in "
            "people's lives. ParkiCup aims to show how health, engineering, and empathy "
            "can come together to create solutions that support dignity and independence."
        )


DESIGN_STEPS = [
    ("CAD Modeling", "The holder, handle and straw mount are modelled in CAD with a larger, "
                     "easier-to-grip handle and a stable base."),
    ("Concept Development", "Renders are used to refine the shape, the ring that clips around "
                            "the cup, and how the foldable straw attaches."),
    ("3D Print Preparation", "Parts are laid out on the print bed and sliced for printing, "
                             "checking wall thickness and supports."),
    ("Prototype Assembly", "Printed rings, handle and straw arm are cleaned up and fitted "
                           "together around a standard cup."),
    ("Final Prototype", "The assembled ParkiCup is tested in the hand for grip, stability "
                        "and ease of drinking."),
]


def design() -> None:
    label("The Design")
    serif("Design Process")
    body("From concept to functional assistive device prototype.")
    st.markdown("")
    st.image(ASSETS / "design_process.jpg", use_container_width=True)
    st.markdown("")
    cols = st.columns(len(DESIGN_STEPS), gap="small")
    for i, (col, (title, desc)) in enumerate(zip(cols, DESIGN_STEPS), start=1):
        with col:
            st.markdown(
                f'<div class="pc-step"><div class="num">{i}</div>'
                f'<div class="title">{title}</div><div class="desc">{desc}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("")
    serif("Prototype 02")
    v1, v2 = st.columns([1, 1.4], gap="large")
    with v1:
        st.video(str(ASSETS / "prototype02.mp4"), autoplay=True, loop=True, muted=True)
    with v2:
        st.image(ASSETS / "prototype02.jpg", use_container_width=True)
        body(
            "The current build: navy print, a straight handle with a soft foam grip, "
            "a D-shaped yoke carrying two nested pivot rings, and a windowed cradle that "
            "takes an ordinary handleless cup. The cradle swings freely and finds level on its own."
        )

    st.markdown("")
    serif("Key features")
    f1, f2, f3 = st.columns(3, gap="large")
    with f1:
        st.markdown("**Soft full-hand grip**")
        body("A straight foam-wrapped handle held like a mug handle, for reduced grip strength and stiff fingers.")
    with f2:
        st.markdown("**Improved stability**")
        body("Two pivot rings form a gimbal so the cup hangs level while the hand shakes.")
    with f3:
        st.markdown("**Foldable straw attachment**")
        body("An easier drinking option that avoids lifting or tilting the cup.")


def about() -> None:
    label("About the Designer")
    with st.container():
        left, right = st.columns([1, 1.6], gap="large")
        with left:
            st.image(ASSETS / "designer.jpg", use_container_width=True)
        with right:
            st.markdown('<h1 class="pc-serif" style="font-size:3.4rem">Hello</h1>', unsafe_allow_html=True)
            body(
                "I am a student with a strong interest in health, design, and innovation. "
                "I created ParkiCup, an assistive cup holder designed to help people with "
                "Parkinson's drink with greater comfort, stability, and independence. This "
                "project was inspired by the idea that thoughtful design can make everyday "
                "tasks easier and improve quality of life in small but meaningful ways."
            )

    st.markdown("")
    with st.container(border=True):
        serif("My Story")
        body(
            "The idea for ParkiCup began with a simple question: how can design make everyday "
            "life easier for people living with Parkinson's? Many people with Parkinson's "
            "experience tremors, stiffness, and reduced grip strength, which can make drinking "
            "from a regular cup difficult and frustrating.<br>"
            "I wanted to create a solution that was practical, supportive, and easy to use. "
            "That led me to design ParkiCup, an assistive cup holder that improves grip and "
            "stability while also including a foldable straw attachment for easier drinking."
        )


# --------------------------------------------------------------------------- #
# Navigation
# --------------------------------------------------------------------------- #
home_page = st.Page(home, title="Home", icon="🏠", default=True)
problem_page = st.Page(problem, title="The Problem", icon="🫗", url_path="problem")
mission_page = st.Page(mission, title="Our Mission", icon="🎯", url_path="mission")
design_page = st.Page(design, title="The Design", icon="🛠️", url_path="design")
about_page = st.Page(about, title="About the Designer", icon="👋", url_path="about")

with st.sidebar:
    st.markdown(
        f'<div style="font-family:\'Libre Baskerville\',Georgia,serif;font-size:1.8rem;'
        f'color:{BRAND_BLUE};margin-bottom:0.5rem">ParkiCup</div>',
        unsafe_allow_html=True,
    )
    st.caption("A steadier sip. Greater independence.")

nav = st.navigation([home_page, problem_page, mission_page, design_page, about_page])
nav.run()

st.markdown("---")
st.caption("© ParkiCup · Stability · Comfort · Independence · Accessibility")
