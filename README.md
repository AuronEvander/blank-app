# ☕ ParkiCup

A Streamlit site for **ParkiCup**, an assistive cup holder that helps people
living with Parkinson's disease drink with a steadier grip, more stability and
greater independence.

Pages:

- **Home**: hero, call to action and a short overview of each section.
- **The Problem**: why an ordinary cup is hard to use with tremors, stiffness and reduced grip strength.
- **Our Mission**: mission, goal and vision.
- **The Design**: the five-step design process from CAD model to final 3D-printed prototype, plus key features.
- **About the Designer**: introduction and the story behind the project.

Images live in `assets/` and the brand theme (blue on white) is set in `.streamlit/config.toml`.

## Premium website (`site/`)

`site/index.html` is a standalone, dependency-free website for ParkiCup:
an EN/TR bilingual landing page with a live canvas simulation of the gimbal
mechanism (hand tremor at 4–6 Hz vs. a self-levelling cradle), the original
prototype photographs, specs, the designer's story, a products roadmap and the
Instagram journal. It deploys to GitHub Pages with the workflow in `deploy/` (see `deploy/README.md`
for the one-time setup).

`site/media/real_demo.mp4` is the designer's own footage of prototype 02 (navy print,
foam grip, windowed cradle) and `site/assets/real_*.jpg` are frames from it. AI stills and
films (GPT Image 2.5, Kling 3.0, Genjutsu motion transfer from the real clip) are listed in
`site/media/manifest.json`; run `scripts/fetch_media.sh` to download them.

## Instagram content (`content/instagram/`)

- `calendar.md`: four-week plan, three series (Understand / Adapt / Making), hashtag set and rules.
- `posts.json`: the twelve posts with TR and EN captions and their image paths.
- `automation.md`: how the scheduled posting works once an Instagram Business account is connected.

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
