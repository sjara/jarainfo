from jaratoolbox import celldatabase

subject = 'test00A'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-xx-xx', brainArea='AC_right', probe='NPv1-4542', recordingTrack='medialxxx_DYE', info=['facesxx', 'soundLeft'])
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

exp0 = celldatabase.Experiment(subject, '2026-08-26', brainArea='left_AudStr', probe='NPv2-1392', recordingTrack='posteriorlateral_DiD', info=['facesAnterior', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp0)
# 12:52 sylgard removed added saline
# 13:02 attached headstage
# 13:06 probe to pia
# 13:09 probe in brain and added saline
# 13:18 reached target depth
# 13:37 15 minutes for brain to settle

exp0.add_site(3600)
exp0.maxDepth = 3600
exp0.add_session('15-54-41', 'a', 'pureTones', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


