from jaratoolbox import celldatabase

subject = 'inpi001'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.

exp0 = celldatabase.Experiment(subject, '2023-02-21', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp0)
#  Experiment Notes:
#  13:00 in booth
#  14:01 started recording 


exp0.maxDepth = 3004

exp0.add_site(3000) # reference: tip
exp0.add_session('15-26-24','a','PureTones','am_tuning_curve') #n320
exp0.add_session('15-34-58','a','FM_Up','oddball_sequence') #n500
exp0.add_session('15-41-37','b','FM_Down','oddball_sequence') #n500

# Experiment 2: 2023-02-22 #


exp0.add_site(3001) # reference: tip
exp0.add_session('11-53-26','a','PureTones','am_tuning_curve') #n320
exp0.add_session('12-12-27','a','FM_Up','oddball_sequence') #n500
exp0.add_session('12-23-20','b','FM_Down','oddball_sequence') #n500

# Experiment 3: 2023-02-24 #



exp0.add_site(3002) # reference: tip
exp0.add_session('10-20-20','a','PureTones','am_tuning_curve') #n320
exp0.add_session('10-31-09','a','FM_Up','oddball_sequence') #n500
exp0.add_session('10-39-55','b','FM_Down','oddball_sequence') #n500

# Experiment 3: 2023-02-28 #



exp0.add_site(3003) # reference: tip
exp0.add_session('12-39-18','a','PureTones','am_tuning_curve') #n320
exp0.add_session('12-53-07','a','FM_Up','oddball_sequence') #n500
exp0.add_session('13-01-31','b','FM_Down','oddball_sequence') #n500

# Experiment 4: 2023-03-07 #


exp0.add_site(3004) # reference: tip
exp0.add_session('16-44-20','a','PureTones','am_tuning_curve') #n320
exp0.add_session('16-52-33','a','FM_Up','oddball_sequence') #n500
exp0.add_session('16-59-19','b','FM_Down','oddball_sequence') #n500



