from jaratoolbox import celldatabase

subject = 'arch023'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-02-xx', brainArea='right_AC', probe='NPv2-1392', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])
# Reference electrode is 1:tip
#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'optoTuningFreq', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'optoNaturalCategories', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'optoTuningAM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2025-03-05', brainArea='right_AC', probe='NPv2-1392', recordingTrack='anteriorLateral_DiD', info=['facesAnterior', 'soundLeft'])

# Dura-Gel
# Reference electrode is 1:tip.
# Left brain to settle for 30 minutes
# Used an 80 degree angle for the optical fiber with respect to the horizontal plane
# 80 degrees for the optic fiber angle makes it really challenging to insert the probe, not a lot of space
# Optic fiber is 2000um deep
# Shank 1 Bank A active 
# Seeing most activity towards the tip of the probe 
# Laser: 5mW
 

experiments.append(exp0)

exp0.add_site(2500)
exp0.maxDepth = 2500
exp0.add_session('18-19-43', 'a', 'optoTuningFreq', 'am_tuning_curve')
exp0.add_session('18-30-34', 'a', 'optoNaturalCategorie', 'natural_sound_detection')
exp0.add_session('18-58-47', 'b', 'optoTuningAM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2025-03-06', brainArea='right_AC', probe='NPv2-1392', recordingTrack='anteriorLateral_DiI', info=['facesAnterior', 'soundLeft'])
# This recording is more towards the center of the craniotomy than the recording on 2025-03-05
# Dura-Gel
# Left brain to settle for 15 minutes
# Used an 70 degree angle for the optical fiber with respect to the horizontal plane
# Optic fiber is 1000um deep
# Laser: 10mW
experiments.append(exp1)
exp1.maxDepth = 2500

# Shank 1 Bank A active 
# Seeing most activity towards the tip of the probe, low noise 
# Reference electrode is 1:tip.
exp1.add_site(2500)
exp1.add_session('15-39-07', 'a', 'optoTuningFreq', 'am_tuning_curve')
exp1.add_session('15-47-39', 'a', 'optoNaturalCategorie', 'natural_sound_detection')
exp1.add_session('16-14-56', 'b', 'optoTuningAM', 'am_tuning_curve')

# Shank 2 Bank A active 
# Shank 2 is super noisy pretty much all throughout the channels 
# Reference electrode is 1:tip.
exp1.add_site(2501)
exp1.add_session('16-24-26', 'a', 'optoTuningFreq', 'am_tuning_curve')
exp1.add_session('16-33-31', 'a', 'optoNaturalCategorie', 'natural_sound_detection')
exp1.add_session('17-01-07', 'b', 'optoTuningAM', 'am_tuning_curve')


# Shank 3 Bank A active 
# Shank 3 is a bit less noisy than shank 2 - I can see spikes on some of the channels ~1900 inside the brain
# Reference electrode is 1:tip.
exp1.add_site(2502)
exp1.add_session('17-09-05', 'a', 'optoTuningFreq', 'am_tuning_curve')
exp1.add_session('17-18-06', 'a', 'optoNaturalCategorie', 'natural_sound_detection')
exp1.add_session('17-46-38', 'b', 'optoTuningAM', 'am_tuning_curve')


# Shank 4 Bank A active 
# This shank is fairly noisy as well but I can see spikes on some channels
# Reference electrode is 1:tip.
exp1.add_site(2503)
exp1.add_session('17-54-26', 'a', 'optoTuningFreq', 'am_tuning_curve')
exp1.add_session('18-03-39', 'a', 'optoNaturalCategorie', 'natural_sound_detection')
exp1.add_session('18-31-24', 'b', 'optoTuningAM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp2 = celldatabase.Experiment(subject, '2025-03-12', brainArea='right_AC', probe='NPv2-3544', recordingTrack='anteriorMedial_DiD', info=['facesAnterior', 'soundLeft'])

# Dura removal - used saline for this recording
# Left brain to settle for 15 minutes
# Used an 75 degree angle for the optical fiber with respect to the horizontal plane
# Optic fiber is 1000um deep
# Laser: 10mW
# It was a lot easier to record today without Dura-Gel - seems like it is easier to see where we are without it 
experiments.append(exp2)
exp2.maxDepth = 2500

# Shank 1 Bank A active 
# Reference electrode is 1:tip.
exp2.add_site(2500)
exp2.add_session('12-52-17', 'a', 'optoTuningAM', 'am_tuning_curve')
exp2.add_session('12-59-59', 'b', 'optoTuningFreq', 'am_tuning_curve')


# Reference electrode is 1:tip.
# Shank 2 Bank A active 
exp2.add_site(2501)
exp2.add_session('13-09-06', 'a', 'optoTuningAM', 'am_tuning_curve')
exp2.add_session('13-16-28', 'b', 'optoTuningFreq', 'am_tuning_curve')


# Shank 3 Bank A active 
# Reference electrode is 1:tip.
exp2.add_site(2502)
exp2.add_session('13-26-05', 'a', 'optoTuningAM', 'am_tuning_curve')
exp2.add_session('13-33-50', 'b', 'optoTuningFreq', 'am_tuning_curve')


# Shank 4 Bank A active 
# Reference electrode is 1:tip.
exp2.add_site(2503)
exp2.add_session('13-44-24', 'a', 'optoTuningAM', 'am_tuning_curve')
exp2.add_session('13-51-53', 'b', 'optoTuningFreq', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


