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
exp0.add_session('12-29-25', 'e', 'tuningFreq', 'am_tuning_curve') #41 trials

# Shank 3 Bank B
exp0.add_session('12-32-18', 'f', 'tuningFreq', 'am_tuning_curve') #40 trial

#Shanks 3 and 4. Manually selected channels 1-96 and 97-192.
exp0.add_session('12-38-17', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('12-53-21', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('13-09-27', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('13-36-34', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances






