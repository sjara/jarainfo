from jaratoolbox import celldatabase

subject = 'feat017'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-xx-xx', brainArea='AC_right', probe='NPv1-4542', recordingTrack='medialxxx_DYE', info=['facesxx', 'soundxxx'])
# Reference electrode is the tip.
#experiments.append(expx)


#expx.add_site(3000)
#expx.maxDepth = 3000
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-03-25', brainArea='AC_left', probe='NPv1-4542', recordingTrack='anteriorCenter_DiO', info=['facesPosterior', 'soundRight'])

# Reference electrode is the tip.
experiments.append(exp0)
# 2:40pm - max depth brain left to settle for 20 minutes
# 3:02pm pure tones start
# 3:15pm start AM sounds 
# 3:24pm - start natural sounds 


exp0.add_site(3000)
exp0.maxDepth = 3000
exp0.add_session('15-03-11', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('15-15-32', 'b', 'AM', 'am_tuning_curve')
exp0.add_session('15-25-02', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2024-03-26', brainArea='AC_left', probe='NPv1-4542', recordingTrack='anteriorMedial_DiL', info=['facesAnterior', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp1)
# Target depth reached 2:04pm - waited 20 minutes for brain to settle
# Started pure tones at 2:24pm 
# Started AM 2:36pm
# Started natural sounds at 2:46pm 


exp1.add_site(3000)
exp1.maxDepth = 3000
exp1.add_session('14-23-56', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('14-35-57', 'b', 'AM', 'am_tuning_curve')
exp1.add_session('14-46-38', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.
