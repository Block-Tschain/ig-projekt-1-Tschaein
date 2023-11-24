
import os, glob, cv2, json
import pandas as pd
# Find latest run
latest_run = (max(glob.glob(os.path.join("runs/detect", '*/')), key=os.path.getmtime))

prediction = os.path.join(latest_run, "predictions.csv")

df = pd.read_csv(prediction,header=None)
df.columns = ["video", "class", "confidence"]
videos_data = []
# iterate over every video
for video in df["video"].unique():
    istrigger = False
    # Get total frames
    cap = cv2.VideoCapture("../videos/"+video)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = float(length)/fps
    total_frames = length/23
    # Get trigger frames
    trigger_frames = df[df["video"]==video].count()["video"]
    ratio = trigger_frames/total_frames

    # If more than half of the frames we looked at had a trigger, then it's a trigger exercise
    if ratio > 0.5:
        istrigger = True
    video_data = {
        "video": video,
        "isTrigger": istrigger,
        "total_frames": length,
        "ratio": float(ratio),
        "duration": duration
    }
    videos_data.append(video_data)
# Serializing json
json_object = json.dumps(videos_data, indent=4)

# Writing to sample.json
with open("../videos/results.json", "w") as outfile:
    outfile.write(json_object)
    