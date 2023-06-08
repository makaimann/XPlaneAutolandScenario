# XPlaneAutolandScenario
This is an autolanding scenario using the X-Plane simulator for the Grant County airport Runway 04.
The module is intended as a research tool for verification with learning-enabled components in the loop.


## Quickstart
Create a Python virtual environment using at least Python 3.7.
```
python3 -m venv ./env
```
Activate your environment and install the module (run from the top-level of this repository):
```
source ./env/bin/activate
pip install -e .
```

Launch X-Plane 11 and start a flight with a Cessna Skyhawk at Grant Co Airport (KMWH).
Run `run_autoland.py` from within the virtual environment.