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

#2025-10-29
exp1 = celldatabase.Experiment(subject, '2025-10-29', brainArea='right_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundLeft'])

experiments.append(exp1)

# Mouse in the rig at 10:25 am
# Red part of the probe faces lateral
# Probe in the right depth at 11:32
# Started to record at 11:53
# Reference electrode is 2:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# Power of the laser 10 mW (Dial 6.02 / screen 52.9)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# I zero the manipulator when I first touched dura-gel
# I estimated that the thickness of the duragel is 1 mm, so I went 4500 um with the manipulator, considering that the max depth in the brain is 3500 um.
# The mouse doesn't have ground wire.
# I removed some dura-gel in the corner of craniotomy and added saline to record
# I added saline before starting to record every session


exp1.add_site(3500)
exp1.maxDepth = 3500

# All shanks  1-96
exp1.add_session('11-53-24', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('12-11-01', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('12-40-51', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('12-58-43', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A
exp1.add_session('13-21-17', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp1.add_session('13-23-49', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials


#2025-10-30
exp2 = celldatabase.Experiment(subject, '2025-10-30', brainArea='right_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])

experiments.append(exp2)

# The cage of the mouse was full of water everywhere. It seems like the bag of water broke.
# I changed the cage, and waited for some time because the temperature of the mouse was low.
# Mouse in the rig at 10:30 am
# Red part of the probe faces medial
# Probe in the right depth at 12:05
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# Power of the laser 10 mW (Dial 6.02 / screen 52.2)
# I zero the manipulator when I touched the surface of the brain (Removed dura-gel layer)
# I added saline before starting to record every session
# The mouse doesn't have ground wire.

exp2.add_site(3500)
exp2.maxDepth = 3500 #3500.1

# All shanks  1-96
exp2.add_session('12-18-56', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('12-35-57', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('13-05-56', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('13-23-38', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

