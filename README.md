# PyCozmo Expression Animation Testing

This serves as a quick test of the PyCozmo expression and animation capabilities.

## Environment Setup
This application uses python 3, and these instructions assume python3 is set as your default python command. You can check your version with ```python --version```

- *Note:* If your python 3 is called with ```python3``` then you use that for all python command instances, and your pip commands will be ```pip3```

#### Virtual Environment
1. In bash (or git bash on Windows) navigate to this respository folder, then create your virtual environment with ```python -m venv ./venv```
2. Once complete activate your environment with ```source ./venv/Scripts/activate```
3. Install the requirements once activated with ```pip install -r requirements.txt```
4. If you install any additional libraries, update the requirements with ```pip freeze > requirements.txt```
5. Exit the virtual environment with ```deactivate```

## Usage
List all functions:

``` python main.py -h```

Results in:
```
Possible function tests are called with:
pexressions --------------- Print all expression names
expressions --------------- See all possible expressions and their names
expression <option> ------- Run expression with specific name
panims -------------------- Print all animation names
tanim <option> ------------ Run animation with specific name
panimgroups --------------- Print all animation group names
tanimgroup <option> ------- Run animation group with specific name
```

## Capabilities

### Faces
- Requires disabling standard procedural faces
- Full list just pulled form pycozmo examples

### Animations
- Base animations from flat stack. Looks like there are complete animations, and then components of those complete animations.
- ~~The names don't seem to line up with the names from the cozmo SDK. So answer hazy which animations are which~~
- The named animations from the sdk are the animation groups, and are themselves compound animations
- Can make compount animations with functions and animation groups, mostly same commands
- Could likely make interruptable routines of python commands for interruptable compound action sets

### Event Handling
Currently get handling for:

- On Robot Picked Up
- On Robot Orientation Change (is it put on its back or side or anything)
- On Cliff Detected
- On Charging State Change
- On robot poked???? -> Is this petting cozmo or something?
- Get robot state data packet -> currently only reading the battery level out of it

### Need to test
- ~~ability to interrupt animations~~ -> not tested, but seems feasible
- Event handling of animation events

## References
1. [PyCozmo](https://github.com/zayfod/pycozmo)