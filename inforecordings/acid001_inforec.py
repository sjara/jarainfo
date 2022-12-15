from jaratoolbox import celldatabase

subject = 'acid001'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2022-12-13', brainArea='AC_left', probe='NPv1-4161', recordingTrack='anteromedial_DiD', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp0)
#  13:40 in booth
#  13:48 in brain
#  13:50 reached max depth
#  14:08 started recording
#  15:55 done

exp0.add_site(3000)
exp0.maxDepth = 3000
exp0.add_session('14-08-13','a','pureTones','am_tuning_curve')
exp0.add_session('14-18-58','a','highFreq','oddball_sequence')
exp0.add_session('14-27-59','b','lowFreq','oddball_sequence')
exp0.add_session('14-59-18','c','FM_Down','oddball_sequence')
exp0.add_session('15-09-32','d','FM_Up','oddball_sequence')
#saline 0.1mL IP
exp0.add_session('15-20-48','b','pureTones','am_tuning_curve')
exp0.add_session('15-29-45','e','highFreq','oddball_sequence')
exp0.add_session('15-35-50','f','lowFreq','oddball_sequence')
exp0.add_session('15-43-47','g','FM_Down','oddball_sequence')
exp0.add_session('15-50-26','h','FM_Up','oddball_sequence')
# probe was found broken at the end of session.


exp1 = celldatabase.Experiment(subject, '2022-12-14', brainArea='AC_left', probe='NPv1-4552', recordingTrack='posteriormedial_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp1)
#  14:04 in booth
#  14:14 in brain
#  14:15 reached max depth
#  14:43 started recording
#  15:17 IP Injection. During injection, lots of blood came from injection site. 	Bleeding stopped on its own and blood was cleaned.
#  11:58 done

exp1.add_site(3100)
exp1.maxDepth = 3100
exp1.add_session('14-43-56','apre','pureTones','am_tuning_curve')
exp1.add_session('14-53-51','apre','highFreq','oddball_sequence')
exp1.add_session('14-59-55','bpre','lowFreq','oddball_sequence')
exp1.add_session('15-06-02','cpre','FM_Down','oddball_sequence')
exp1.add_session('15-12-56','dpre','FM_Up','oddball_sequence')
#saline 0.1mL IP
exp1.add_session('15-25-37','apost','pureTones','am_tuning_curve')
exp1.add_session('15-33-55','apost','highFreq','oddball_sequence')
exp1.add_session('15-39-46','bpost','lowFreq','oddball_sequence')
exp1.add_session('15-46-27','cpost','FM_Down','oddball_sequence')
exp1.add_session('15-53-00','dpost','FM_Up','oddball_sequence')


