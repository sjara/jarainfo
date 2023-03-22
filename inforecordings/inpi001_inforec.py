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


exp0.maxDepth = 3000

exp0.add_site(3000) # reference: tip
exp0.add_session('15-26-24','a','PureTones','am_tuning_curve') #n320
exp0.add_session('15-34-58','a','FM_Up','oddball_sequence') #n500
exp0.add_session('15-41-37','b','FM_Down','oddball_sequence') #n500

# Experiment 2: 2023-02-22 #

exp1 = celldatabase.Experiment(subject, '2023-02-22', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp1)

# Experiment Notes:

exp1.maxDepth = 3000

exp1.add_site(3000) # reference: tip
exp1.add_session('11-53-26','a','PureTones','am_tuning_curve') #n320
exp1.add_session('12-12-27','a','FM_Up','oddball_sequence') #n500
exp1.add_session('12-23-20','b','FM_Down','oddball_sequence') #n500

# Experiment 3: 2023-02-24 #

exp2 = celldatabase.Experiment(subject, '2023-02-24', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp2)

# Experiment Notes:

exp2.maxDepth = 3000

exp2.add_site(3000) # reference: tip
exp2.add_session('10-20-20','a','PureTones','am_tuning_curve') #n320
exp2.add_session('10-31-09','a','FM_Up','oddball_sequence') #n500
exp2.add_session('10-39-55','b','FM_Down','oddball_sequence') #n500

# Experiment 3: 2023-02-28 #

exp3 = celldatabase.Experiment(subject, '2023-02-28', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp3)

# Experiment Notes:
# did 500 trials for the first one 

exp3.maxDepth = 3000

exp3.add_site(3000) # reference: tip
exp3.add_session('12-39-18','a','PureTones','am_tuning_curve') #n320
exp3.add_session('12-53-07','a','FM_Up','oddball_sequence') #n500
exp3.add_session('13-01-31','b','FM_Down','oddball_sequence') #n500

# Experiment 4: 2023-03-07 #

exp4 = celldatabase.Experiment(subject, '2023-03-07', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp4)

# Experiment Notes:

exp4.maxDepth = 3000

exp4.add_site(3000) # reference: tip
exp4.add_session('16-44-20','a','PureTones','am_tuning_curve') #n320
exp4.add_session('16-52-33','a','FM_Up','oddball_sequence') #n500
exp4.add_session('16-59-19','b','FM_Down','oddball_sequence') #n500

# Experiment 4: 2023-03-07 #

exp5 = celldatabase.Experiment(subject, '2023-03-13', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp5)

# Experiment Notes:

exp5.maxDepth = 3000

exp5.add_site(3000) # reference: tip
exp5.add_session('09-42-59','a','PureTones','am_tuning_curve') #n320
exp5.add_session('09-52-03','a','FM_Up','oddball_sequence') #n500
exp5.add_session('09-58-32','b','FM_Down','oddball_sequence') #n500




# Max's DOI study

# Experiment 6: 2023-03-22

exp6 = celldatabase.Experiment(subject, '2023-03-22', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp6)

# Experiment Notes:
#  11:47 in booth
#  14:51 started recording
#  12:23 done

exp6.maxDepth = 3000

exp6.add_site(3000) # reference: tip
exp6.add_session('11-53-23','apre','prePureTones','am_tuning_curve') #n321
exp6.add_session('12-06-32','apre','preHighFreq','oddball_sequence') #n501
exp6.add_session('--','bpre','preLowFreq','oddball_sequence') #n502
exp6.add_session('--','cpre','preFM_Down','oddball_sequence') #n501
exp6.add_session('--','dpre','preFM_Up','oddball_sequence') #n501

#saline "" subq flank
exp6.add_session('15-28-38','aduring','','')

exp6.add_session('15-30-37','asaline','salinePureTones','am_tuning_curve') #n321
exp6.add_session('15-38-41','asaline','salineHighFreq','oddball_sequence') #n501
exp6.add_session('15-44-16','bsaline','salineLowFreq','oddball_sequence') #n501
exp6.add_session('15-50-16','csaline','salineFM_Down','oddball_sequence') #n501
exp6.add_session('15-56-44','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "" subq flank
exp6.add_session('15-28-38','bduring','','')

exp6.add_session('15-30-37','adoi','doiPureTones','am_tuning_curve') #n321
exp6.add_session('15-38-41','adoi','doiHighFreq','oddball_sequence') #n501
exp6.add_session('15-44-16','bdoi','doiLowFreq','oddball_sequence') #n501
exp6.add_session('15-50-16','cdoi','doiFM_Down','oddball_sequence') #n501
exp6.add_session('15-56-44','ddoi','doiFM_Up','oddball_sequence') #n501
