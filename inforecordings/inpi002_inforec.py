from jaratoolbox import celldatabase

subject = 'inpi002'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.

exp0 = celldatabase.Experiment(subject, '2023-02-21', brainArea='AC_right', probe='NPv1-2641', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp0)
#  

exp0.maxDepth = 3000

exp0.add_site(3000) # reference: tip
exp0.add_session('17-33-54','a','PureTones','am_tuning_curve') #n320
exp0.add_session('17-56-12','a','FM_Up','oddball_sequence') #n500
exp0.add_session('18-09-11','b','FM_Down','oddball_sequence') #n500


# Experiment 2: 2023-02-23 #

exp1 = celldatabase.Experiment(subject, '2023-02-23', brainArea='AC_right', probe='NPv1-2641', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp1)
# Experiment Notes:

exp1.maxDepth = 3000

exp1.add_site(3000) # reference: tip
exp1.add_session('16-44-27','a','PureTones','am_tuning_curve') #n320
exp1.add_session('17-00-18','a','FM_Up','oddball_sequence') #n500
exp1.add_session('17-08-09','b','FM_Down','oddball_sequence') #n500
