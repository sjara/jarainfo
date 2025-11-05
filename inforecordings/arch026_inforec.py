from jaratoolbox import celldatabase

subject = 'arch026'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])

#experiments.append(expx)

# Reference electrode is 4:tip

#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'optoTuningAM', 'am_tuning_curve') #440
#expx.add_session('xx-xx-xx', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
#expx.add_session('xx-xx-xx', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#expx.add_session('xx-xx-xx', 'a', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# October 24th

exp0 = celldatabase.Experiment(subject, '2025-10-24', brainArea='left_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp0)

# Reference electrode is 1:tip
# Mouse in the rig at 1:21
# Probe at the desired depth at 2:11
# Waited for the brain to settle for around 1 hour
# In the "Neuropix PXI" tab in Open Ephys, while looking at the "Probe signal", in shank 1 Bank B  we can see difference on the electrodes from Y position above 5055 and below that. Electrodes above 5055 look yellowish while electrodes below that look blue  (we think that is the transition from duragel to the air)
# The manipulator depth is 4500.
# I zero the manipulator when I touched the duragel, and I estimated together with Sara and Santiago that the thickness of the layer is about 1 mm, so ideally there is 3500 distance from the surface of the brain till the tip of the electrodes.
#I think the change from dura to brain is around Y position 3120
# Rig test done
# Laser turned on at 3:30
# Dial 5.01 and screen 36.6

exp0.add_site(3500)
exp0.maxDepth = 3500
# Shank 1 Bank A
exp0.add_session('15-17-20', 'a', 'tuningFreq', 'am_tuning_curve') #40 trials Bank A, no video. Session to check LFP only

# Shank 1 Bank B
exp0.add_session('15-22-00', 'b', 'tuningFreq', 'am_tuning_curve') #40 trials Bank B, no video. Session to check LFP only

# All shanks  1-96
exp0.add_session('15-37-07', 'c', 'optoTuningAM', 'am_tuning_curve') #No enough trials (400 trials)
exp0.add_session('15-52-23', 'd', 'optoTuningAM', 'am_tuning_curve') #440 trials
exp0.add_session('16-08-28', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 trials OptoNaturalCategories
exp0.add_session('16-38-18', 'e', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#exp0.add_session('xx-xx-xx', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 trials OptoNaturalInstances. Sometihng weird happened and the ephys data for this session was not saved
exp0.add_session('17-22-27', 'c', 'optoNaturalInstances', 'natural_sound_detection')  #160 trials OptoNaturalInstances.

# October 28th

exp1 = celldatabase.Experiment(subject, '2025-10-28', brainArea='right_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp1)

# Reference electrode is 4:tip
# I zero the manipulator when I touched the duragel, and I estimated that the thickness of the layer is about 1 mm, so ideally there is 3500 distance from the surface of the brain till the tip of the electrodes.

exp1.add_site(4500)
exp1.maxDepth = 4500
#All shanks 1-96
#exp1.add_session('12-31-48', 'a', 'tuningFreq', 'am_tuning_curve') #Around 325 trials.

# All shanks  1-96
exp1.add_session('13-32-21', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('13-54-04', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('13-08-49', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('14-26-50', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160

# Shank 1 Bank A
exp1.add_session('15-13-38', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp1.add_session('15-16-28', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials
