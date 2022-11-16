from jaratoolbox import celldatabase

subject = 'feat011'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2022-11-16', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='anteromedial_DiI', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp0)
#  10:14 in booth
#  10:27 in brain
#  10:34 reached max depth
#  10:54 started recording
#  11:58 done

exp0.add_site(2803)
exp0.maxDepth = 2803
exp0.add_session('10-57-52','a','AM','am_tuning_curve')
exp0.add_session('11-07-38','b','pureTones','am_tuning_curve')
exp0.add_session('11-24-50','a','FTVOTBorders','2afc_speech')


