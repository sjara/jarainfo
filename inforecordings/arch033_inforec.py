from jaratoolbox import celldatabase

subject = 'arch033'
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

# The mouse was under anesthesia around 15 min at 3 pm
# Mouse in the rig at 3:40 pm
# Red part of the probe faces lateral
# Probe in the right depth at 4:23
# Started to record at 5:16
# Reference electrode is 2:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# Power of the laser 10 mW (Dial 5.47 / screen 43.5)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# I zero the manipulator when I first touched dura-gel
# I estimated that the thickness of the duragel is 1 mm, so I went 4500 um with the manipulator, considering that the max depth in the brain is 3500 um.
# The mouse doesn't have ground wire.
# I removed some dura-gel in the corner of craniotomy and added saline to record
# I added saline before starting to record every session


exp0.add_site(3500)
exp0.maxDepth = 3500

# Shank 1 Bank A
exp0.add_session('17-15-55', 'a', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('17-26-03', 'b', 'tuningFreq', 'am_tuning_curve') #40 trials

# All shanks  1-96
exp0.add_session('17-35-45', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('17-52-10', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('18-20-59', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('18-39-40', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances 
