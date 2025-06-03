from jaratoolbox import celldatabase

subject = 'wifi008'
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



exp0 = celldatabase.Experiment(subject, '2025-05-28', brainArea='right_AC', probe='NPv2-5422', recordingTrack='posteriorCenter_DiD', info=['facesPosterior', 'soundLeft'])

experiments.append(exp0)

# Reference electrode is 3:tip
# 58 degrees with respect to the horizontal axis
# 83 degrees with respect to the azimuth axis
# Targeting A1
# Probe is located posterior center leaning medial
# All shanks active 1-96
# It continues to be challenging to see when we enter pia with the current camera set up
# We originally went to 1500um deep in the brain but did not see much neural actiity so we decided to go further into the brain 
# Left brain to settle for 15 minutes

exp0.add_site(2000)
exp0.maxDepth = 2000
exp0.add_session('11-35-03', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('11-45-48', 'a', 'naturalSound', 'natural_sound_detection')
exp0.add_session('12-13-35', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


exp1 = celldatabase.Experiment(subject, '2025-05-29', brainArea='right_AC', probe='NPv2-0282', recordingTrack='anteriorLateral_DiD', info=['facesPosterior', 'soundLeft'])

# Reference electrode is 4:tip
# Recording with shank 4
# Targeting AAF
# 70 degrees with respect to the horizontal axis
# 60 degrees with respect to the azimuth axis
# Lots of dura removal 

experiments.append(exp1)

exp1.add_site(1500)
exp1.maxDepth = 1500
exp1.add_session('17-18-25', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('17-28-25', 'a', 'naturalSound', 'natural_sound_detection')
exp1.add_session('17-58-12', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp2 = celldatabase.Experiment(subject, '2025-05-30', brainArea='right_AC', probe='NPv2-1134', recordingTrack='posteriorLateral_DiI', info=['facesPosterior', 'soundLeft'])

# All shanks 97-192
# Reference electrode is 1:tip
# Targeting ventral
# Dura removal - lots of gunk covering the craniotomy and bone that need to be removed in order to see the markings made and insert the probe.
# Dish was not long enough - mouse was still able to reach the original probe with 2 shanks and it broke. We added a 3rd extension to the dish to shield the probe from the mouse. We also extended the corral bars so that they could also be used to block the mouse from reaching the probe. 
# 57.5 degrees with respect to the horizontal axis
# 64 degrees with respect to the azimuth axis 


experiments.append(exp2)


exp2.add_site(780)
exp2.maxDepth = 1500
exp2.add_session('14-13-36', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('14-23-35', 'a', 'naturalSound', 'natural_sound_detection')
exp2.add_session('14-54-33', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


exp3 = celldatabase.Experiment(subject, '2025-05-30', brainArea='right_AC', probe='NPv2-1134', recordingTrack='anteriorLateral_DiI', info=['facesPosterior', 'soundLeft'])

# Reference electrode is 1:tip

experiments.append(exp3)

exp3.add_site(1500)
exp3.maxDepth = 1500
exp3.add_session('17-12-01', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('17-21-30', 'b', 'AM', 'am_tuning_curve')




