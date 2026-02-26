from jaratoolbox import celldatabase

subject = 'arch045'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])

# Reference electrode is 3:tip

#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')


exp0 = celldatabase.Experiment(subject, '2026-02-24', brainArea='right_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp0)

#Mouse in the rig at 11:57am
#Probe inserted at 12:30pm
#The data was very noisy I think because the ground wire fell, but not compeletely so it is probably touching the head bar creating a loop, I used the saline well wire.
#Took the mouse out at 5:00 pm




exp0.add_site(4000) 
exp0.maxDepth = 4000


# Shank 3 Bank A
exp0.add_session('16-54-44', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 3 Bank B
exp0.add_session('16-59-35', 'f', 'tuningFreq', 'am_tuning_curve') #40 trial

#Recording from all shanks, channels 1-96.
exp0.add_session('13-44-52', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('14-05-01', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('14-24-52', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('14-54-49', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Recoeding from all shanks, channels 97-192.
exp0.add_session('15-27-33', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('15-43-40', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('16-01-07', 'c', 'optoNaturalCategories', 'natural_sound_detection') #212 OptoNaturalCategories
exp0.add_session('16-32-18', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


