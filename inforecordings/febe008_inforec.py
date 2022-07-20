from jaratoolbox import celldatabase

subject = 'febe008'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2022-07-20', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='anteromedial_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp0)
# 13:25 in booth
# 13:36 in brain
# 13:42 reached max depth
# 13:59 started recording
# 15:30 done

exp0.add_site(2974)
exp0.maxDepth = 2974
exp0.add_session('13-59-38','a','behaviorVOT','headfixed_speech') 
exp0.add_session('15-03-09','a','AM','am_tuning_curve')
exp0.add_session('15-13-21','b','pureTones','am_tuning_curve')

