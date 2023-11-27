# ig-projekt-1-Tschaein

## Prerequisites
1. Python 3.11
2. Git (optional)

### 1. Python
We recommend using Python Version 3.11 to run our application. Our program does not support the newest Version 3.12.

#### Windows
Pythons installer for Windows can be found here -> https://www.python.org/downloads/windows/

#### macOS
Pythons installer for macOS can be found here -> https://www.python.org/downloads/macos/

#### Linux/UNIX
Pythons source-code for Linux/UNIX can be found here -> https://www.python.org/downloads/source/

#### Others
Pythons source-code for other OS can be found here -> https://www.python.org/download/other/

#### PATH Variable
If the installer didn't prompt you, please make sure to add the python installation path ``` [installationPath]\python311\ ``` and Scripts path ``` [installationPath]\python311\Scripts ``` to your PATH Variable

Please ensure you have the correct version of Python installed by running the following command in your terminal
```
python --version
```

### 2. Git (optional)

#### Windows
Gits installer for Windows can be found here -> https://git-scm.com/download/win

#### macOS
Gits installer for macOS can be found here -> https://git-scm.com/download/mac

#### Source-Code
Gits source-code for can be found here -> https://github.com/git/git

#### PATH Variable
Please make sure to also add Gits installation path to your PATH Variable


## How to detect Trigger Exercises?
Put the videos you want to classify inside the videos folder, then call `trigger_detection.sh`. Right now it will output whether the exercises user the trigger or not right there in terminal.

## how can I fine-tune a YOLO Model to detect custom classes (e.g. different people)?

This is documented in the `Yolo_fine_tune.ipynb` Jupyter Notebook. There's a Link at the top which has the neccessary information