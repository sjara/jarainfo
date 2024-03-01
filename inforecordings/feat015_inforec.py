from jaratoolbox import celldatabase

subject = 'feat015'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-02-23', brainArea='AC_right', probe='NPv1-4542', recordingTrack='posteriorlateral_na', info=['facesAnterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp0)
# 12:52 sylgard removed added saline
# 1:02 attached headstage
# 1:06 probe to pia
# 1:09 probe in brain and added saline
# 1:18 reached target depth
# 1:37 15 minutes for brain to settle

exp0.add_site(1100)
exp0.maxDepth = 1100
exp0.add_session('13-38-29', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('13-51-22', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2024-02-27', brainArea='AC_right', probe='NPv1-4542', recordingTrack='posteriorlateral_Dil', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp1)
# Dil dye used - electrode inserted posterior and to the left of the craniotomy
# Removed dura 11:30am
# 11:50am probe to pia
# 11:53am probe in brain and added saline
# 11:57am reached target depth
# 11:58am 20 minutes for brain to settle

exp1.add_site(2900)
exp1.maxDepth = 2900
exp1.add_session('12-19-12', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('12-31-30', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp2 = celldatabase.Experiment(subject, '2024-02-28', brainArea='AC_right', probe='NPv1-4542', recordingTrack='anteriorlateral_DiO', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp2)
# DiO dye used - electrode inserted anterior and to the left of the craniotomy
#  probe to pia 6:00pm
#  probe in brain and added saline
#  6:30pm reached target depth
#  6:35pm 15 minutes for brain to settle

exp2.add_site(1700)
exp2.maxDepth = 1700
exp2.add_session('18-48-54', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('18-59-42', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp3 = celldatabase.Experiment(subject, '2024-03-01', brainArea='AC_right', probe='NPv1-4542', recordingTrack='posteriorMedial_DiD', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp3)

# DiD dye used - electrode inserted posterior and middle of the craniotomy
#  11:44am probe to pia 
#  11:50am probe in brain and added saline 
#  reached target depth 11:58am and set 15 minutes for brain to settle

exp3.add_site(3500)
exp3.maxDepth = 3500
exp3.add_session('12-20-12', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('12-33-34', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


