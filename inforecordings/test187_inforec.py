from jaratoolbox import celldatabase

subject = 'test187'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])

# Reference electrode is 4:tip

#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')



exp0 = celldatabase.Experiment(subject, '2025-10-07', brainArea='right_pStr', probe='NPv2-3813', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundLeft'])

experiments.append(exp0)

# Reference electrode is 3:tip
# Targeting right pStr
# Probe is located in the center of craniotomy facing the midline
# All shanks active 1-96, except the second shank (We selected more electrodes from shank 4 instead)
# Left brain to ettle for a long time >2 hours
#According to the software, shank 1 is at 3540 depth, shank 3 is at 3585 and shank 4 at 3615.
#Depth is 3502.4  according to the manipulator

exp0.add_site(3502)
exp0.maxDepth = 3502
#exp0.add_session('13-26-44', 'a', 'pureTones', 'am_tuning_curve') #140 trials(No the correct amount of trials)
#exp0.add_session('13-42-15', 'b', 'AM', 'am_tuning_curve') #I forgot to save the stimulus h5 file and no correct amount of trials
exp0.add_session('13-56-04', 'c', 'pureTones', 'am_tuning_curve') #File with 320 trials - Good
exp0.add_session('14-10-45', 'd', 'AM', 'am_tuning_curve') #File with 220 trials - Good

