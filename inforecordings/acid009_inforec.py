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

