from jaratoolbox import celldatabase

subject = 'sole018'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


# 2023-08-04

exp0 = celldatabase.Experiment(subject, '2023-10-13', brainArea='AC_left', probe='NPv1-2641', recordingTrack='implant_DiD', info=['facesPosterior', 'soundRight']) #reference = tip
experiments.append(exp0)

# Experiment Notes:
#  12:01 in booth
#  12:03 started recording
#  14:20 done

exp0.maxDepth = 3000

exp0.add_site(3000)
#exp0.add_session('12-03-37','apre','prePureTones','am_tuning_curve') #n321
#exp0.add_session('12-11-52','apre','preHighFreq','oddball_sequence') #n501
#exp0.add_session('12-17-26','bpre','preLowFreq','oddball_sequence') #n501
#exp0.add_session('12-23-01','cpre','preFM_Down','oddball_sequence') #n501
#exp0.add_session('12-29-24','dpre','preFM_Up','oddball_sequence') #n501
