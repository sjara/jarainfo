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


exp1 = celldatabase.Experiment(subject, '2022-06-22', brainArea='AC_left', probe = 'NPv1-4542', recordingTrack='anteromedial_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp1)
# 10:58 in booth
# 11:01 in brain
# 11:09 reached max depth
# 11:30 started recording
# 12:30 done

exp1.add_site(2973)
exp1.maxDepth = 2973
exp1.add_session('11-35-26','a','AM','am_tuning_curve')
exp1.add_session('11-44-09','b','pureTones','am_tuning_curve')
exp1.add_session('12-00-49','a','FTVOTBorders','2afc_speech') 


exp2 = celldatabase.Experiment(subject, '2022-06-27', brainArea='AC_right', probe = 'NPv1-4542', recordingTrack='anteromedial_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp2)
# 14:45 in booth
# 14:52 in brain
# 14:58 reached max depth
# 15:18 started recording
# 16:14 done

exp2.add_site(3056)
exp2.maxDepth = 3056
exp2.add_session('15-17-45','a','AM','am_tuning_curve')
exp2.add_session('15-26-40','b','pureTones','am_tuning_curve')
exp2.add_session('15-43-18','a','FTVOTBorders','2afc_speech') 


exp3 = celldatabase.Experiment(subject, '2022-06-28', brainArea='AC_right', probe = 'NPv1-4542', recordingTrack='middlemedial_DiI', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp3)
# 10:36 in booth
# 10:39 in brain
# 10:43 reached max depth
# 11:03 started recording
# 11:59 done

exp3.add_site(2958)
exp3.maxDepth = 2958
exp3.add_session('11-02-07','a','AM','am_tuning_curve')
exp3.add_session('11-10-51','b','pureTones','am_tuning_curve')
exp3.add_session('11-28-21','a','FTVOTBorders','2afc_speech') 


exp4 = celldatabase.Experiment(subject, '2022-06-30', brainArea='AC_right', probe = 'NPv1-4542', recordingTrack='posterior_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp4)
# 10:32 in booth
# 10:38 in brain
# 10:41 reached max depth
# 11:00 started recording
# 11:57 done

exp4.add_site(2992)
exp4.maxDepth = 2992
exp4.add_session('11-00-11','a','AM','am_tuning_curve')
exp4.add_session('11-08-03','b','pureTones','am_tuning_curve')
exp4.add_session('11-25-31','a','FTVOTBorders','2afc_speech') 


