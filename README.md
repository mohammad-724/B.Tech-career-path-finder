# B.Tech Career Path Finder

A professional multi-page career discovery website for B.Tech graduates, built with Python and Flask.

## Features

- Department selection for ECE, CSE, EEE and Mechanical Engineering
- Separate fresh page for every stage
- Career cards with objective, skills, tools and roadmap
- Browser Back button support
- On-page Back navigation
- Responsive layout
- Hover effects and page entrance transitions
- Light, modern visual design
- No database required for the first version

## Project structure

```text
BTech-Career-Path-Finder/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── branch.html
│   ├── careers.html
│   ├── career.html
│   └── 404.html
└── static/
    ├── style.css
    └── script.js
```

## Run

```bash
py -m pip install -r requirements.txt
py app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Navigation flow

Home → Department → Career Paths → Career Details

Each stage is a real Flask route, so the previous page disappears and the browser Back button works normally.
