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
#The natural sounds categories does not have a recoeded video.



exp0.add_site(4500) 
exp0.maxDepth = 4500

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp0.add_session('11-28-59', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('12-38-37', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances
exp0.add_session('13-16-21', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('13-36-09', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories


# Shank 1 Bank A
exp0.add_session('13-03-20', 'c', 'tuningFreq', 'am_tuning_curve') #41 trials

# Shank 2 Bank A
exp0.add_session('13-07-39', 'd', 'tuningFreq', 'am_tuning_curve') #40 trial


exp1 = celldatabase.Experiment(subject, '2025-12-14', brainArea='right_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])

experiments.append(exp1)

# Mouse in the rig at 10:25 am
# 14:25 took the mouse out
# Inserted the probe in the first attempt (10:34am)
# Power of the laser 10 mW (Dial 5.49 / screen 44.6)
# Red part of the probe faces Medial
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse have a ground wire.
#The natural sounds categories does not have a recoeded video.



exp1.add_site(4000) 
exp1.maxDepth = 4000

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp1.add_session('10-44-47', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('11-16-21', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('11-34-30', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('12-03-28', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
#These recordings are with the laser shining outside of the brain.
exp1.add_session('12-43-01', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('12-58-01', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('13-14-33', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('13-42-24', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#The following sessions recorded with laser on and tether attached to the right optic fiber.
# Shank 1 Bank A 
exp1.add_session('14-17-21', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 2 Bank A
exp1.add_session('14-19-30', 'f', 'tuningFreq', 'am_tuning_curve') #40 trial


exp2 = celldatabase.Experiment(subject, '2025-12-16', brainArea='left_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp2)

# Mouse in the rig at 2:10 pm
#  took the mouse out
# Inserted the probe at 3:38, took me many attempts to penetrate.
# Power of the laser 10 mW (Dial 5.17 / screen 39.4)
# Red part of the probe faces Medial
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse have a ground wire.
#The natural sounds categories does not have a recoeded video.



exp2.add_site(4500) 
exp2.maxDepth = 4500

# Shank 1 Bank A 
exp2.add_session('16-01-07', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 2 Bank A
exp2.add_session('16-06-27', 'f', 'tuningFreq', 'am_tuning_curve') #40 trial

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp2.add_session('16-10-11', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('16-25-33', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('16-41-50', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('17-09-41', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


#The following sessions recorded with laser on and tether attached to the right optic fiber.
#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp2.add_session('17-41-32', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('17-57-46', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('18-14-27', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('18-42-54', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances









