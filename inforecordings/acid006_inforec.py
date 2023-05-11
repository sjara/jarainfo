from jaratoolbox import celldatabase

# This mouse was formerly known as 'inpi001'.

subject = 'acid006'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


# 2023-03-22
# DOI & Saline

exp0 = celldatabase.Experiment(subject, '2023-03-22', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp0)

# Experiment Notes:
#  13:25 in booth
#  13:36 started recording
#  16:00 done

exp0.maxDepth = 3000

exp0.add_site(3000) # reference: tip
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
exp0.add_session('15-46-07','cdoi','doiFM_Down','oddball_sequence') #n501 may be extra ephys trials at the end
exp0.add_session('15-53-21','ddoi','doiFM_Up','oddball_sequence') #n501


# 2023-05-11
# DOI & Saline

exp1 = celldatabase.Experiment(subject, '2023-05-11', brainArea='AC_right', probe='NPv1-9691', recordingTrack='??? ', info=['faces ???', 'soundLeft']) #reference = (see sites)
experiments.append(exp1)

# Experiment Notes:
#  13:25 in booth
#  13:36 started recording
#  14:54 done

exp1.maxDepth = 3000

exp1.add_site(3000) # reference: tip
exp1.add_session('12-45-56','apre','prePureTones','am_tuning_curve') #n321
exp1.add_session('12-54-28','apre','preHighFreq','oddball_sequence') #n501
exp1.add_session('13-00-21','bpre','preLowFreq','oddball_sequence') #n506
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

exp1.add_session('14-22-29','adoi','doiPureTones','am_tuning_curve') #n321
exp1.add_session('14-30-21','adoi','doiHighFreq','oddball_sequence') #n501
exp1.add_session('14-35-57','bdoi','doiLowFreq','oddball_sequence') #n501
exp1.add_session('14-41-29','cdoi','doiFM_Down','oddball_sequence') #n501
exp1.add_session('14-47-53','ddoi','doiFM_Up','oddball_sequence') #n501

