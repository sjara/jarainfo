from jaratoolbox import celldatabase

subject = 'wifi008'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])
# Reference electrode is 1:tip
#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2025-05-28', brainArea='right_AC', probe='NPv2-5422', recordingTrack='posteriorCenter_DiD', info=['facesPosterior', 'soundLeft'])

experiments.append(exp0)

# Reference electrode is 3:tip
# 58 degrees with respect to the horizontal axis
# 83 degrees with respect to the azimuth axis
# Targeting A1
# Probe is located posterior center leaning medial
# All shanks active 1-96
# Left brain to settle for 15 minutes

exp0.add_site(2000)
exp0.maxDepth = 2000
exp0.add_session('11-35-03', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('11-45-48', 'a', 'naturalSound', 'natural_sound_detection')
exp0.add_session('12-13-35', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


