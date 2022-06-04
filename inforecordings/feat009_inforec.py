from jaratoolbox import celldatabase

subject = 'feat009'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2022-06-04', brainArea='AC_left', probe = 'NPv1-4542', recordingTrack='caudomedial_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp0)
# 14:48 in booth
# 14:55 in brain
# 15:00 reached max depth
# 15:19 started recording
# 16: done

exp0.add_site(2949)
exp0.maxDepth = 2949
exp0.add_session('15-19-36','a','AM','am_tuning_curve')
exp0.add_session('15-28-18','b','pureTones','am_tuning_curve')
exp0.add_session('15-46-19','a','FTVOTBorders','2afc_speech')
