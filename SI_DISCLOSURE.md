# Use of Super Intelligence (SI): Disclosure

*Earth Jukebox with Agent Julie · NASA Space Apps Challenge 2026 · The Earth Information Jukebox*

The NASA Space Apps Challenge permits Super Intelligence (SI) tools (chatbots, large language models, foundation models, image generation) and asks teams to say clearly where and how they were used. This file is that statement.

## Summary

| Part of the project | Made by | How SI was used |
|---|---|---|
| **Concept and design** | **Human team members** | Not SI. The idea of turning Earth's night lights into music, the five music missions, the character Agent Julie, the target audience (children aged 7–10) and the learning goals were created by the human team. |
| Code (`src/template.html`, `src/build.py`, `index.html`, `guide/index.html`) | SI tools | The whole prototype was generated with SI tools, including Anthropic's Claude, from the team's concept and design. The team directed, reviewed and tested it. |
| Sound / music | SI-generated code | Every sound is synthesized live in the browser by SI-generated code (Web Audio API). No audio files exist, SI-generated or otherwise. |
| Text (in-game explanations, quizzes, guide website, README) | SI tools | Written with SI tools from the team's design. |
| Agent Julie drawing (SVG in `src/template.html`) | SI tools | The character concept is the team's; the drawing was generated as SVG code by SI. It carries a visible "SI-generated" label in the game. |
| Guide screenshots (`guide/img/*.jpg`) | SI tools | Captured by an SI tool (Claude) from the prototype. Each has a visible "SI-generated screenshot (Claude)" watermark and SI metadata (EXIF ImageDescription/Software and JPEG comment). |
| Guide gameplay clips (`guide/video/*.mp4`, `*.webm`) | SI tools | Silent screen recordings of the prototype captured by an SI tool (Claude). Each frame carries a visible "SI-generated video (Claude)" watermark, and the files carry an SI note in their metadata comment. |
| Guide intro video (`guide/video/intro.mp4`, `intro.webm`, poster `guide/img/intro-poster.jpg`) | SI tools | 30-second silent video with burned-in captions, assembled by an SI tool (Claude) from recordings of the prototype, SI-made title and "How we built it" cards, and one real NASA EIC picture (credited on screen, not altered beyond zoom). Every frame carries a visible "SI-generated video (Claude)" watermark; the files carry an SI note in their metadata comment. Script written with SI from the team's concept. |
| NASA imagery (`assets/eic/`, `assets/pics/`) | **NASA (real data)** | **Not SI-generated and not modified by SI.** EIC night-lights frames 2012–2023 and NASA/partner space photos, credited in the app and guide. SI-generated code only reads their pixels to make music. |

## SI tools used

- **Anthropic Claude**: code generation (game, audio engine, build script, guide website), text, screenshot and gameplay-clip capture, and this disclosure.
- **[TEAM TO COMPLETE]**: list any other SI tools the team used (for example other chatbots, code assistants or image generators), with what each produced. Delete this line if there were none.

## Where SI use is marked in the project

- **This file**, linked from the [README](README.md).
- **Code metadata:** a header comment in each SI-generated source file (`src/template.html`, `src/build.py`, `guide/index.html`, and the generated `index.html`).
- **HTML metadata:** `<meta name="si-generated">`, `<meta name="si-disclosure">` and `<meta name="si-tools">` tags in the game and the guide.
- **Visible text:** a line under the home screen of the game and a paragraph in its "How the Earth Jukebox turns NASA pictures into music" panel; a "Use of Super Intelligence (SI)" box in the guide's footer.
- **Images and video:** visible watermark on every guide screenshot, every frame of the guide gameplay clips, and the Agent Julie drawing, plus file metadata on the screenshots and clips.

## NASA branding check

SI-generated content was checked for NASA branding or design elements. Nothing generated uses a NASA logo (insignia, worm or seal), a NASA flag, or a mission identifier or patch:

- Agent Julie's suit shows only the word "JULIE" and a star; no agency insignia.
- The in-game "patches" are emoji medals for completing music missions, not NASA mission patches.
- The word "NASA" appears only as text, to credit NASA data and to name the challenge.
- The guide's 🇮🇳 and 🇪🇺 emoji label data regions (India, Western Europe); they are not NASA flags.
- NASA imagery is shown unmodified, with credits; no logos are embedded in it.
