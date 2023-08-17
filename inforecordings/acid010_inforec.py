from jaratoolbox import celldatabase

subject = 'acid010'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


# 2023-08-07

exp0 = celldatabase.Experiment(subject, '2023-08-07', brainArea='AC_left', probe='NPv1-2642', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp0)

# Experiment Notes:
#  10:50 in booth
#  10:53 started recording
#  13:12 done

exp0.maxDepth = 3000

exp0.add_site(3000) 
exp0.add_session('10-53-44','apre','prePureTones','am_tuning_curve') #n321
exp0.add_session('11-01-30','apre','preHighFreq','oddball_sequence') #n501
exp0.add_session('11-07-12','bpre','preLowFreq','oddball_sequence') #n501
exp0.add_session('11-12-50','cpre','preFM_Down','oddball_sequence') #n501
exp0.add_session('11-19-12','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.12mL" subq flank- 15min
exp0.add_session('11-25-27','','salineInjection','')

exp0.add_session('11-40-50','asaline','salinePureTones','am_tuning_curve') #n321
exp0.add_session('11-48-39','asaline','salineHighFreq','oddball_sequence') #n504
exp0.add_session('11-54-22','bsaline','salineLowFreq','oddball_sequence') #n501
exp0.add_session('11-59-52','csaline','salineFM_Down','oddball_sequence') #n501
exp0.add_session('12-06-15','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.12mL" subq flank 15min
exp0.add_session('12-12-31','','doiInjection','')

exp0.add_session('12-29-27','adoi','doiPureTones','am_tuning_curve') #n396
exp0.add_session('12-38-58','adoi','doiHighFreq','oddball_sequence') #n501
exp0.add_session('12-44-32','bdoi','doiLowFreq','oddball_sequence') #n501
exp0.add_session('12-50-06','cdoi','doiFM_Down','oddball_sequence') #n501
exp0.add_session('12-56-25','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp0.add_session('13-02-36','','doiSpontaneous','')



# 2023-08-09

exp1 = celldatabase.Experiment(subject, '2023-08-09', brainArea='AC_left', probe='NPv1-2642', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp1)

# Experiment Notes:
#  11:25 in booth
#  11:28 started recording
#  13:45 done

exp1.maxDepth = 3000

exp1.add_site(3000) 
exp1.add_session('11-28-08','apre','prePureTones','am_tuning_curve') #n321
exp1.add_session('11-35-57','apre','preHighFreq','oddball_sequence') #n501
exp1.add_session('11-41-31','bpre','preLowFreq','oddball_sequence') #n501
exp1.add_session('11-47-05','cpre','preFM_Down','oddball_sequence') #n501
exp1.add_session('11-53-31','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.12mL" subq flank- 15min
exp1.add_session('11-59-51','','salineInjection','')

exp1.add_session('12-15-13','asaline','salinePureTones','am_tuning_curve') #n356
exp1.add_session('12-23-57','asaline','salineHighFreq','oddball_sequence') #n501
exp1.add_session('12-29-33','bsaline','salineLowFreq','oddball_sequence') #n501
exp1.add_session('12-35-11','csaline','salineFM_Down','oddball_sequence') #n501
exp1.add_session('12-41-40','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.12mL" subq flank 15min
exp1.add_session('12-48-00','','doiInjection','')

exp1.add_session('13-03-23','adoi','doiPureTones','am_tuning_curve') #n323
exp1.add_session('13-11-21','adoi','doiHighFreq','oddball_sequence') #n501
exp1.add_session('13-16-56','bdoi','doiLowFreq','oddball_sequence') #n501
exp1.add_session('13-22-33','cdoi','doiFM_Down','oddball_sequence') #n501
exp1.add_session('13-29-00','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp1.add_session('13-35-19','','doiSpontaneous','')



# 2023-08-14

exp2 = celldatabase.Experiment(subject, '2023-08-14', brainArea='AC_left', probe='NPv1-2642', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp2)

# Experiment Notes:
#  11:20 in booth
#  11:22 started recording
#  13:40 done

exp2.maxDepth = 3000

exp2.add_site(3000) 
exp2.add_session('11-22-21','apre','prePureTones','am_tuning_curve') #n321
exp2.add_session('11-30-20','apre','preHighFreq','oddball_sequence') #n501
exp2.add_session('11-35-59','bpre','preLowFreq','oddball_sequence') #n501
exp2.add_session('11-41-38','cpre','preFM_Down','oddball_sequence') #n501
exp2.add_session('11-48-07','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.12mL" subq flank- 15min
exp2.add_session('11-54-40','','salineInjection','')

exp2.add_session('12-10-02','asaline','salinePureTones','am_tuning_curve') #n321
exp2.add_session('12-17-59','asaline','salineHighFreq','oddball_sequence') #n501
exp2.add_session('12-23-37','bsaline','salineLowFreq','oddball_sequence') #n501
exp2.add_session('12-29-16','csaline','salineFM_Down','oddball_sequence') #n501
exp2.add_session('12-35-45','dsaline','salineFM_Up','oddball_sequence') #n513

#doi "0.12mL" subq flank 15min
exp2.add_session('12-42-30','','doiInjection','')

exp2.add_session('12-58-04','adoi','doiPureTones','am_tuning_curve') #n321
exp2.add_session('13-05-56','adoi','doiHighFreq','oddball_sequence') #n501
exp2.add_session('13-11-36','bdoi','doiLowFreq','oddball_sequence') #n501
exp2.add_session('13-17-15','cdoi','doiFM_Down','oddball_sequence') #n501
exp2.add_session('13-23-44','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp2.add_session('13-30-07','','doiSpontaneous','')



# 2023-08-17

exp3 = celldatabase.Experiment(subject, '2023-08-17', brainArea='AC_left', probe='NPv1-2642', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp3)

# Experiment Notes:
#  14:33 in booth
#  14:35 started recording
#  : done

exp3.maxDepth = 3000

exp3.add_site(3000) 
exp3.add_session('14-46-16','apre','prePureTones','am_tuning_curve') #n321
exp3.add_session('14-54-49','apre','preHighFreq','oddball_sequence') #n501
exp3.add_session('15-00-26','bpre','preLowFreq','oddball_sequence') #n501
exp3.add_session('15-06-06','cpre','preFM_Down','oddball_sequence') #n501
exp3.add_session('15-12-36','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.12mL" subq flank- 15min
exp3.add_session('15-18-59','','salineInjection','')

exp3.add_session('15-35-16','asaline','salinePureTones','am_tuning_curve') #n321
exp3.add_session('15-43-16','asaline','salineHighFreq','oddball_sequence') #n501
exp3.add_session('15-48-54','bsaline','salineLowFreq','oddball_sequence') #n501
exp3.add_session('15-54-32','csaline','salineFM_Down','oddball_sequence') #n501
exp3.add_session('16-01-02','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.12mL" subq flank 15min
exp3.add_session('16-07-26','','doiInjection','')

exp3.add_session('16-23-46','adoi','doiPureTones','am_tuning_curve') #n321
exp3.add_session('16-31-39','adoi','doiHighFreq','oddball_sequence') #n501
exp3.add_session('16-37-14','bdoi','doiLowFreq','oddball_sequence') #n501
exp3.add_session('16-42-51','cdoi','doiFM_Down','oddball_sequence') #n501
exp3.add_session('16-49-18','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp3.add_session('16-55-42','','doiSpontaneous','')
