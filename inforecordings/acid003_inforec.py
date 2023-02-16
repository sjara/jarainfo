from jaratoolbox import celldatabase

subject = 'acid003'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2023-02-10', brainArea='AC_left', probe='NPv1-4542', recordingTrack='anteriorlateral_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp0)
#  13:20 in booth
#  11:30 in brain
#  13:32 reached max depth
#  13:47 started recording
#  14:12 done

exp0.add_site(3000)
exp0.maxDepth = 3002
exp0.add_session('13-47-21','apre','prePureTones','am_tuning_curve')#n160
# Injection Method 001- subq flank 14:39
exp0.add_session('13-51-11','aduring','','')
exp0.add_session('13-52-46','apost','postPureTones','am_tuning_curve')#n160

exp0.add_site(3001)
exp0.add_session('13-57-12','bpre','prePureTones','am_tuning_curve')#n160
# Injection Method 002- subq scruf 14:53
exp0.add_session('14-01-07','bduring','','')
exp0.add_session('14-02-36','bpost','postPureTones','am_tuning_curve')#n160

exp0.add_site(3002)
exp0.add_session('14-06-53','cpre','prePureTones','am_tuning_curve')#n160
# Injection Method 003- ip 15:06
exp0.add_session('14-11-02','cduring','','')
exp0.add_session('14-12-17','cpost','postPureTones','am_tuning_curve')#n160


exp1 = celldatabase.Experiment(subject, '2023-02-15', brainArea='AC_right', probe='NPv1-4542', recordingTrack='anteriormedial_DiD', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp1)
#  09:50 in booth
#  10:13 in brain
#  10:14 reached max depth
#  10:44 started recording
#  14:12 done

exp1.add_site(3100)
exp1.maxDepth = 3102
exp1.add_session('10-45-17','apre','prePureTones','am_tuning_curve')#n160
# Injection Method 003- IP 14:50
exp1.add_session('10-49-40','aduring','','')
exp1.add_session('10-52-09','apost','postPureTones','am_tuning_curve')#n160

exp1.add_site(3101)
exp1.add_session('10-56-35','bpre','prePureTones','am_tuning_curve')#n160
# Injection Method 002- subq scruf 11:01
exp1.add_session('11-00-31','bduring','','')
exp1.add_session('11-02-17','bpost','postPureTones','am_tuning_curve')#n160

exp1.add_site(3102)
exp1.add_session('11-07-04','cpre','prePureTones','am_tuning_curve')#n160
# Injection Method 001- subq flank 11:11
exp1.add_session('11-10-55','cduring','','')
exp1.add_session('11-12-17','cpost','postPureTones','am_tuning_curve')#n160


exp2 = celldatabase.Experiment(subject, '2023-02-16', brainArea='AC_right', probe='NPv1-4542', recordingTrack='posteriorlateral_DiI', info=['facesMedial', 'soundLeft']) #reference = tip
experiments.append(exp2)
#  10:30 in booth
#  10:38 in brain
#  10:39 reached max depth
#  11:09 started recording
#  12:23 done

exp2.add_site(3050)
exp2.maxDepth = 3050
exp2.add_session('11-10-00','apre','prePureTones','am_tuning_curve') #n320
exp2.add_session('11-19-14','apre','preHighFreq','oddball_sequence') #n500
exp2.add_session('11-24-57','bpre','preLowFreq','oddball_sequence')
exp2.add_session('11-30-43','cpre','preFM_Down','oddball_sequence')
exp2.add_session('11-37-12','dpre','preFM_Up','oddball_sequence')

#saline 0.1mL subq flank
exp2.add_session('11-43-31','aduring','','')

exp2.add_session('11-46-21','apost','postPureTones','am_tuning_curve') #accidentally ran ~450 trials
exp2.add_session('11-57-51','apost','postHighFreq','oddball_sequence')
exp2.add_session('12-03-54','bpost','postLowFreq','oddball_sequence')
exp2.add_session('12-10-21','cpost','postFM_Down','oddball_sequence')
exp2.add_session('12-16-59','dpost','postFM_Up','oddball_sequence')

