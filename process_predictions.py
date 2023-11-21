
import os, glob, cv2
import pandas as pd
# Find latest run
latest_run = (max(glob.glob(os.path.join("runs/detect", '*/')), key=os.path.getmtime))

prediction = os.path.join(latest_run, "predictions.csv")

df = pd.read_csv(prediction,header=None)
df.columns = ["video", "class", "confidence"]

# iterate over every video
for video in df["video"].unique():
    # Get total frames
    cap = cv2.VideoCapture("../videos/"+video)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    total_frames = length/24
    # Get trigger frames
    trigger_frames = df[df["video"]==video].count()["video"]
    ratio = trigger_frames/total_frames

    # If more than half of the frames we looked at had a trigger, then it's a trigger exercise
    if ratio > 0.5:
        print("Video: {} is trigger exercise".format(video))
    else:
        print("Video: {} is not trigger exercise".format(video))