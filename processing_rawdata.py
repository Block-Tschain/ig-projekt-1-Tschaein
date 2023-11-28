import json

json_file = open('videos/results.json')
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

## do we even need these?
totalTriggerDuration = 0
minTriggerDuration = maxDuration
maxTriggerDuration = 0
meanTriggerDuration = 0

totalDuoBallsDuration = 0
minDuoBallsDuration = maxDuration
maxDuoBallsDuration = 0
meanDuoBallsDuration = 0

## now to run the evaluation
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

    if videoDetails['hasPerson'] is True and float(videoDetails['duration']) > 5:
        exercisesCounter += 1
        totalExercisesDuration += float(videoDetails['duration'])
        
        if float(videoDetails['duration']) < minDurationExercise:
            minDurationExercise = float(videoDetails['duration'])
        
        if videoDetails['hasTrigger'] is True:
            triggerExercisesCounter += 1
            totalTriggerDuration += float(videoDetails['duration'])
            triggerExercises.append(videoDetailsReduced)
            if float(videoDetails['duration']) < minTriggerDuration:
                minTriggerDuration = float(videoDetails['duration'])
            if float(videoDetails['duration']) > maxTriggerDuration:
                maxTriggerDuration = float(videoDetails['duration'])

        if videoDetails['hasDuoballs'] is True and videoDetails['hasTrigger'] is False:
            duoBallExercisesCounter += 1
            totalDuoBallsDuration += float(videoDetails['duration'])
            duoBallsExercises.append(videoDetailsReduced)
            if float(videoDetails['duration']) < minDuoBallsDuration:
                minDuoBallsDuration = float(videoDetails['duration'])
            if float(videoDetails['duration']) > maxDuoBallsDuration:
                maxDuoBallsDuration = float(videoDetails['duration'])


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

## prepare statistics for JSON dump
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

with open("videos/statistics.json", "w") as outfile:
    outfile.write(json_object)



