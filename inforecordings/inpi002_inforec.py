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


# Experiment 3: 2023-02-27 #

exp2 = celldatabase.Experiment(subject, '2023-02-27', brainArea='AC_right', probe='NPv1-2641', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp2)
# Experiment Notes:

exp2.maxDepth = 3000

exp2.add_site(3000) # reference: tip
exp2.add_session('16-41-36','a','PureTones','am_tuning_curve') #n320
exp2.add_session('16-51-57','a','FM_Up','oddball_sequence') #n500
exp2.add_session('17-01-15','b','FM_Down','oddball_sequence') #n500


# Experiment 3: 2023-03-02 #

exp3 = celldatabase.Experiment(subject, '2023-03-02', brainArea='AC_right', probe='NPv1-2641', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp3)
# Experiment Notes:

exp3.maxDepth = 3000

exp3.add_site(3000) # reference: tip
exp3.add_session('11-16-00','a','PureTones','am_tuning_curve') #n320
exp3.add_session('11-25-32','a','FM_Up','oddball_sequence') #n500
exp3.add_session('11-33-36','b','FM_Down','oddball_sequence') #n500


# Experiment 4: 2023-03-07 #

exp4 = celldatabase.Experiment(subject, '2023-03-07', brainArea='AC_right', probe='NPv1-2641', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp4)
# Experiment Notes:

exp4.maxDepth = 3000

exp4.add_site(3000) # reference: tip
exp4.add_session('11-30-27','a','PureTones','am_tuning_curve') #n320
exp4.add_session('11-40-11','a','FM_Up','oddball_sequence') #n500
exp4.add_session('11-47-42','b','FM_Down','oddball_sequence') #n500


# Experiment 5: 2023-03-13 #

exp5 = celldatabase.Experiment(subject, '2023-03-13', brainArea='AC_right', probe='NPv1-2641', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp5)
# Experiment Notes:

exp5.maxDepth = 3000

exp5.add_site(3000) # reference: tip
exp5.add_session('17-15-24','a','PureTones','am_tuning_curve') #n320
exp5.add_session('17-24-10','a','FM_Up','oddball_sequence') #n500
exp5.add_session('17-32-25','b','FM_Down','oddball_sequence') #n500

'''
Below moved to acid007_inforec.py

#-------------------------------------
# Max's DOI Study:


# 2023-03-23
# Saline

exp0 = celldatabase.Experiment(subject, '2023-03-23', brainArea='AC_right', probe='NPv1-2641', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp0)

# Experiment Notes:
#  14:01 in booth
#  14:03 started recording
#  15:25 done

exp0.maxDepth = 3000

exp0.add_site(3000) # reference: tip
exp0.add_session('14-03-17','apre','prePureTones','am_tuning_curve') #n321
exp0.add_session('14-11-12','apre','preHighFreq','oddball_sequence') #n501
exp0.add_session('14-16-47','bpre','preLowFreq','oddball_sequence') #n501
exp0.add_session('14-22-26','cpre','preFM_Down','oddball_sequence') #n511
exp0.add_session('14-29-03','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.138mL" subq flank- 15min
exp0.add_session('14-35-17','aduring','','')

exp0.add_session('14-50-32','asaline','salinePureTones','am_tuning_curve') #n321
exp0.add_session('14-58-28','asaline','salineHighFreq','oddball_sequence') #n501
exp0.add_session('15-04-02','bsaline','salineLowFreq','oddball_sequence') #n501
exp0.add_session('15-09-37','csaline','salineFM_Down','oddball_sequence') #n501
exp0.add_session('15-16-01','dsaline','salineFM_Up','oddball_sequence') #n501



# 2023-03-24
# DOI

exp1 = celldatabase.Experiment(subject, '2023-03-24', brainArea='AC_right', probe='NPv1-2641', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp1)

# Experiment Notes:
#  10:30 in booth
#  10:31 started recording
#  11:55 done

exp1.maxDepth = 3000

exp1.add_site(3000) # reference: tip
exp1.add_session('10-31-37','apre','prePureTones','am_tuning_curve') #n321
exp1.add_session('10-39-28','apre','preHighFreq','oddball_sequence') #n501
exp1.add_session('10-45-04','bpre','preLowFreq','oddball_sequence') #n501
exp1.add_session('10-50-55','cpre','preFM_Down','oddball_sequence') #n501
exp1.add_session('10-57-21','dpre','preFM_Up','oddball_sequence') #n501


#doi "0.14mL" subq flank 15min
exp1.add_session('11-03-57','aduring','','')

exp1.add_session('11-19-14','adoi','doiPureTones','am_tuning_curve') #n321
exp1.add_session('11-27-08','adoi','doiHighFreq','oddball_sequence') #n501
exp1.add_session('11-32-44','bdoi','doiLowFreq','oddball_sequence') #n501
exp1.add_session('11-38-25','cdoi','doiFM_Down','oddball_sequence') #n501
exp1.add_session('11-44-49','ddoi','doiFM_Up','oddball_sequence') #n501

Above moved to acid007_inforec.py
'''
