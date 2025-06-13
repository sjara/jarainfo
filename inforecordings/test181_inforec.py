from jaratoolbox import celldatabase

subject = 'test181'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2025-06-13', brainArea='left_pStr', probe='NPv2-1134', recordingTrack='centerCenter_noDye', info=['facesLateral', 'soundRight'])

# 2025-06-12 attempted to insert sharpened dummy probe to the left hemisphere but the sharpened probe would not penetrate the surface of the brain regardless of multiple attempts and removing dura. May have been a blood vessle in the way. We are replicating the insertion 2025-06-13 in the right hemisphere 

# Attempted to insert dummy probe on right hemisphere 2025-06-13 and was still unable to insert the sharpend probe. 

# Lots of dura removal again was able to insert probe and record

experiments.append(exp0)

exp0.add_site(1500)
exp0.maxDepth = 1500
exp0.add_session('15-16-42', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('15-27-11', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


