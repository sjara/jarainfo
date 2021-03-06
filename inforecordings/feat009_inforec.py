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
# 16:26 done

exp0.add_site(2949)
exp0.maxDepth = 2949
exp0.add_session('15-19-36','a','AM','am_tuning_curve')
exp0.add_session('15-28-18','b','pureTones','am_tuning_curve')
exp0.add_session('15-46-19','a','FTVOTBorders','2afc_speech')


exp1 = celldatabase.Experiment(subject, '2022-06-05', brainArea='AC_left', probe = 'NPv1-4542', recordingTrack='anteromedial_DiD', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp1)
# 12:32 in booth
# 12:34 in brain
# 12:40 reached max depth. Very noisy today.
# 12:55 started recording
# 14:07 done

exp1.add_site(2972)
exp1.maxDepth = 2972
#exp1.add_session('12-57-32','a','AM','am_tuning_curve') #presented binaurally on accident.
exp1.add_session('13-06-25','b','pureTones','am_tuning_curve')
exp1.add_session('13-23-36','a','FTVOTBorders','2afc_speech')
exp1.add_session('13-59-18','c','AM','am_tuning_curve')


exp2 = celldatabase.Experiment(subject, '2022-06-06', brainArea='AC_left', probe = 'NPv1-4542', recordingTrack='anterolateral_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp2)
# 10:48 in booth
# 10:50 in brain
# 10:57 reached max depth. Very noisy today.
# 11:07 started recording
# 12:15 done

exp2.add_site(2916)
exp2.maxDepth = 2916
exp2.add_session('11-17-18','a','AM','am_tuning_curve')
exp2.add_session('11-26-35','b','pureTones','am_tuning_curve')
exp2.add_session('11-43-47','a','FTVOTBorders','2afc_speech')


exp3 = celldatabase.Experiment(subject, '2022-06-07', brainArea='AC_left', probe = 'NPv1-4161', recordingTrack='caudolateral_DiD', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp3)
# 10:48 in booth
# 11:04 in brain
# 11:09 reached max depth
# 11:30 started recording
# 12:28 done

exp3.add_site(2944)
exp3.maxDepth = 2944
exp3.add_session('11-31-19','a','AM','am_tuning_curve')
exp3.add_session('11-39-32','b','pureTones','am_tuning_curve')
exp3.add_session('11-57-21','a','FTVOTBorders','2afc_speech')


exp4 = celldatabase.Experiment(subject, '2022-06-09', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='anterior_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp4)
# 11:12 in booth
# 11:14 in brain
# 11:20 reached max depth
# 11:40 started recording
# 12:42 done

exp4.add_site(2788)
exp4.maxDepth = 2788
exp4.add_session('11-39-59','a','AM','am_tuning_curve')
exp4.add_session('11-49-31','b','pureTones','am_tuning_curve')
exp4.add_session('12-06-33','a','FTVOTBorders','2afc_speech')


exp5 = celldatabase.Experiment(subject, '2022-06-10', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='anteromedial_DiI', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp5)
# 09:17 in booth
# 09:27 couldn't penetrate brain, removed some remaining dura
# 09:35 in brain
# 09:42 reached max depth
# 09:58 started recording
# 10:53 done

exp5.add_site(2919)
exp5.maxDepth = 2919
exp5.add_session('09-58-06','a','AM','am_tuning_curve')
exp5.add_session('10-06-03','b','pureTones','am_tuning_curve')
exp5.add_session('10-22-02','a','FTVOTBorders','2afc_speech')


#exp6 = celldatabase.Experiment(subject, '2022-06-14', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
#experiments.append(exp6)
# 10:40 in booth
# 10:42 headbar fell off, recording cancelled
