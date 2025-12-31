from jaratoolbox import celldatabase

subject = 'arch044'
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


exp0 = celldatabase.Experiment(subject, '2025-12-28', brainArea='right_pStr', probe='NPv2-3082', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp0)

# Mouse in the rig at 12:20 pm
# 14:25 took the mouse out
# Inserted the probe in the first attemp and super easy.
# Power of the laser 10 mW (Dial 5.99 / screen 52.5)
# Red part of the probe faces Medial
# Reference electrode is 3:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel. Dura-gel was so clear that i could see when the probe tauched the brain surface, it was at 1102um.
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse have a ground wire.




exp0.add_site(4720) 
exp0.maxDepth = 4720


# Shank 3 Bank A
exp0.add_session('12-29-25', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 3 Bank B
exp0.add_session('12-32-18', 'f', 'tuningFreq', 'am_tuning_curve') #40 trial

#Shanks 3 and 4. Manually selected channels 1-96 and 97-192.
exp0.add_session('12-38-17', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('12-53-21', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('13-09-27', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('13-36-34', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances



exp1 = celldatabase.Experiment(subject, '2025-12-29', brainArea='right_pStr', probe='NPv2-3082', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])

experiments.append(exp1)

# Mouse in the rig at 11:30am
# 15:25 took the mouse out
# Inserted the probe in the first attemp and super easy.
# Power of the laser 10 mW (Dial 5.99 / screen 57.8)
# Red part of the probe faces Medial
# Reference electrode is 3:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel. Dura-gel was so clear that i could see when the probe tauched the brain surface, it was at 1102um.
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse have a ground wire.




exp1.add_site(4700) 
exp1.maxDepth = 4700


# Shank 3 Bank A
exp1.add_session('11-48-21', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 3 Bank B
exp1.add_session('11-50-23', 'f', 'tuningFreq', 'am_tuning_curve') #43 trial

#Shanks 3 and 4. Manually selected channels 1-96 and 97-192.
exp1.add_session('11-53-56', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('12-59-04', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('12-09-08', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('12-36-35', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


#Shanks 3 and 4. Manually selected channels 1-96 and 97-192. The lasers shining outside of the brain. 
exp1.add_session('13-18-41', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('13-32-55', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('14-44-37', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('14-16-02', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances



exp2 = celldatabase.Experiment(subject, '2025-12-30', brainArea='left_pStr', probe='NPv2-3082', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundRight'])

experiments.append(exp2)

# Mouse in the rig at 10:40am
# Applied Vatericyn to the eye before recording with vet's recommendation. 
# 2:00pm took the mouse out
# Inserted the probe in the first attemp and super easy.
# Power of the laser 10 mW (Dial 4.9 / screen 35.4)
# Red part of the probe faces Lateral
# Reference electrode is 3:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel. 
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse have a ground wire.




exp2.add_site(4530) 
exp2.maxDepth = 4530


# Shank 3 Bank A
exp2.add_session('13-40-52', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 3 Bank B
exp2.add_session('13-43-00', 'f', 'tuningFreq', 'am_tuning_curve') #43 trial

#Shanks 3 and 4. Manually selected channels 1-96 and 97-192.
exp2.add_session('10-54-23', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('11-09-46', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('11-26-01', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('11-54-08', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#These sessions are recorded with the laset shining outside of the brain.
#Shanks 3 and 4. Manually selected channels 1-96 and 97-192.
exp2.add_session('12-18-14', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('12-34-12', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('12-50-13', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('13-17-37', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances



exp3 = celldatabase.Experiment(subject, '2025-12-31', brainArea='left_pStr', probe='NPv2-3082', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])

experiments.append(exp3)

# Mouse in the rig at 10:30am 
# 2:00pm took the mouse out
# Inserted the probe in the first attemp and super easy.
# Power of the laser 10 mW (Dial 4.9 / screen 34.6)
# Red part of the probe faces Lateral
# Reference electrode is 3:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel. 
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse have a ground wire.




exp3.add_site(4500) 
exp3.maxDepth = 4500


# Shank 3 Bank A
exp3.add_session('10-42-16', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 3 Bank B
exp3.add_session('10-44-25', 'f', 'tuningFreq', 'am_tuning_curve') #43 trial

#Shanks 3 and 4. Manually selected channels 1-96 and 97-192.
exp3.add_session('10-47-09', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp3.add_session('11-01-52', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp3.add_session('11-18-10', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp3.add_session('11-45-33', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances
