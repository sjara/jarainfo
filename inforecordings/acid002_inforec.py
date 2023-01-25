from jaratoolbox import celldatabase

subject = 'acid002'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2023-01-14', brainArea='AC_left', probe='NPv1-4552', recordingTrack='posteriormedial_DiI', info=['facesMedial', 'soundRight']) #reference = tip
experiments.append(exp0)
#  14:04 in booth
#  14:14 in brain
#  14:15 reached max depth
#  14:43 started recording
#  11:58 done

exp0.add_site(3100)
exp0.maxDepth = 3100
exp0.add_session('14-43-56','apre','prePureTones','am_tuning_curve')
# Injection Method 001
exp0.add_session('14-43-56','apost','postPureTones','am_tuning_curve')

exp0.add_site(3101)
exp0.add_session('14-43-56','bpre','prePureTones','am_tuning_curve')
# Injection Method 001
exp0.add_session('14-43-56','bpost','postPureTones','am_tuning_curve')

exp0.add_site(3102)
exp0.add_session('14-43-56','cpre','prePureTones','am_tuning_curve')
# Injection Method 001
exp0.add_session('14-43-56','cpost','postPureTones','am_tuning_curve')

#exp0.add_session('14-53-51','apre','highFreq','oddball_sequence')
#exp0.add_session('14-59-55','bpre','lowFreq','oddball_sequence')
#exp0.add_session('15-06-02','cpre','FM_Down','oddball_sequence')
#exp0.add_session('15-12-56','dpre','FM_Up','oddball_sequence')
#saline 0.1mL IP
#exp0.add_session('15-25-37','apost','pureTones','am_tuning_curve')
#exp0.add_session('15-33-55','apost','highFreq','oddball_sequence')
#exp0.add_session('15-39-46','bpost','lowFreq','oddball_sequence')
#exp0.add_session('15-46-27','cpost','FM_Down','oddball_sequence')
#exp0.add_session('15-53-00','dpost','FM_Up','oddball_sequence')


