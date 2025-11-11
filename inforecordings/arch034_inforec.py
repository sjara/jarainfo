from jaratoolbox import celldatabase

subject = 'arch034'
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


exp0 = celldatabase.Experiment(subject, '2025-10-27', brainArea='left_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundRight'])

experiments.append(exp0)

# Mouse in the rig at 12:53 pm
# Started habituation of the mouse
# 1:09 took the mouse out
# Mouse in the rig at 1:11
# 1:14 took the mouse out
# Mouse in the rig at 1:16
# Probe in the right depth at 2:23 (First attempt)
# Power of the laser 10 mW (Dial 5.25 / screen 40.8)
# Red part of the probe faces lateral
# Started to record at 2:56
# Reference electrode is 2:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# When I removed the sylgard, the dura-gel came out so I could start penetrating from the surface of the brain
# I zero the manipulator when I first touched dura-gel
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse doesn't have ground wire.
# I added saline before starting to record every session


exp0.add_site(3500) #3500.4
exp0.maxDepth = 3500

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp0.add_session('14-56-11', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('17-52-10', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('18-20-59', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('18-39-40', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A
exp0.add_session('17-15-55', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('17-26-03', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials
