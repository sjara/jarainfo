from jaratoolbox import celldatabase

subject = 'acid002'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2023-01-25', brainArea='AC_right', probe='NPv1-4552', recordingTrack='anteriormedial_DiD', info=['facesMedial', 'binaural']) #reference = tip
experiments.append(exp0)
#  13:50 in booth
#  14:05 in brain
#  14:08 reached max depth
#  14:30 started recording
#  15:12 done

exp0.add_site(3000)
exp0.maxDepth = 3002
exp0.add_session('14-30-23','apre','prePureTones','am_tuning_curve')#n320
# Injection Method 001- subq flank 14:39
exp0.add_session('14-39-34','apost','postPureTones','am_tuning_curve')#n320

exp0.add_site(3001)
exp0.add_session('14-48-55','bpre','prePureTones','am_tuning_curve')#n160
# Injection Method 002- subq scruf 14:53
exp0.add_session('14-55-09','bpost','postPureTones','am_tuning_curve')#n160

exp0.add_site(3002)
exp0.add_session('14-59-59','cpre','prePureTones','am_tuning_curve')#n160
# Injection Method 003- ip 15:06
exp0.add_session('15-07-53','cpost','postPureTones','am_tuning_curve')#n160



exp1 = celldatabase.Experiment(subject, '2023-01-31', brainArea='AC_left', probe='NPv1-4552', recordingTrack='anteriormedial_DiD', info=['facesMedial', 'binaural']) #reference = tip
experiments.append(exp1)
#  13:50 
#  14:05 
#  14:08 
#  14:30 
#  15:12

exp1.add_site(3010)
exp1.maxDepth = 3002
exp1.add_session('14-30-23','apre','prePureTones','am_tuning_curve')#n160
# Injection Method 001- subq flank 14:39
exp1.add_session('14-30-23','apre','injection','am_tuning_curve')#n16
0
exp1.add_session('14-39-34','apost','postPureTones','am_tuning_curve')#n160

exp1.add_site(3001)
exp1.add_session('14-48-55','bpre','prePureTones','am_tuning_curve')#n160
# Injection Method 002- subq scruf 14:53
exp1.add_session('14-55-09','bpost','postPureTones','am_tuning_curve')#n160

exp1.add_site(3002)
exp1.add_session('14-59-59','cpre','prePureTones','am_tuning_curve')#n160
# Injection Method 003- ip 15:06
exp1.add_session('15-07-53','cpost','postPureTones','am_tuning_curve')#n160

