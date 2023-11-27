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
If the installer didn't prompt you, please make sure to add the python installation path ```[installationPath]\python311``` and Scripts path ```[installationPath]\python311\Scripts``` to your PATH Variable

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
Please make sure to also add Gits installation path ```[installationPath]\git``` to your PATH Variable

## Installation

If you have installed Git feel free to <a href="git-installed">skip</a> this next part, else please use the following link to download our Sourcecode from Github
	- https://github.com/Block-Tschain/ig-projekt-1-Tschaein/archive/refs/heads/main.zip

Navigate to the downloaded file and unpack it
```
tar -xf ig-projekt-1-Tschaein-main.zip
```
Then navigate to the unpacked folder

<a name="git-installed"></a>

### Git installed
Navigate to a Directory of your choice, then enter the following command in your terminal
```
git clone https://github.com/Block-Tschain/ig-projekt-1-Tschaein.git
```

## Add Videos for evaluation and Run the program
Add your videos to the videos folder located in the programs root directory.
Please make sure they are encoded in ...

Once that is done, navigate to the programs root directory once more and execute the ```trigger_detection.sh``` script.
This will automatically download and install the necessary remaining requirements and evaluate the videos once ready.
The raw data from the evaluation can be found in the results.json file inside the videos folder.
Further evaluation of this data can be found in \*.json in the root directory.

## How to detect Trigger Exercises?
Put the videos you want to classify inside the videos folder, then call `trigger_detection.sh`. Right now it will output whether the exercises user the trigger or not right there in terminal.

## how can I fine-tune a YOLO Model to detect custom classes (e.g. different people)?

This is documented in the `Yolo_fine_tune.ipynb` Jupyter Notebook. There's a Link at the top which has the neccessary information