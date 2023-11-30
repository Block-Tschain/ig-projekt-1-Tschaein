
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
    
    if stride > 0:
        evaluated_frames = length/stride
    else:
        evaluated_frames = 0
    
    # Get trigger frames
    if evaluated_frames > 0:
        trigger_frames = df[(df["video"] == video) & (df["class"] == "Triggerpointlever") & (df["confidence"] > 0.65)].count()["video"]
        trigger_ratio = trigger_frames/evaluated_frames
        
        # Getting Confidence Levels
        total_trigger_frames = df[(df["video"] == video) & (df["class"] == "Triggerpointlever")].count()["video"]
        total_trigger_confidence = df[(df["video"] == video) & (df["class"] == "Triggerpointlever")].sum()["confidence"]
        if total_trigger_frames > 0:
            mean_trigger_confidence = (total_trigger_confidence/total_trigger_frames) * 100
        else:
            mean_trigger_confidence = 0

        duoballs_frames = df[(df["video"] == video) & (df["class"] == "Duoballs") & (df["confidence"] > 0.65)].count()["video"]
        duoballs_ratio = duoballs_frames/evaluated_frames

        # Getting Confidence Levels
        total_duoballs_frames = df[(df["video"] == video) & (df["class"] == "Duoballs")].count()["video"]
        total_duoballs_confidence = df[(df["video"] == video) & (df["class"] == "Duoballs")].sum()["confidence"]
        if total_duoballs_frames > 0:
            mean_duoballs_confidence = (total_duoballs_confidence/total_duoballs_frames) * 100
        else:
            mean_duoballs_confidence = 0

        head_frames = df[(df["video"] == video) & (df["class"] == "Head") & (df["confidence"] > 0.65)].count()["video"]
        head_ratio = head_frames/evaluated_frames

        # Getting Confidence Levels
        total_head_frames = df[(df["video"] == video) & (df["class"] == "Head")].count()["video"]
        total_head_confidence = df[(df["video"] == video) & (df["class"] == "Head")].sum()["confidence"]
        if total_head_frames > 0:
            mean_head_confidence = (total_head_confidence/total_head_frames) * 100
        else:
            mean_head_confidence = 0

    else:
        trigger_ratio = 0
        duoballs_ratio = 0
        head_ratio = 0
    

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
        "evaluated_frames": evaluated_frames,
        "trigger_ratio": float(trigger_ratio),
        "mean_trigger_confidence": int(mean_trigger_confidence),
        "duoballs_ratio": float(duoballs_ratio),
        "mean_duoballs_confidence": int(mean_duoballs_confidence),
        "head_ratio": float(head_ratio),
        "mean_head_confidence": int(mean_head_confidence),
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
    