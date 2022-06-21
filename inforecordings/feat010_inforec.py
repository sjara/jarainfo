from jaratoolbox import celldatabase

subject = 'feat010'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2022-06-21', brainArea='AC_left', probe = 'NPv1-4542', recordingTrack='anterolateral_DiD', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp0)
# 11:20 in booth
# 11:31 in brain
# 11:36 reached max depth
# 11:56 started recording
# 13:09 done

exp0.add_site(2941)
exp0.maxDepth = 2941
exp0.add_session('11-54-41','a','AM','am_tuning_curve')
exp0.add_session('12-04-47','b','pureTones','am_tuning_curve')
#exp0.add_session('12-18-41','a','FTVOTBorders','2afc_speech') #lost saline, got very noisy.
exp0.add_session('12-38-02','b','FTVOTBorders','2afc_speech') #got noisy at the last ~10 trials or so, but it looks like we should still be able to sort the units out of the noise alright.


