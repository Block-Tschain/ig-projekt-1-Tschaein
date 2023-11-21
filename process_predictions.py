# Find latest
import os, glob, cv2
import pandas as pd
latest_run = (max(glob.glob(os.path.join("runs/detect", '*/')), key=os.path.getmtime))

prediction = os.path.join(latest_run, "predictions.csv")

df = pd.read_csv(prediction,header=None)
df.columns = ["video", "class", "confidence"]
#print(df.groupby("video").count())
#print(df.head())
for video in df["video"].unique():
    cap = cv2.VideoCapture("../videos/"+video)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    total_frames = length/30
    trigger_frames = df[df["video"]==video].count()["video"]
    ratio = trigger_frames/total_frames
    if ratio > 0.5:
        print("Video: {} is trigger exercise".format(video))
    else:
        print("Video: {} is not trigger exercise".format(video))
    #print(df[df["video"]==video].sort_values(by="confidence", ascending=False).head(5))
    #print(df[df["video"]==video].sort_values(by="confidence", ascending=False).tail(5))