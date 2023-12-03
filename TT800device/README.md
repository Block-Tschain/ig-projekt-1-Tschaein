# TT800 Device Module

## Python for Device

This Python script 'TT800run.py' is the implementation for the Tension Terminator OfficePro running on a device, which is connected with the OAK-D camera. It leverages DepthAI SDK for spatial detection and operates with an EasyGUI interface on compatible devices. The script is structured to provide a comprehensive solution for exercise monitoring and data collection. 

![cumulative object counting](..\docufiles\screenshot_tt800run.png.PNG)

Below is a detailed breakdown of its functionalities:

1. **Library Import and Global Variable Initialization**: 
   - The script begins by importing necessary libraries such as `os`, `sys`, `json`, `cv2`, `numpy`, `pathlib.Path`, and various DepthAI SDK components.
   - Global variables are defined to store exercise data and state information, including exercise type, duration, area, and various counters and flags.

2. **File Naming and JSON Structure Adjustment**:
   - A timestamp is generated to name output files in a structured manner, ensuring data consistency and ease of retrieval.
   - The script addresses a specific bug in YOLO8 model's JSON structure, where classes are incorrectly named, and provides a correct format for labeling.

3. **Model Selection and Command-Line Argument Handling**:
   - The script defaults to a 'slow' mode using Yolo5m and can switch to a 'fast' mode with Yolo8s based on command-line arguments, impacting object detection rate and processing speed.

4. **Label Loading and Data Appending Functions**:
   - `load_labels` function reads label information from the specified JSON model file.
   - `append_to_json_file` function appends new data entries to a JSON file, ensuring all exercise data is recorded and stored systematically.

5. **Neural Network Data Decoding and Screen Clearing Functions**:
   - The `decode` function processes NN data to extract detection results, including class, confidence, and coordinates.
   - `clear_screen` provides a clean visual slate for EasyGUI by clearing the terminal screen based on the operating system.

6. **Main Callback Function (`cb`) for Processing Detection Packets**:
   - This function is the core of the script, handling real-time data from the DepthAI camera and processing it for exercise monitoring.
   - It updates various counters and flags based on detection data and time intervals, tracking head movements and exercise areas.
   - The script dynamically updates exercise status, including type, duration, and spatial coordinates of detected objects.
   - Visual feedback is provided through the OpenCV interface, drawing rectangles and text on the camera frame to indicate detected areas and exercise data.
   - The function also ensures the exercise data is saved periodically and resets variables upon completion or interruption of an exercise.

7. **Camera and Neural Network Initialization with DepthAI SDK**:
   - The script initializes the OakCamera and sets up the color camera and neural network for YOLO object detection.
   - It employs a callback mechanism (`cb`) to process data from the neural network output and provides visual feedback.

8. **Camera Execution and Display**:
   - The script starts the camera in blocking mode, meaning it will continuously capture and process video frames until manually stopped.
   - Visual output is displayed using OpenCV, with options for resizing the frame for better visibility.