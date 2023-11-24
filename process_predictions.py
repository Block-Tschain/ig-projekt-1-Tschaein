
import os, glob, cv2, json
import pandas as pd
# Find latest run
latest_run = (max(glob.glob(os.path.join("runs/detect", '*/')), key=os.path.getmtime))

prediction = os.path.join(latest_run, "predictions.csv")

df = pd.read_csv(prediction,header=None)
df.columns = ["video", "class", "confidence"]

# iterate over every video
for video in df["video"].unique():
    istrigger = False
    # Get total frames
    cap = cv2.VideoCapture("../videos/"+video)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = float(length)/fps
    total_frames = length/24
    # Get trigger frames
    trigger_frames = df[df["video"]==video].count()["video"]
    ratio = trigger_frames/total_frames

    # If more than half of the frames we looked at had a trigger, then it's a trigger exercise
    if ratio > 0.5:
        print("Video: {} is trigger exercise".format(video))
        istrigger = True
    else:
        print("Video: {} is not trigger exercise".format(video))
    video_data = {
        "video": video,
        "isTrigger": istrigger,
        "total_frames": fps,
        "ratio": float(ratio),
        "duration": duration
    }
    #print(type(video), type(istrigger), type(total_frames), type(trigger_frames), type(ratio), type(duration))
    # Serializing json
    json_object = json.dumps(video_data, indent=4)
 
    # Writing to sample.json
    with open("../videos/"+video+".json", "w") as outfile:
        outfile.write(json_object)
    