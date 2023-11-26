
import os, glob, cv2, json, argparse,datetime
import pandas as pd
# Find latest run
latest_run = (max(glob.glob(os.path.join("runs/detect", '*/')), key=os.path.getmtime))
parser = argparse.ArgumentParser()
parser.add_argument('stride')
args = parser.parse_args()
stride = int(args.stride)
prediction = os.path.join(latest_run, "predictions.csv")

df = pd.read_csv(prediction,header=None)
df.columns = ["video", "class", "confidence"]
videos_data = []
total_duration = 0
# iterate over every video
for video in df["video"].unique():
    hasTrigger = False
    hasDuoballs = False
    hasPerson = False
    # Get total frames
    cap = cv2.VideoCapture("../videos/"+video)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = float(length)/fps
    total_duration += duration
    total_frames = length/stride
    # Get trigger frames
    trigger_frames = df[(df["video"]==video) & (df["class"] == "Triggerpointlever")].count()["video"]
    trigger_ratio = trigger_frames/total_frames

    duoballs_frames = df[(df["video"]==video) & (df["class"] == "Duoballs")].count()["video"]
    duoballs_ratio = duoballs_frames/total_frames

    head_frames = df[(df["video"]==video) & (df["class"] == "Head")].count()["video"]
    head_ratio = head_frames/total_frames

    # If more than half of the frames we looked at had a trigger, then it's a trigger exercise
    if trigger_ratio > 0.5:
        hasTrigger = True
    if duoballs_ratio > 0.5:
        hasDuoballs = True
    if head_ratio > 0.5:
        hasPerson = True
    
    video_data = {
        "video": video,
        "hasTrigger": hasTrigger,
        "hasDuoballs": hasDuoballs,
        "hasPerson": hasPerson,
        "total_frames": length,
        "trigger_ratio": float(trigger_ratio),
        "duoballs_ratio": float(duoballs_ratio),
        "head_ratio": float(head_ratio),
        "duration": duration
    }
    
    videos_data.append(video_data)
day_data = {
        "day": datetime.datetime.now().strftime("%Y-%m-%d"),
        "num_videos": len(videos_data),
        "sum_durations": total_duration,
        "mean_duration": total_duration/len(videos_data),
        "max_duration": max(videos_data, key=lambda x:x["duration"])["duration"],
        "min_duration": min(videos_data, key=lambda x:x["duration"])["duration"],
        "videos": videos_data

    }
# Serializing json
json_object = json.dumps(day_data, indent=4)

# Writing to sample.json
with open("../videos/results.json", "w") as outfile:
    outfile.write(json_object)
    