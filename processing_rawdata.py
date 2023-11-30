import json

json_file = open('../videos/results.json')
rawData = json.load(json_file)

postProcessingDate = str(rawData["day"])
amountVideos = int(rawData["num_videos"])
totalDuration = float(rawData["sum_durations"])
meanDuration = float(rawData["mean_duration"])
maxDuration = float(rawData["max_duration"])
minDuration = float(rawData["min_duration"])

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


exercisesCounter = 0
totalExercisesDuration = 0
meanExercisesDuration = 0
maxDurationExercise = maxDuration
minDurationExercise = maxDuration
triggerExercisesCounter = 0
duoBallExercisesCounter = 0
triggerExercises = []
duoBallsExercises = []

## not yet implentable due to missing individual-person detection
## total amount of individuals performing exercises
## duration of a single individual performing exercises
## duration of all exercises performed by individual
## total amount of exercises performed by individual
## duration of session per individual

totalTriggerDuration = 0
minTriggerDuration = maxDuration
maxTriggerDuration = 0
meanTriggerDuration = 0

totalDuoBallsDuration = 0
minDuoBallsDuration = maxDuration
maxDuoBallsDuration = 0
meanDuoBallsDuration = 0

## This is where the evaluation 'magic' happens for all Videos ;)
for video in videos:
    videoDetails = {"video":None, "hasTrigger":None, "hasDuoballs":None,"hasPerson":None, "total_frames":None, "trigger_ratio":None, "duoballs_ratio":None, "head_ratio":None, "duration":None}
    videoDetailsReduced = {"video":None, "duration":None}
    videoDetails['video'] = video['video']
    videoDetailsReduced['video'] = video['video']
    videoDetails['hasTrigger'] = video['hasTrigger']
    videoDetails['hasDuoballs'] = video['hasDuoballs']
    videoDetails['hasPerson'] = video['hasPerson']
    videoDetails['total_frames'] = video['total_frames']
    videoDetails['trigger_ratio'] = video['trigger_ratio']
    videoDetails['duoballs_ratio'] = video['duoballs_ratio']
    videoDetails['head_ratio'] = video['head_ratio']
    videoDetails['duration'] = video['duration']
    videoDetailsReduced['duration'] = video['duration']

    ## Check if Person was detected and disregard videos shorter than 5 seconds
    if videoDetails['hasPerson'] is True and float(videoDetails['duration']) > 5:
        exercisesCounter += 1
        totalExercisesDuration += float(videoDetails['duration'])
        
        ## Check for Minimum Duration of all Videos
        if float(videoDetails['duration']) < minDurationExercise:
            minDurationExercise = float(videoDetails['duration'])
        
        ## Check for Trigger Exercise and run all relevant evaluations
        if videoDetails['hasTrigger'] is True:
            triggerExercisesCounter += 1
            totalTriggerDuration += float(videoDetails['duration'])
            triggerExercises.append(videoDetailsReduced)
            if float(videoDetails['duration']) < minTriggerDuration:
                minTriggerDuration = float(videoDetails['duration'])
            if float(videoDetails['duration']) > maxTriggerDuration:
                maxTriggerDuration = float(videoDetails['duration'])

        ## Check for DuoBall Exercise and run all relevant evaluations
        if videoDetails['hasDuoballs'] is True and videoDetails['hasTrigger'] is False:
            duoBallExercisesCounter += 1
            totalDuoBallsDuration += float(videoDetails['duration'])
            duoBallsExercises.append(videoDetailsReduced)
            if float(videoDetails['duration']) < minDuoBallsDuration:
                minDuoBallsDuration = float(videoDetails['duration'])
            if float(videoDetails['duration']) > maxDuoBallsDuration:
                maxDuoBallsDuration = float(videoDetails['duration'])

## General Data evaluation (no 'for' Loop needed)
if exercisesCounter > 0:
    meanExercisesDuration = float(totalExercisesDuration / exercisesCounter)
else:
    meanExercisesDuration = 0

if triggerExercisesCounter > 0:
    meanTriggerDuration = float(totalTriggerDuration / triggerExercisesCounter)
else:
    meanTriggerDuration = 0

if duoBallExercisesCounter > 0:
    meanDuoBallsDuration = float(totalDuoBallsDuration / duoBallExercisesCounter)
else:
    meanDuoBallsDuration = 0

## Serialize statistics and write to JSON File
exercise_statistics = {
    "General-Exercise-Statistics": {
        "Processing-Date": postProcessingDate,
        "Total-Exercises-Performed": exercisesCounter,
        "Exercises-Total-Duration": totalExercisesDuration,
        "Exercises-Shortest-Duration": minDurationExercise,
        "Exercises-Longest-Duration": maxDurationExercise,
        "Exercises-Mean-Duration": meanExercisesDuration
    },
    "Trigger-Exercise-Statistics": {
        "Total-Trigger-Exercises-Performed": triggerExercisesCounter,
        "Trigger-Exercises-Total-Duration": totalTriggerDuration,
        "Trigger-Exercises-Shortest-Duration": minTriggerDuration,
        "Trigger-Exercises-Longest-Duration": maxTriggerDuration,
        "Trigger-Exercises-Mean-Duration": meanTriggerDuration,
        "List-Of-Trigger-Exercises": triggerExercises
    },
    "DuoBalls-Exercise-Statistics": {
        "Total-DuoBalls-Exerxices-Performed": duoBallExercisesCounter,
        "DuoBalls-Exercises-Total-Duration": totalDuoBallsDuration,
        "DuoBalls-Exercises-Shortest-Duration": minDuoBallsDuration,
        "DuoBalls-Exercises-Longest-Duration": maxDuoBallsDuration,
        "DuoBalls-Exercises-Mean-Duration": meanDuoBallsDuration,
        "List-Of-DuoBalls-Exercises": duoBallsExercises
    }
}

json_object = json.dumps(exercise_statistics, indent=4)

with open("../videos/statistics.json", "w") as outfile:
    outfile.write(json_object)