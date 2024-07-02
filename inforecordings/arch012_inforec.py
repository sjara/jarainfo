from jaratoolbox import celldatabase

subject = 'Arch012'
experiments = [Inactivation of auditory thalamo-striatal or cortico-striatal pathways]

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

exp0 = celldatabase.Experiment(subject, '2024-05-29', brainArea='left_AudStr', probe='NPv1-2141', recordingTrack='posteriorlateral_DiD', info=['facesAnterior', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp0)
# 12:52 sylgard removed added saline
# 13:02 attached headstage
# 13:06 probe to pia
# 13:09 probe in brain and added saline
# 13:18 reached target depth
# 13:37 15 minutes for brain to settle

exp0.add_site()
exp0.maxDepth = 1800
exp0.add_session('13-38-29', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('13-51-22', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2024-06-16', brainArea='left_AudStr', probe='NPv1-4432', recordingTrack='posteriorlateral_DiD', info=['facesMedial', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp1)
# DiD dye used - electrode inserted posterior and to the left of the craniotomy
# Removed dura 17:15
# 17:35 probe to pia
# 17:45 probe in brain and added saline
# 18:25 reached target depth
# 18:50 20 minutes for brain to settle

exp1.add_site(2000)
exp1.maxDepth = 2900
exp1.add_session('18-43-50', 'a', 'AM', 'am_tuning_curve')
exp1.add_session('18-59-36', 'a', 'naturalSound', 'natural_sound_detection')
exp1.add_session('19-26-04', 'b', 'pureTones', 'am_tuning_curve')



