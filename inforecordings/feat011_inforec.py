from jaratoolbox import celldatabase

subject = 'feat011'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2022-11-16', brainArea='AC_right', probe='NPv1-4161', recordingTrack='anteromedial_DiI', info=['facesMedial', 'soundLeft']) #reference = tip
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


exp1 = celldatabase.Experiment(subject, '2022-11-17', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='anterolateral_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp1)
#  10:02 in booth
#  10:20 in brain
#  10:25 x axis bumped, probe removed to inspect
#  11:15 failed to reinsert probe. Recording session cancelled.


exp2 = celldatabase.Experiment(subject, '2022-11-18', brainArea='AC_left', probe='NPv1-4161', recordingTrack='anteromedial_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp2)
#  10:35 in booth
#  11:10 in brain 
#  11:20 reached max depth 
#  11:50 started recording 
#  12:55 done 

exp2.add_site(3000)
exp2.maxDepth = 3000
exp2.add_session('11-51-30','a','AM','am_tuning_curve')
exp2.add_session('12-00-20','b','pureTones','am_tuning_curve')
exp2.add_session('12-18-07','a','FTVOTBorders','2afc_speech')


exp3 = celldatabase.Experiment(subject, '2022-11-20', brainArea='AC_left', probe='NPv1-4161', recordingTrack='anterolateral_DiD', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp3)
#  13:50 in booth
#  14:04 in brain 
#  14:05 reached max depth 
#  14:24 started recording 
#  15:30 Realized first two session behavior data wasn't saved, re-ran them.
#  15:55 Done

exp3.add_site(3030)
exp3.maxDepth = 3030
exp3.add_session('15-47-45','a','AM','am_tuning_curve')
exp3.add_session('15-31-42','b','pureTones','am_tuning_curve')
exp3.add_session('14-50-51','a','FTVOTBorders','2afc_speech')


exp4 = celldatabase.Experiment(subject, '2022-11-21', brainArea='AC_left', probe='NPv1-4161', recordingTrack='posterior_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp4)
#  10:28 in booth
#  10:55 in brain 
#  10:56 reached max depth 
#  11:16 started recording 
#  12:14 Done

exp4.add_site(3040)
exp4.maxDepth = 3040
exp4.add_session('11-19-59','a','AM','am_tuning_curve')
exp4.add_session('11-27-32','b','pureTones','am_tuning_curve')
exp4.add_session('11-43-58','a','FTVOTBorders','2afc_speech')

