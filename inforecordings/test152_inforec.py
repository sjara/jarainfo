from jaratoolbox import celldatabase

subject = 'test152'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-12-xx', brainArea='right_AC', probe='NPv2-1392', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])
# Reference electrode is the tip.
#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')

# LEFT HEMISPHERE

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-12-11', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerCenter_DiI', info=['facesAnterior', 'soundLeft'])

# Reference electrode is the 1: Tip.
# Electrodes 97-192 active
# Went down in the brain 1500 microns
# Used an angle of 64 degrees with respect to the horizontal axis and a 60 degree azimuth angle - this was done accidentally
# Attempting to hit AUDp

experiments.append(exp0)


exp0.add_site(780)
exp0.maxDepth = 1500
exp0.add_session('18-23-00', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('19-31-01', 'a', 'naturalSound', 'natural_sound_detection')
exp0.add_session('19-58-43', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2024-12-12', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerMedial_DiO', info=['facesPosterior', 'soundLeft'])

# Reference electrode is the 4: Tip.
# Electrodes 1-96 active
# Went down in the brain 1500 microns
# Used an angle of 40 degrees with respect to the horizontal axis and a 60 degree azimuth angle
# Left brain to settle for 15 min.
# Attempting to hit AUDd

experiments.append(exp1)


exp1.add_site(1500)
exp1.maxDepth = 1500
exp1.add_session('17-12-29', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('17-24-37', 'a', 'naturalSound', 'natural_sound_detection')
exp1.add_session('17-52-25', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp2 = celldatabase.Experiment(subject, '2024-12-18', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerLateral_DiI', info=['facesLateral', 'soundLeft'])

# Reference electrode is the 1: Tip.
# Electrodes 97-192 active
# Went down in the brain 1500 microns
# The head bar holder was adjusted further left in the rig in order to be able to record from the side of the mouse at a 85 degree azmiuth angle. 
# Used an angle of 52 degrees with respect to the horizontal axis and a 90 degree azimuth angle
# Left brain to settle for 15 min.
# Still looks pretty noisy after ground wire was implanted.
# For third recording with AM, mouse eye was covered in a white film. Washed it out with saline before proceding with the recording. 
# Attempting to hit AUDv
# When trying out ways to reduce noise, we found that grounding the head plate holder to the probe ground wire appears to help - we grounded the head plate after the sessions for the day were recorded

experiments.append(exp2)

exp2.add_site(750)
exp2.maxDepth = 1500
exp2.add_session('12-31-03', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('12-40-46', 'a', 'naturalSound', 'natural_sound_detection')
exp2.add_session('13-08-57', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp3 = celldatabase.Experiment(subject, '2024-12-19', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerLateral_DiD', info=['facesMedial', 'soundLeft'])

# Note that this recording was more medial than the previous one.
# Reference electrode is the 1: Tip.
# Adjusted wheel and head plate holder further down in order for the manipulator arm to reach higher up in the craniotomy, where as during the recording before, the manipulator could not reach unless the angle of the arm was adjusted with respect to the horizontal axis. 
# Full range of motion for the up and down axis on maniuplator arm - currently z - is ~5094 microns
# The larger post used before was 38 mm - switched to smaller one that was 25 mm. Probe and manipulator is able to reach all places in craniotomy now
# Recorded with an angle of 32.5 with respect to the horizontal axis; 90 degree azimuth angle
# Electrodes 97-192 active
# Went down 2500 microns
# This is the first session with grounded head plate and adjusted head plate holder and wheel 

experiments.append(exp3)


exp3.add_site(1250)
exp3.maxDepth = 2500
exp3.add_session('15-09-57', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('15-19-34', 'a', 'naturalSound', 'natural_sound_detection')
exp3.add_session('15-47-21', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp4 = celldatabase.Experiment(subject, '2024-12-20', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerCenter_noDye', info=['facesLateral', 'soundLeft'])

# Removed Dura-Gel and performed test with saline in well
# Reference electrode is the 1: Tip.
# Went down in the brain 2900 microns
# Recorded with an angle of 32.5 with respect to the horizontal axis; 90 degree azimuth angle
# Minor dura removal 
experiments.append(exp4)
exp4.maxDepth = 2900

# Channel 268 displayed the best sound responsive neurons
# Electrodes 1-96 active
exp4.add_site(2900)
exp4.add_session('16-29-03', 'a', 'AM', 'am_tuning_curve')

# Reference electrode is the 1: Tip.
# Shank A Bank 4 all 
exp4.add_site(2901)
exp4.add_session('16-39-44', 'a', 'AM', 'am_tuning_curve')


