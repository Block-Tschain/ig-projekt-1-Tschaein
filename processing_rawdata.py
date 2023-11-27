import json

json_file = open('videos/results.json')
rawData = json.load(json_file)

day = str(rawData["day"])
amountVideos = int(rawData["num_videos"])
totalDuration = int(rawData["sum_durations"])
meanDuration = int(rawData["mean_duration"])
maxDuration = int(rawData["max_duration"])
minDuration = int(rawData["min_duration"])

videos = []

for video in rawData["videos"]:
    videoDetails = {"video":None, "hasTrigger":None, "hasDuoballs":None,"hasPerson":None, "total_frames":None, "trigger_ratio":None, "duoballs_ratio":None, "head_ratio":None, "duration":None}
    videoDetails['video'] = video['video']
    videoDetails['hasTrigger'] = video['hasTrigger']
    videoDetails['hasDuoballs'] = video['hasDuoballs']
    videoDetails['hasPerson'] = video['hasPerson']
    videoDetails['total_frames'] = video['total_frames']
    videoDetails['trigger_ratio'] = video['trigger_ratio']
    videoDetails['duoballs_ratio'] = video['duoballs_ratio']
    videoDetails['head_ratio'] = video['head_ratio']
    videoDetails['duration'] = video['duration']
    videos.append(videoDetails)

## initial Test for JSON-Parsing
## print(videos)

exercisesCounter = 0
##if hasPerson is true && duration > 5

totalExercisesDuration = 0
##if counts_as_exercise

meanExercisesDuration = 0
##double(totalExercisesDuration / exercisesCounter)

maxDurationExercise = maxDuration

minDurationExercise = maxDuration
##if counts_as_exercise && duration < minDuration -> minDuration = duration

triggerExercisesCounter = 0
##if hasTrigger is true

duoBallExercisesCounter = 0
##if hasTrigger is false && hasPerson is true

triggerExercises = []
##duration of trigger exercises
##if is_trigger_exercise -> triggerExercises.append(duration)

duoBallsExercises = []
##duration of duoBalls exercises
# if is_duoBalls_exercise -> duoBallsExercises.append(duration)




## not yet implentable due to missing individual-person detection
## total amount of individuals performing exercises
## duration of a single individual performing exercises
## duration of all exercises performed by individual
## total amount of exercises performed by individual
## duration of session per individual




