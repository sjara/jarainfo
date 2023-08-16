from jaratoolbox import celldatabase

subject = 'acid009'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


# 2023-08-04

exp0 = celldatabase.Experiment(subject, '2023-08-04', brainArea='AC_left', probe='NPv1-2641', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp0)

# Experiment Notes:
#  12:01 in booth
#  12:03 started recording
#  14:20 done

exp0.maxDepth = 3000

exp0.add_site(3000) 
exp0.add_session('12-03-37','apre','prePureTones','am_tuning_curve') #n321
exp0.add_session('12-11-52','apre','preHighFreq','oddball_sequence') #n501
exp0.add_session('12-17-26','bpre','preLowFreq','oddball_sequence') #n501
exp0.add_session('12-23-01','cpre','preFM_Down','oddball_sequence') #n501
exp0.add_session('12-29-24','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.11mL" subq flank- 15min
exp0.add_session('12-35-54','','salineInjection','')

exp0.add_session('12-51-12','asaline','salinePureTones','am_tuning_curve') #n321
exp0.add_session('12-59-17','asaline','salineHighFreq','oddball_sequence') #n501
exp0.add_session('13-04-48','bsaline','salineLowFreq','oddball_sequence') #n501
exp0.add_session('13-10-23','csaline','salineFM_Down','oddball_sequence') #n501
exp0.add_session('13-16-46','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.11mL" subq flank 15min
exp0.add_session('13-23-02','','doiInjection','')

exp0.add_session('13-38-26','adoi','doiPureTones','am_tuning_curve') #n321
exp0.add_session('13-46-14','adoi','doiHighFreq','oddball_sequence') #n501
exp0.add_session('13-51-42','bdoi','doiLowFreq','oddball_sequence') #n501
exp0.add_session('13-57-12','cdoi','doiFM_Down','oddball_sequence') #n501
exp0.add_session('14-03-30','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp0.add_session('14-09-44','','doiSpontaneous','')


# 2023-08-08

exp1 = celldatabase.Experiment(subject, '2023-08-08', brainArea='AC_left', probe='NPv1-2641', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp1)

# Experiment Notes:
#  13:45 in booth
#  13:47 started recording
#  16:07 done

exp1.maxDepth = 3000

exp1.add_site(3000) 
exp1.add_session('13-48-14','apre','prePureTones','am_tuning_curve') #n321
exp1.add_session('13-56-13','apre','preHighFreq','oddball_sequence') #n501
exp1.add_session('14-02-30','bpre','preLowFreq','oddball_sequence') #n501
exp1.add_session('14-09-17','cpre','preFM_Down','oddball_sequence') #n501
exp1.add_session('14-15-43','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.11mL" subq flank- 15min
exp1.add_session('14-22-06','','salineInjection','')

exp1.add_session('14-37-25','asaline','salinePureTones','am_tuning_curve') #n321
exp1.add_session('14-45-25','asaline','salineHighFreq','oddball_sequence') #n501
exp1.add_session('14-51-01','bsaline','salineLowFreq','oddball_sequence') #n501
exp1.add_session('14-56-42','csaline','salineFM_Down','oddball_sequence') #n501
exp1.add_session('15-03-11','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.11mL" subq flank 15min
exp1.add_session('15-09-33','','doiInjection','')

exp1.add_session('15-24-56','adoi','doiPureTones','am_tuning_curve') #n321
exp1.add_session('15-32-54','adoi','doiHighFreq','oddball_sequence') #n501
exp1.add_session('15-38-33','bdoi','doiLowFreq','oddball_sequence') #n501
exp1.add_session('15-44-11','cdoi','doiFM_Down','oddball_sequence') #n501
exp1.add_session('15-50-39','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp1.add_session('15-57-01','','doiSpontaneous','')



# 2023-08-10

exp2 = celldatabase.Experiment(subject, '2023-08-10', brainArea='AC_left', probe='NPv1-2641', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp2)

# Experiment Notes:
#  10:59 in booth
#  10:59 started recording
#  13:20 done

exp2.maxDepth = 3000

exp2.add_site(3000) 
exp2.add_session('10-59-42','apre','prePureTones','am_tuning_curve') #n321
exp2.add_session('11-07-41','apre','preHighFreq','oddball_sequence') #n501
exp2.add_session('11-13-17','bpre','preLowFreq','oddball_sequence') #n505
exp2.add_session('11-19-00','cpre','preFM_Down','oddball_sequence') #n501
exp2.add_session('11-25-30','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.11mL" subq flank- 15min
exp2.add_session('11-31-52','','salineInjection','')

exp2.add_session('11-47-12','asaline','salinePureTones','am_tuning_curve') #n321
exp2.add_session('11-55-12','asaline','salineHighFreq','oddball_sequence') #n501
exp2.add_session('12-00-52','bsaline','salineLowFreq','oddball_sequence') #n501
exp2.add_session('12-06-55','csaline','salineFM_Down','oddball_sequence') #n501
exp2.add_session('12-13-27','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.11mL" subq flank 15min
exp2.add_session('12-19-51','','doiInjection','')

exp2.add_session('12-35-24','adoi','doiPureTones','am_tuning_curve') #n321
exp2.add_session('12-43-27','adoi','doiHighFreq','oddball_sequence') #n501
exp2.add_session('12-49-04','bdoi','doiLowFreq','oddball_sequence') #n501
exp2.add_session('12-54-44','cdoi','doiFM_Down','oddball_sequence') #n501
exp2.add_session('13-01-16','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp2.add_session('13-07-39','','doiSpontaneous','')


# 2023-08-14

exp3 = celldatabase.Experiment(subject, '2023-08-14', brainArea='AC_left', probe='NPv1-2641', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp3)

# Experiment Notes:
#  13:56 in booth
#  13:57 started recording
#  16:15 done

exp3.maxDepth = 3000

exp3.add_site(3000) 
exp3.add_session('13-57-47','apre','prePureTones','am_tuning_curve') #n321
exp3.add_session('14-05-41','apre','preHighFreq','oddball_sequence') #n501
exp3.add_session('14-11-18','bpre','preLowFreq','oddball_sequence') #n501
exp3.add_session('14-16-57','cpre','preFM_Down','oddball_sequence') #n501
exp3.add_session('14-23-26','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.11mL" subq flank- 15min
exp3.add_session('14-29-49','','salineInjection','')

exp3.add_session('14-45-14','asaline','salinePureTones','am_tuning_curve') #n321
exp3.add_session('14-53-12','asaline','salineHighFreq','oddball_sequence') #n501
exp3.add_session('14-58-51','bsaline','salineLowFreq','oddball_sequence') #n501
exp3.add_session('15-04-36','csaline','salineFM_Down','oddball_sequence') #n502
exp3.add_session('15-11-15','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.11mL" subq flank 15min
exp3.add_session('15-17-39','','doiInjection','')

exp3.add_session('15-33-09','adoi','doiPureTones','am_tuning_curve') #n328
exp3.add_session('15-41-21','adoi','doiHighFreq','oddball_sequence') #n501
exp3.add_session('15-46-57','bdoi','doiLowFreq','oddball_sequence') #n501
exp3.add_session('15-52-37','cdoi','doiFM_Down','oddball_sequence') #n501
exp3.add_session('15-59-06','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp3.add_session('16-05-33','','doiSpontaneous','')



# 2023-08-16

exp4 = celldatabase.Experiment(subject, '2023-08-16', brainArea='AC_left', probe='NPv1-2641', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp4)

# Experiment Notes:
#  12:58 in booth
#  12:58 started recording
#  15:16 done

exp4.maxDepth = 3000

exp4.add_site(3000) 
exp4.add_session('12-58-52','apre','prePureTones','am_tuning_curve') #n321
exp4.add_session('13-06-47','apre','preHighFreq','oddball_sequence') #n501
exp4.add_session('13-12-24','bpre','preLowFreq','oddball_sequence') #n501
exp4.add_session('13-18-05','cpre','preFM_Down','oddball_sequence') #n501
exp4.add_session('13-24-41','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.11mL" subq flank- 15min
exp4.add_session('13-31-09','','salineInjection','')

exp4.add_session('13-46-31','asaline','salinePureTones','am_tuning_curve') #n330
exp4.add_session('13-54-45','asaline','salineHighFreq','oddball_sequence') #n501
exp4.add_session('14-00-26','bsaline','salineLowFreq','oddball_sequence') #n501
exp4.add_session('14-06-06','csaline','salineFM_Down','oddball_sequence') #n501
exp4.add_session('14-12-36','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.11mL" subq flank 15min
exp4.add_session('14-19-03','','doiInjection','')

exp4.add_session('14-34-25','adoi','doiPureTones','am_tuning_curve') #n321
exp4.add_session('14-42-22','adoi','doiHighFreq','oddball_sequence') #n505
exp4.add_session('14-48-01','bdoi','doiLowFreq','oddball_sequence') #n501
exp4.add_session('14-53-43','cdoi','doiFM_Down','oddball_sequence') #n501
exp4.add_session('15-00-15','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp4.add_session('15-06-37','','doiSpontaneous','')
