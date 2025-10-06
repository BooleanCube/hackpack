# hackpack

Hackpack with self-implemented algorithms and data structures stored for ICPC

Working on compiling a PDF with everything

## Setup Manim

```bash
sudo apt-get update
sudo apt-get install -y libcairo2-dev libpango1.0-dev ffmpeg texlive-full

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Compile Manim

```bash
manim -pqh -a visual/script.py --format gif
```
