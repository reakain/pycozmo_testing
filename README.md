# PyCozmo Expression Animation Testing

This serves as a quick test of the PyCozmo expression and animation capabilities.

### Faces
- Requires disabling standard procedural faces
- Full list just pulled form pycozmo examples

### Animations
- Base animations from flat stack. Looks like there are complete animations, and then components of those complete animations.
- The names don't seem to line up with the names from the cozmo SDK. So answer hazy which animations are which

### Need to test
- ability to interrupt animations
- Event handling of animation events
- ability to make compound animations

## Environment Setup
This application uses python 3, and these instructions assume python3 is set as your default python command. You can check your version with ```python --version```

- *Note:* If your python 3 is called with ```python3``` then you use that for all python command instances, and your pip commands will be ```pip3```

#### Virtual Environment
1. In bash (or git bash on Windows) navigate to this respository folder, then create your virtual environment with ```python -m venv ./venv```
2. Once complete activate your environment with ```source ./venv/Scripts/activate```
3. Install the requirements once activated with ```pip install -r requirements.txt```
4. If you install any additional libraries, update the requirements with ```pip freeze > requirements.txt```
5. Exit the virtual environment with ```deactivate```

## References
1. [PyCozmo](https://github.com/zayfod/pycozmo)