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


exp2 = celldatabase.Experiment(subject, '2022-12-15', brainArea='AC_left', probe='NPv1-4552', recordingTrack='anteriorlateral_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp2)
#  12:00 in booth
#  12:15 in brain
#  12:18 reached max depth
#  12:35 started recording
#  13:10 IP Injection. 
#  13:50 done

exp2.add_site(3050)
exp2.maxDepth = 3050
exp2.add_session('12-35-30','apre','pureTones','am_tuning_curve')
exp2.add_session('12-44-42','apre','highFreq','oddball_sequence')
exp2.add_session('12-50-28','bpre','lowFreq','oddball_sequence')
exp2.add_session('12-56-21','cpre','FM_Down','oddball_sequence')
exp2.add_session('13-02-57','dpre','FM_Up','oddball_sequence')
#saline 0.1mL IP
exp2.add_session('13-13-31','apost','pureTones','am_tuning_curve')
exp2.add_session('13-21-33','apost','highFreq','oddball_sequence')
exp2.add_session('13-27-17','bpost','lowFreq','oddball_sequence')
exp2.add_session('13-33-05','cpost','FM_Down','oddball_sequence')
exp2.add_session('13-40-40','dpost','FM_Up','oddball_sequence')


exp3 = celldatabase.Experiment(subject, '2022-12-15', brainArea='AC_left', probe='NPv1-4552', recordingTrack='posteriorlateral_DiD', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp3)
#  12:00 in booth
#  12:15 in brain
#  12:18 reached max depth
#  12:35 started recording
#  13:10 IP Injection. 
#  : done

exp3.add_site()
exp3.maxDepth = 
exp3.add_session('--','bpre','pureTones','am_tuning_curve')
exp3.add_session('--','epre','highFreq','oddball_sequence')
exp3.add_session('--','fpre','lowFreq','oddball_sequence')
exp3.add_session('--','gpre','FM_Down','oddball_sequence')
exp3.add_session('--','hpre','FM_Up','oddball_sequence')
#saline 0.1mL IP
exp3.add_session('--','bpost','pureTones','am_tuning_curve')
exp3.add_session('--','epost','highFreq','oddball_sequence')
exp3.add_session('--','fpost','lowFreq','oddball_sequence')
exp3.add_session('--','gpost','FM_Down','oddball_sequence')
exp3.add_session('--','hpost','FM_Up','oddball_sequence')

