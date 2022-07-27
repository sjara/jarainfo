from jaratoolbox import celldatabase

subject = 'febe008'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2022-07-20', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='caudomedial_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
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


exp1 = celldatabase.Experiment(subject, '2022-07-21', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='caudomedial_DiI', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp1)
# 11:15 in booth
# 11:25 in brain
# 11:29 reached max depth
# 11:49 started recording
# 13:01 done

exp1.add_site(2883)
exp1.maxDepth = 2883
exp1.add_session('11-51-42','a','AM','am_tuning_curve')
exp1.add_session('12-01-19','b','pureTones','am_tuning_curve')
exp1.add_session('12-16-38','a','behaviorVOT','headfixed_speech') #did <100 trials.


exp2 = celldatabase.Experiment(subject, '2022-07-22', brainArea='AC_right', probe = 'NPv1-4161', recordingTrack='caudolateral_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp2)
# 11:15 in booth
# 11:40 in brain
# 11:47 reached max depth
# 12:07 started recording
# 13:01 done

exp2.add_site(2961)
exp2.maxDepth = 2961
exp2.add_session('12-06-40','a','behaviorVOT','headfixed_speech') 
exp2.add_session('12-50-51','a','AM','am_tuning_curve')
exp2.add_session('12-59-11','b','pureTones','am_tuning_curve')


exp3 = celldatabase.Experiment(subject, '2022-07-26', brainArea='AC_left', probe = 'NPv1-4161', recordingTrack='posterior_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp3)
# 13:20 in booth ... was making adjustments to pupillometry camera
# 13:56 in brain
# 14:04 reached max depth
# 14:24 started recording
# 15:51 done

exp3.add_site(2941)
exp3.maxDepth = 2941
exp3.add_session('14-28-22','a','behaviorVOT','headfixed_speech') #did very few trials :(
exp3.add_session('15-16-38','a','AM','am_tuning_curve')
exp3.add_session('15-24-37','b','pureTones','am_tuning_curve')


exp4 = celldatabase.Experiment(subject, '2022-07-27', brainArea='AC_left', probe = 'NPv1-4161', recordingTrack='_DiD', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp4)
# 12:57 in booth
# 13:05 in brain
# 13:09 reached max depth
# 13:30 started recording
# 15:00 done

exp4.add_site(3097)
exp4.maxDepth = 3097
exp4.add_session('13-35-01','a','behaviorVOT','headfixed_speech') exp4.add_session('14-34-17','a','AM','am_tuning_curve')
exp4.add_session('14-45-02','b','pureTones','am_tuning_curve')


