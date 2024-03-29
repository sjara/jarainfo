from jaratoolbox import celldatabase

# This mouse was formerly known as 'inpi001'.

subject = 'acid006'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


# 2023-03-22
# DOI & Saline

exp0 = celldatabase.Experiment(subject, '2023-03-22', brainArea='AC_right', probe='NPv1-9691', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = ext
experiments.append(exp0)

# Experiment Notes:
#  13:25 in booth
#  13:36 started recording
#  16:00 done

exp0.maxDepth = 3000

exp0.add_site(3000) 
exp0.add_session('13-51-20','apre','prePureTones','am_tuning_curve') #n321
exp0.add_session('13-59-56','apre','preHighFreq','oddball_sequence') #n501
exp0.add_session('14-05-37','bpre','preLowFreq','oddball_sequence') #n506
exp0.add_session('14-11-25','cpre','preFM_Down','oddball_sequence') #n501
exp0.add_session('14-17-56','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.135mL" subq flank- 15min
exp0.add_session('14-24-14','aduring','','')

exp0.add_session('14-39-31','asaline','salinePureTones','am_tuning_curve') #n321
exp0.add_session('14-47-28','asaline','salineHighFreq','oddball_sequence') #n501
exp0.add_session('14-53-05','bsaline','salineLowFreq','oddball_sequence') #n501
exp0.add_session('14-58-52','csaline','salineFM_Down','oddball_sequence') #n501
exp0.add_session('15-05-22','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.135mL" subq flank 15min
exp0.add_session('15-11-39','bduring','','')

exp0.add_session('15-26-56','adoi','doiPureTones','am_tuning_curve') #n321
exp0.add_session('15-34-56','adoi','doiHighFreq','oddball_sequence') #n501
exp0.add_session('15-40-31','bdoi','doiLowFreq','oddball_sequence') #n501
exp0.add_session('15-46-07','cdoi','doiFM_Down','oddball_sequence') #n501 see note below about potential extra ephys trials
exp0.add_session('15-53-21','ddoi','doiFM_Up','oddball_sequence') #n501
# For session '15-46-07', started the next session without starting a new ephys folder. 
# Some of the new session trials were sent to ephys. Session was stopped and restarted with new ephys folder. 


# 2023-05-11
# DOI & Saline

exp1 = celldatabase.Experiment(subject, '2023-05-11', brainArea='AC_right', probe='NPv1-9691', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = ext
experiments.append(exp1)

# Experiment Notes:
#  13:25 in booth
#  13:36 started recording
#  14:54 done

exp1.maxDepth = 3000

exp1.add_site(3000)
exp1.add_session('12-45-45','apre','prePureTones','am_tuning_curve') #n321
exp1.add_session('12-54-27','apre','preHighFreq','oddball_sequence') #n501
exp1.add_session('13-00-21','bpre','preLowFreq','oddball_sequence') #n501
exp1.add_session('13-06-06','cpre','preFM_Down','oddball_sequence') #n501
exp1.add_session('13-12-35','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.14mL" subq flank- 15min
exp1.add_session('13-18-51','aduring','','')

exp1.add_session('13-34-53','asaline','salinePureTones','am_tuning_curve') #n321
exp1.add_session('13-42-45','asaline','salineHighFreq','oddball_sequence') #n501
exp1.add_session('13-48-18','bsaline','salineLowFreq','oddball_sequence') #n501
exp1.add_session('13-53-50','csaline','salineFM_Down','oddball_sequence') #n501
exp1.add_session('14-00-14','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.14mL" subq flank 15min
exp1.add_session('14-06-29','bduring','','')

exp1.add_session('14-22-28','adoi','doiPureTones','am_tuning_curve') #n321
exp1.add_session('14-30-21','adoi','doiHighFreq','oddball_sequence') #n501
exp1.add_session('14-35-57','bdoi','doiLowFreq','oddball_sequence') #n501
exp1.add_session('14-41-29','cdoi','doiFM_Down','oddball_sequence') #n501
exp1.add_session('14-47-53','ddoi','doiFM_Up','oddball_sequence') #n501



# 2023-05-18
# DOI & Saline

exp2 = celldatabase.Experiment(subject, '2023-05-18', brainArea='AC_right', probe='NPv1-9691', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = ext
experiments.append(exp2)

# Experiment Notes:
#  11:45 start
#  13:55 done

exp2.maxDepth = 3000

exp2.add_site(3000)
exp2.add_session('11-48-41','apre','prePureTones','am_tuning_curve') #n321
exp2.add_session('11-56-30','apre','preHighFreq','oddball_sequence') #n501
exp2.add_session('12-02-00','bpre','preLowFreq','oddball_sequence') #n509
exp2.add_session('12-07-46','cpre','preFM_Down','oddball_sequence') #n501
exp2.add_session('12-14-07','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.14mL" subq flank- 15min
exp2.add_session('12-20-20','aduring','','')

exp2.add_session('12-36-07','asaline','salinePureTones','am_tuning_curve') #n321
exp2.add_session('12-43-54','asaline','salineHighFreq','oddball_sequence') #n501
exp2.add_session('12-49-23','bsaline','salineLowFreq','oddball_sequence') #n501
exp2.add_session('12-54-55','csaline','salineFM_Down','oddball_sequence') #n501
exp2.add_session('13-01-18','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.14mL" subq flank 15min
exp2.add_session('13-07-30','bduring','','')

exp2.add_session('13-23-29','adoi','doiPureTones','am_tuning_curve') #n321
exp2.add_session('13-31-17','adoi','doiHighFreq','oddball_sequence') #n501
exp2.add_session('13-36-44','bdoi','doiLowFreq','oddball_sequence') #n501
exp2.add_session('13-42-17','cdoi','doiFM_Down','oddball_sequence') #n501
exp2.add_session('13-48-37','ddoi','doiFM_Up','oddball_sequence') #n501


# 2023-05-25
# DOI & Saline

exp3 = celldatabase.Experiment(subject, '2023-05-25', brainArea='AC_right', probe='NPv1-9691', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = tip
experiments.append(exp3)

# Experiment Notes:
#  12:11 start
#  14:35 done

exp3.maxDepth = 3000

exp3.add_site(3000)
exp3.add_session('12-16-57','apre','prePureTones','am_tuning_curve') #n321
exp3.add_session('12-25-20','apre','preHighFreq','oddball_sequence') #n501
exp3.add_session('12-30-55','bpre','preLowFreq','oddball_sequence') #n509
exp3.add_session('12-36-31','cpre','preFM_Down','oddball_sequence') #n501
exp3.add_session('12-42-53','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.14mL" subq flank- 15min
exp3.add_session('12-49-08','','salineInjection','')

exp3.add_session('13-05-06','asaline','salinePureTones','am_tuning_curve') #n321
exp3.add_session('13-13-00','asaline','salineHighFreq','oddball_sequence') #n501
exp3.add_session('13-18-32','bsaline','salineLowFreq','oddball_sequence') #n501
exp3.add_session('13-24-02','csaline','salineFM_Down','oddball_sequence') #n501
exp3.add_session('13-30-21','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.14mL" subq flank 15min
exp3.add_session('13-36-36','','doiInjection','')

exp3.add_session('13-52-24','adoi','doiPureTones','am_tuning_curve') #n321
exp3.add_session('14-00-24','adoi','doiHighFreq','oddball_sequence') #n501
exp3.add_session('14-05-51','bdoi','doiLowFreq','oddball_sequence') #n501
exp3.add_session('14-11-21','cdoi','doiFM_Down','oddball_sequence') #n501
exp3.add_session('14-17-40','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp3.add_session('14-23-52','','doiSpontaneous','')


# 2023-05-30
# DOI & Saline

exp4 = celldatabase.Experiment(subject, '2023-05-30', brainArea='AC_right', probe='NPv1-9691', recordingTrack='implant_DiI', info=['facesPosterior', 'soundLeft']) #reference = tip
experiments.append(exp4)

# Experiment Notes:
#  13:01 start
#  15:20 done

exp4.maxDepth = 3000

exp4.add_site(3000)
exp4.add_session('13-01-38','apre','prePureTones','am_tuning_curve') #n321
exp4.add_session('13-09-28','apre','preHighFreq','oddball_sequence') #n501
exp4.add_session('13-14-56','bpre','preLowFreq','oddball_sequence') #n501
exp4.add_session('13-20-25','cpre','preFM_Down','oddball_sequence') #n501
exp4.add_session('13-26-43','dpre','preFM_Up','oddball_sequence') #n501

#saline "0.14mL" subq flank- 15min
exp4.add_session('13-32-56','','salineInjection','')

exp4.add_session('13-49-00','asaline','salinePureTones','am_tuning_curve') #n329
exp4.add_session('13-56-59','asaline','salineHighFreq','oddball_sequence') #n501
exp4.add_session('14-02-26','bsaline','salineLowFreq','oddball_sequence') #n501
exp4.add_session('14-07-54','csaline','salineFM_Down','oddball_sequence') #n501
exp4.add_session('14-14-14','dsaline','salineFM_Up','oddball_sequence') #n501

#doi "0.14mL" subq flank 15min
exp4.add_session('14-20-27','','doiInjection','')

exp4.add_session('14-36-36','adoi','doiPureTones','am_tuning_curve') #n321
exp4.add_session('14-44-23','adoi','doiHighFreq','oddball_sequence') #n501
exp4.add_session('14-49-49','bdoi','doiLowFreq','oddball_sequence') #n501
exp4.add_session('14-55-17','cdoi','doiFM_Down','oddball_sequence') #n501 see below info 
exp4.add_session('15-01-44','ddoi','doiFM_Up','oddball_sequence') #n501

#doi spontaneous recording 10min
exp4.add_session('15-08-04','','doiSpontaneous','')

#14-55-17: saw error message in tkparadigms at end of session. "recv(42) failed: Connection reset by peer (104)"
