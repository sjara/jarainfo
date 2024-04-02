from jaratoolbox import celldatabase

subject = 'feat017'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-xx-xx', brainArea='AC_xxx', probe='NPv1-4542', recordingTrack='medialxxx_DYE', info=['facesxx', 'soundxxx'])
# Reference electrode is the tip.
#experiments.append(expx)


#expx.add_site(3000)
#expx.maxDepth = 3000
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-03-25', brainArea='AC_left', probe='NPv1-4542', recordingTrack='anteriorCenter_DiO', info=['facesPosterior', 'soundRight'])

# Reference electrode is the tip.
experiments.append(exp0)
# 2:40pm - max depth brain left to settle for 20 minutes
# 3:02pm pure tones start
# 3:15pm start AM sounds 
# 3:24pm - start natural sounds 


exp0.add_site(3000)
exp0.maxDepth = 3000
exp0.add_session('15-03-11', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('15-15-32', 'b', 'AM', 'am_tuning_curve')
exp0.add_session('15-25-02', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2024-03-26', brainArea='AC_left', probe='NPv1-4542', recordingTrack='anteriorLateral_DiL', info=['facesAnterior', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp1)
# Target depth reached 2:04pm - waited 20 minutes for brain to settle
# Started pure tones at 2:24pm 
# Started AM 2:36pm
# Started natural sounds at 2:46pm 


exp1.add_site(3000)
exp1.maxDepth = 3000
exp1.add_session('14-23-56', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('14-35-57', 'b', 'AM', 'am_tuning_curve')
exp1.add_session('14-46-38', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp2 = celldatabase.Experiment(subject, '2024-03-27', brainArea='AC_left', probe='NPv1-4542', recordingTrack='AnteriorMedial_DiD', info=['facesMedial', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp2)

# 11:18am reached target depth - brain left to settle for twenty minutes
# 11:41am start pure tones
# 11:51am started AM
# 12:01pm started natural sounds 


exp2.add_site(3000)
exp2.maxDepth = 3000
exp2.add_session('11-41-02', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('11-50-26', 'b', 'AM', 'am_tuning_curve')
exp2.add_session('12-00-31', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp3 = celldatabase.Experiment(subject, '2024-03-29', brainArea='AC_left', probe='NPv1-4542', recordingTrack='posteriorLateral_DiO', info=['facesMedial', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp3)
# Some troubleshooting with the lights today - whiskers were oversaturated and we had to cover another camera led
# start pure tones at 11:29am
# start AM at 11:38am
# start natural sounds at 11:48am


exp3.add_site(3000)
exp3.maxDepth = 3000
exp3.add_session('11-28-04', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('11-38-09', 'b', 'AM', 'am_tuning_curve')
exp3.add_session('11-48-21', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp4 = celldatabase.Experiment(subject, '2024-04-01', brainArea='AC_Left', probe='NPv1-4542', recordingTrack='medialCenter_DiI', info=['facesPosterior' 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp4)
# Some troubleshooting with the video contrast again today - covered all leds on the camera to get rid of issues with contrast
# Noticed the mouse was squinting a lot randomly? Not sure why. I checked it's eyes to see if there was something stuck but didn't see anything. Mouse also didn't display other signs of distress so I don't think it was in pain. 
# Started pure tones 3:38pm
# Started AM sounds 3:53pm
# Started natural sounds 4:05pm
# Done 4:48pm


exp4.add_site(3000)
exp4.maxDepth = 3000
exp4.add_session('15-41-23', 'a', 'pureTones', 'am_tuning_curve')
exp4.add_session('15-52-49', 'b', 'AM', 'am_tuning_curve')
exp4.add_session('16-04-55', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp5 = celldatabase.Experiment(subject, '2024-04-02', brainArea='AC_left', probe='NPv1-4542', recordingTrack='medialPosterior_DiO', info=['facesPosterior', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp5)

# 10:07am reached max depth brain left to settle for 20 minutes
# Start pure tones 10:26am
# Start AM 10:35am
# Start natural sounds 10:45am
# Done - mouse in cage 


exp5.add_site(3200)
exp5.maxDepth = 3200
exp5.add_session('10-26-02', 'a', 'pureTones', 'am_tuning_curve')
exp5.add_session('10-35-25', 'b', 'AM', 'am_tuning_curve')
exp5.add_session('10-45-32', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.
