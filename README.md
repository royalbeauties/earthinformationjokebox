# 🌍 Earth Jukebox with Agent Julie

An interactive web jukebox that turns NASA Earth Information Center (EIC) imagery into music for children aged 7–10. Kids pick a picture of our planet, and the app finds its city lights and turns them into melody, harmony, tempo, rhythm and timbre. Agent Julie, a cartoon astronaut, guides them through five music missions.

Built for the NASA Space Apps "Earth Jukebox" challenge: *generate dynamic sonifications from NASA's EIC visual frames.*

## Use of Super Intelligence (SI)

The **concept and design** of the Earth Jukebox (the idea, the five music missions, Agent Julie and the learning goals) were created by the **human team members**. The prototype itself (code, sound engine, text, guide website, screenshots and gameplay clips) was generated with SI tools, including Anthropic's Claude. The NASA pictures are real NASA data and were not made or changed by SI. See **[SI_DISCLOSURE.md](SI_DISCLOSURE.md)** for the full statement required by the NASA Space Apps Challenge.

## Guide website

A companion guide explaining the idea, how it answers the NASA Space Apps 2026 *Earth Information Jukebox* challenge, and how to play each mission (with screenshots and short silent gameplay clips) lives in [`guide/`](guide/index.html). On Vercel it is served at `/guide/` (`vercel.json` adds the trailing slash so the relative image and video paths resolve). Both the game and the guide are laid out for phones and tablets as well as desktops.

## Run it

Open `index.html` in a browser (Chrome, Edge, Firefox or Safari). Nothing else is needed: every picture is embedded in the file and every sound is synthesized live with the Web Audio API.

**Publish with GitHub Pages:** push this folder, then in the repository go to *Settings → Pages → Deploy from a branch*, choose `main` and `/ (root)`. The app will be live at `https://<your-user>.github.io/<repo>/`.

## The missions

| Mission | Music idea | What the child does |
|---|---|---|
| ⏳ Earth Time Machine | Tempo, melody, harmony | Hears night lights year by year, 2012 → 2023, for the World, India, Europe or the Nile. More light = more notes, faster tempo, more instruments. A scan line crosses the original EIC frame and each light flashes and sings as it is touched. |
| 🎵 Star Melody | Melody | The brightest light in each part of the picture is connected into a tune; kids can also tap lights to compose their own melody. |
| 🎶 Star Choir | Harmony | Lights stacked in the same column sing together. Compare "just melody" with "melody + harmony". |
| 🚀 Rocket Tempo | Tempo | A rocket flies across the picture; every circled light plays as the rocket passes. Speed ranges from turtle to rocket (50–180 BPM). |
| 🎛️ Music Sandbox | Melody, harmony, rhythm | A 16-step sequencer over any picture, with 8 note rows, kick and clap, and "make music from the picture". |

Every mission has:
- an **instrument picker** (timbre): trumpet, guitar, piano, saxophone, bells, violin and space synth, or 🎨 *picture colours*, where each light's colour picks its instrument;
- a **💡 Lights slider**: start with only the brightest lights circled and slide right to add dimmer ones (up to 150);
- a **3-question quiz** that earns a 🏅 medal. Questions cover music concepts, listening, and data measured from the pictures (for example "Which year had the most night light?").

Tapping a music word (Melody, Harmony, Tempo, Rhythm, Timbre) opens a short explanation with a "Show me on the picture!" demo.

## How pictures become music

1. **Find the lights.** Each pixel's brightness is compared with its neighbourhood (local contrast). Touching bright pixels are grouped into clusters, and large merged glows are split into tiles. Clusters are ranked by total brightness, and the brightest (up to 150) become circles. For pictures without clear bright spots, a backup picks the brightest points spread across the image.
2. **Map data to sound.**

| What the picture shows | What you hear |
|---|---|
| Height of a light | Pitch: 48 white-key notes (C1–A7, no sharps or flats); a higher light never plays a lower note |
| Brightness and size of a light cluster | Volume: bright clusters are louder, dim ones are softer |
| Lights in the same column | Notes played together (harmony, snapped to C, F, G or Am chords) |
| Colour of a light | Instrument (timbre), when 🎨 is selected |
| Total night light in a year's frame | Number of notes, tempo and extra instrument layers (Time Machine) |

3. **Measured results** (computed in the browser from the EIC frames). Total night light compared with 2012: World +64%, India +125%, Nile region +28%, Western Europe about the same (−7%), with a small dip in 2020.

## Rebuild after editing

The app is generated from `src/template.html` and the images in `assets/`:

```bash
python3 src/build.py      # writes index.html (needs only Python 3)
```

- `src/template.html`: all HTML, CSS and JavaScript (missions, audio engine, quizzes, Agent Julie)
- `src/build.py`: picture titles, facts and credits; embeds the images into `index.html`
- `assets/eic/`: EIC night-lights frames (world map 2012–2023, change maps) and `years_closeups/` (India, Europe and Nile for each year)
- `assets/pics/`: the Earth-from-the-ISS photo and the bonus space pictures

## Credits

- Night-lights frames: NASA Earth Information Center (EIC) visualization, 2012–2023
- Earth from the International Space Station: NASA / ISS crew
- Cartwheel Galaxy: NASA, ESA, CSA, STScI (James Webb Space Telescope)
- The Sun and Solar Flare: NASA Solar Dynamics Observatory
- Cassiopeia A: NASA telescopes (Chandra and others)
- Songs and sounds: synthesized in the browser; no audio files are used
- Font: Fredoka (Google Fonts)

Agent Julie is an original cartoon character named in honour of Canadian astronaut Julie Payette; she is not a likeness of a real person.
