# Hablar México

A beginner course in **spoken Mexican Spanish** for an adult English speaker. The aim is conversation you can use in Mexico: greetings, ordering food, asking prices, finding your way, meeting people, and being a guest. It is not a translation-drill app, and it is not a course in the Spanish of Spain.

This repository is the first stretch of the beginner level: the method and Units 1–9. Later units are not in this tree yet.

## How to study

Open `docs/index.html` in a browser, or serve the `docs/` folder locally. Each unit teaches first, then gives a model conversation you can listen to, a list of reusable chunks, pronunciation notes, shadowing, a role-play with your lines left blank, and a short check that mirrors the unit. Print the one-page review sheet after you finish.

The Listen button reads explanations in English and model conversations in Spanish. It prefers a Mexican voice (`es-MX`) when the browser has one, and falls back to another Spanish voice. Hear buttons play individual chunks. There is no account, and nothing is sent to a server.

## Building

```
pip install -r requirements.txt
python3 build.py         # writes docs/
python3 check_links.py   # every internal link and anchor
python3 render_pdfs.py   # Letter-size PDFs of the review sheets
```

`docs/` is committed, so the site can be opened without a build step.

## Mexican Spanish in this course

- Plural *you* is *ustedes*, never *vosotros*.
- *Tú* and *usted* are both taught, with guidance on when each is the safer choice.
- High-frequency Mexican expressions are included only when a reputable source records them, and they are labeled informal when they are informal.

See [SOURCES.md](SOURCES.md) for the dictionaries behind those choices.
