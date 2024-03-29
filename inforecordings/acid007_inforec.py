from jaratoolbox import celldatabase

# Mouse was formerly known as 'inpi002'.

subject = 'acid007'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


'''
# Commented out 2023-03-23 and 2023-03-24 due to not able to process combined multiday sessions yet.

# 2023-03-23
# Saline

exp0 = celldatabase.Experiment(subject, '2023-03-23', brainArea='AC_right', probe='NPv1-2641', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = tip
experiments.append(exp0)

# Experiment Notes:
#  14:01 in booth
#  14:03 started recording
#  15:25 done

exp0.maxDepth = 3000

exp0.add_site(3000)
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

exp1 = celldatabase.Experiment(subject, '2023-03-24', brainArea='AC_right', probe='NPv1-2641', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = tip
experiments.append(exp1)

# Experiment Notes:
#  10:30 in booth
#  10:31 started recording
#  11:55 done

exp1.maxDepth = 3000

exp1.add_site(3000)
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


'''

# 2023-05-17
# DOI & Saline

exp2 = celldatabase.Experiment(subject, '2023-05-17', brainArea='AC_right', probe='NPv1-2641', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = ext
experiments.append(exp2)

# Experiment Notes:
#  11:20 Start
#  13:30 Done
# 

exp2.maxDepth = 3000

exp2.add_site(3000)
exp2.add_session('11-22-07','apre','prePureTones','am_tuning_curve') #n321
exp2.add_session('11-30-27','apre','preHighFreq','oddball_sequence') #n501
exp2.add_session('11-36-00','bpre','preLowFreq','oddball_sequence') #n506
exp2.add_session('11-41-39','cpre','preFM_Down','oddball_sequence') #n501
exp2.add_session('11-48-05','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.15mL" subq flank- 15min
exp2.add_session('11-54-28','','salineInjection','')

exp2.add_session('12-10-03','asaline','salinePureTones','am_tuning_curve') #n321
exp2.add_session('12-18-03','asaline','salineHighFreq','oddball_sequence') #n501
exp2.add_session('12-23-35','bsaline','salineLowFreq','oddball_sequence') #n501
exp2.add_session('12-29-09','csaline','salineFM_Down','oddball_sequence') #n501
exp2.add_session('12-35-32','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.15mL" subq flank 15min
exp2.add_session('12-42-18','','doiInjection','')

exp2.add_session('12-58-23','adoi','doiPureTones','am_tuning_curve') #n321
exp2.add_session('13-06-14','adoi','doiHighFreq','oddball_sequence') #n501
exp2.add_session('13-11-44','bdoi','doiLowFreq','oddball_sequence') #n501
exp2.add_session('13-17-19','cdoi','doiFM_Down','oddball_sequence') #n501
exp2.add_session('13-23-47','ddoi','doiFM_Up','oddball_sequence') #n501



# 2023-05-19
# DOI & Saline

exp3 = celldatabase.Experiment(subject, '2023-05-19', brainArea='AC_right', probe='NPv1-2641', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = tip
experiments.append(exp3)

# Experiment Notes:
#  10:10 Start
#  Forgot to write time for Done
# 

exp3.maxDepth = 3000

exp3.add_site(3000) 
exp3.add_session('10-11-28','apre','prePureTones','am_tuning_curve') #n321
exp3.add_session('10-19-20','apre','preHighFreq','oddball_sequence') #n501
exp3.add_session('10-24-47','bpre','preLowFreq','oddball_sequence') #n501
exp3.add_session('10-30-16','cpre','preFM_Down','oddball_sequence') #n501
exp3.add_session('10-36-35','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.15mL" subq flank- 15min
exp3.add_session('10-42-51','aduring','','')

exp3.add_session('10-58-30','asaline','salinePureTones','am_tuning_curve') #n321
exp3.add_session('11-06-19','asaline','salineHighFreq','oddball_sequence') #n501
exp3.add_session('11-11-49','bsaline','salineLowFreq','oddball_sequence') #n501
exp3.add_session('11-17-19','csaline','salineFM_Down','oddball_sequence') #n501
exp3.add_session('11-23-45','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.15mL" subq flank 15min
exp3.add_session('11-30-01','bduring','','')

exp3.add_session('11-46-39','adoi','doiPureTones','am_tuning_curve') #n386
exp3.add_session('11-56-00','adoi','doiHighFreq','oddball_sequence') #n501
exp3.add_session('12-01-31','bdoi','doiLowFreq','oddball_sequence') #n501
exp3.add_session('12-07-01','cdoi','doiFM_Down','oddball_sequence') #n501
exp3.add_session('12-13-23','ddoi','doiFM_Up','oddball_sequence') #n501


# 2023-05-25
# DOI & Saline

exp4 = celldatabase.Experiment(subject, '2023-05-25', brainArea='AC_right', probe='NPv1-2641', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = tip
experiments.append(exp4)

# Experiment Notes:
#  14:50 Start
#  17:15 Done
# 

exp4.maxDepth = 3000

exp4.add_site(3000) 
exp4.add_session('14-55-57','apre','prePureTones','am_tuning_curve') #n321
exp4.add_session('15-03-53','apre','preHighFreq','oddball_sequence') #n501
exp4.add_session('15-09-22','bpre','preLowFreq','oddball_sequence') #n501
exp4.add_session('15-14-54','cpre','preFM_Down','oddball_sequence') #n501
exp4.add_session('15-21-19','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.15mL" subq flank- 15min
exp4.add_session('15-27-33','','salineInjection','')

exp4.add_session('15-43-31','asaline','salinePureTones','am_tuning_curve') #n321
exp4.add_session('15-51-18','asaline','salineHighFreq','oddball_sequence') #n501
exp4.add_session('15-56-46','bsaline','salineLowFreq','oddball_sequence') #n501
exp4.add_session('16-02-22','csaline','salineFM_Down','oddball_sequence') #n501
exp4.add_session('16-08-43','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.15mL" subq flank 15min
exp4.add_session('16-14-57','','doiInjection','')

exp4.add_session('16-30-37','adoi','doiPureTones','am_tuning_curve') #n321
exp4.add_session('16-38-25','adoi','doiHighFreq','oddball_sequence') #n501
exp4.add_session('16-43-53','bdoi','doiLowFreq','oddball_sequence') #n501
exp4.add_session('16-49-23','cdoi','doiFM_Down','oddball_sequence') #n501
exp4.add_session('16-55-45','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp4.add_session('17-01-57','','doiSpontaneous','')


# 2023-05-31
# DOI & Saline

exp5 = celldatabase.Experiment(subject, '2023-05-31', brainArea='AC_right', probe='NPv1-2641', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = tip
experiments.append(exp5)

# Experiment Notes:
#  12:25 Start
#  14:50 Done
 

exp5.maxDepth = 3000

exp5.add_site(3000) 
exp5.add_session('12-29-59','apre','prePureTones','am_tuning_curve') #n321
exp5.add_session('12-37-43','apre','preHighFreq','oddball_sequence') #n501
exp5.add_session('12-43-12','bpre','preLowFreq','oddball_sequence') #n501
exp5.add_session('12-48-40','cpre','preFM_Down','oddball_sequence') #n501
exp5.add_session('12-55-03','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.145mL" subq flank- 15min
exp5.add_session('13-01-14','','salineInjection','')

exp5.add_session('13-17-03','asaline','salinePureTones','am_tuning_curve') #n321
exp5.add_session('13-24-48','asaline','salineHighFreq','oddball_sequence') #n501
exp5.add_session('13-30-14','bsaline','salineLowFreq','oddball_sequence') #n501
exp5.add_session('13-35-43','csaline','salineFM_Down','oddball_sequence') #n501
exp5.add_session('13-42-07','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.145mL" subq flank 15min
exp5.add_session('13-48-19','','doiInjection','')

exp5.add_session('14-04-08','adoi','doiPureTones','am_tuning_curve') #n321
exp5.add_session('14-11-51','adoi','doiHighFreq','oddball_sequence') #n501
exp5.add_session('14-17-19','bdoi','doiLowFreq','oddball_sequence') #n501
exp5.add_session('14-22-50','cdoi','doiFM_Down','oddball_sequence') #n501
exp5.add_session('14-29-09','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp5.add_session('14-35-20','','doiSpontaneous','')


# 2023-06-14
# DOI & Saline

exp6 = celldatabase.Experiment(subject, '2023-06-14', brainArea='AC_right', probe='NPv1-2641', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = tip
experiments.append(exp6)

# Experiment Notes:
#  12:20 Start
#  14:40 Done
 

exp6.maxDepth = 3000

exp6.add_site(3000) 
exp6.add_session('12-20-12','apre','prePureTones','am_tuning_curve') #n321
exp6.add_session('12-27-59','apre','preHighFreq','oddball_sequence') #n501
exp6.add_session('12-33-46','bpre','preLowFreq','oddball_sequence') #n501
exp6.add_session('12-39-19','cpre','preFM_Down','oddball_sequence') #n501
exp6.add_session('12-45-38','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.15mL" subq flank- 15min
exp6.add_session('12-51-50','','salineInjection','')

exp6.add_session('13-07-38','asaline','salinePureTones','am_tuning_curve') #n321
exp6.add_session('13-15-23','asaline','salineHighFreq','oddball_sequence') #n501
exp6.add_session('13-20-50','bsaline','salineLowFreq','oddball_sequence') #n501
exp6.add_session('13-26-20','csaline','salineFM_Down','oddball_sequence') #n501
exp6.add_session('13-32-41','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.15mL" subq flank 15min
exp6.add_session('13-38-55','','doiInjection','')

exp6.add_session('13-54-38','adoi','doiPureTones','am_tuning_curve') #n321
exp6.add_session('14-02-22','adoi','doiHighFreq','oddball_sequence') #n517
exp6.add_session('14-08-05','bdoi','doiLowFreq','oddball_sequence') #n501
exp6.add_session('14-13-35','cdoi','doiFM_Down','oddball_sequence') #n501
exp6.add_session('14-19-55','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp6.add_session('14-26-06','','doiSpontaneous','')
