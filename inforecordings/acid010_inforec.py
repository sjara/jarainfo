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



