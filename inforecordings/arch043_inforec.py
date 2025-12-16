from jaratoolbox import celldatabase

subject = 'arch043'
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

#2025-12-15
exp0 = celldatabase.Experiment(subject, '2025-12-15', brainArea='left_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp0)

# Started habituation of the mouse at 12:45 pm
# Left mice for periods of 8 minutes in the rig and put it back in the cage (I did this 3 times)
# Mouse in the rig (after 3 times of taking it in and out) at 1:28 pm
# Probe in the right positioning at 2:08 pm (First attempt)
# Power of the laser 10 mW (Dial 5.74 / screen 48)
# Red part of the probe faces medial
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (1 mm tick)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has ground wire.


exp0.add_site(4500) 
exp0.maxDepth = 4500

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp0.add_session('14-33-46', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('14-48-36', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('15-16-12', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('15-32-44', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A
exp0.add_session('15-57-46', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('16-00-58', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials
