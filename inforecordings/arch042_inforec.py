from jaratoolbox import celldatabase

subject = 'arch042'
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

#2025-12-08
exp0 = celldatabase.Experiment(subject, '2025-12-08', brainArea='left_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp0)

# Started habituation of the mouse at 1:37 pm
# Left mice for periods of 6 minutes in the rig and put it back in the cage (I did this 3 times)
# Mouse in the rig (after 3 times of taking it in and out) at 2:02 pm
# When I removed the sylgard, the dura-gel came out and the craniotomy started bleeding. 
# Probe in the right depth at 2:50 (First attempt)
# Power of the laser 10 mW (Dial 4.61 / screen 30.4)
# Red part of the probe faces medial
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (There was a very fine layer protecting the brain)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has ground wire.
# I added saline before starting to record every session


exp0.add_site(3700) 
exp0.maxDepth = 3700

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp0.add_session('15-14-36', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('15-30-47', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('15-59-21', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('16-16-15', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A
exp0.add_session('16-38-55', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('16-41-13', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials

#2025-12-10
exp1 = celldatabase.Experiment(subject, '2025-12-10', brainArea='right_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp1)

# Mouse in the rig at 10:07
# Probe in the right depth at 11:10
# Power of the laser 10 mW (Dial 4.98 / screen 36.1)
# Red part of the probe faces medial
# Reference electrode is 2:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (There was a very fine layer protecting the brain)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse lost the ground wire.
# I added saline before starting to record every session


exp1.add_site(3700) 
exp1.maxDepth = 3700

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp1.add_session('11-47-19', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('12-03-34', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('12-32-47', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('12-50-15', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A. Reference 1:tip
exp1.add_session('13-15-18', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp1.add_session('13-17-45', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials
