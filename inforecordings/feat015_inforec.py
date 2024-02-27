from jaratoolbox import celldatabase

subject = 'feat015'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-02-23', brainArea='AC_right', probe='NPv1-4542', recordingTrack='posteriorlateral_na', info=['facesAnterior', 'soundLeft'])
# Reference electrode is the tip.

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
