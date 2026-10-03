# F1 Pitwall: Telemetry Replay and Dashboard

A Python project that analyzes real Formula 1 telemetry and (in progress)
replays it as a live pit-wall dashboard.

## Features (so far)
- Load race sessions with FastF1
- Plot speed, throttle, brake and gear for any driver's fastest lap

## Setup
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
mkdir cache
python day1_lap_plot.py
```

## Roadmap
- [x] Day 1: single-lap telemetry plot
- [ ] Driver comparison and time delta
- [ ] Tyre degradation model
- [ ] Live replay engine
- [ ] Streamlit dashboard with alerts