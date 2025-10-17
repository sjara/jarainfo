from jaratoolbox import celldatabase

subject = 'arch032'
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

#Bank 1-96
exp0 = celldatabase.Experiment(subject, '2025-10-16', brainArea='right_pStr', probe='NPv2-1134', recordingTrack='centerCenter', info=['facesMedial', 'soundLeft'])

experiments.append(exp0)

#Mouse in the rig at 10 am
#Probe in the right depth at 10:49. Waited 40 minutes for the brain to settle.
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of craniotomy facing the midline
# All shanks active 1-96
#According to the software, shanks were around 3460 depth
#Depth is 3500.3  according to the manipulator (Manipulator set to 0 when we touched the duragel)
#Power of the laser 10 mW

exp0.add_site(3500)
exp0.maxDepth = 3500
exp0.add_session('11-42-45', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('12-05-27', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('12-36-01', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('12-57-58', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances 


#Bank 97-192
exp1 = celldatabase.Experiment(subject, '2025-10-16', brainArea='right_pStr', probe='NPv2-1134', recordingTrack='centerCenter', info=['facesMedial', 'soundLeft'])

experiments.append(exp1)

# Reference electrode is 1:tip

exp1.add_site(2780)
exp1.maxDepth = 3500
exp1.add_session('13-28-22', 'c', 'optoTuningAM', 'am_tuning_curve')#440
exp1.add_session('13-46-27', 'c', 'optoNaturalCategoriesnaturalSound', 'natural_sound_detection') #200
exp1.add_session('14-21-21', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('14-39-05', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 
