from jaratoolbox import celldatabase

subject = 'arch040'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])

# Reference electrode is 1:tip

#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')


exp0 = celldatabase.Experiment(subject, '2025-12-09', brainArea='right_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp0)

# Mouse in the rig at 10:32 am
# 14:25 took the mouse out
# Inserted the probe in the first attempt.
# Power of the laser 10 mW (Dial 5.49 / screen 43.7)
# Red part of the probe faces Medial
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse have a ground wire.



exp0.add_site(4500) 
exp0.maxDepth = 4500

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp0.add_session('11-28-59', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('12-38-37', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances
exp0.add_session('13-16-21', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('13-36-09', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories


# Shank 1 Bank A
exp0.add_session('13-03-20', 'c', 'tuningFreq', 'am_tuning_curve') #41 trials

# Shank 1 Bank B
exp0.add_session('13-07-39', 'd', 'tuningFreq', 'am_tuning_curve') #40 trial
