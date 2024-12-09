from jaratoolbox import celldatabase

subject = 'test152'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-12-xx', brainArea='right_AC', probe='NPv2-XXXX', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])
# Reference electrode is the tip.
#experiments.append(expx)


#expx.add_site(3000)
#expx.maxDepth = 3000
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')

# LEFT HEMISPHERE

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-XX-XX', brainArea='right_AC', probe='NPv2-XXX', recordingTrack='anteriorXXX_DYE', info=['facesXXX', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp0)

#9:45am moues in booth

exp0.add_site(3000)
exp0.maxDepth = 3000
exp0.add_session('XX-XX-XX', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('XX-XX-XX', 'a', 'naturalSound', 'natural_sound_detection')
exp0.add_session('XX-XX-XX', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.
