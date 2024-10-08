from jaratoolbox import celldatabase

subject = 'feat017'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-xx-xx', brainArea='xxx_AC', probe='NPv1-2141', recordingTrack='medialxxx_DYE', info=['facesxx', 'soundxxx'])
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

exp0 = celldatabase.Experiment(subject, '2024-03-25', brainArea='left_AC', probe='NPv1-4542', recordingTrack='anteriorCenter_DiO', info=['facesPosterior', 'soundRight'])

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

exp1 = celldatabase.Experiment(subject, '2024-03-26', brainArea='left_AC', probe='NPv1-4542', recordingTrack='anteriorLateral_DiI', info=['facesAnterior', 'soundRight'])
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

exp2 = celldatabase.Experiment(subject, '2024-03-27', brainArea='left_AC', probe='NPv1-4542', recordingTrack='anteriorMedial_DiD', info=['facesMedial', 'soundRight'])
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

exp3 = celldatabase.Experiment(subject, '2024-03-29', brainArea='left_AC', probe='NPv1-4542', recordingTrack='posteriorLateral_DiO', info=['facesMedial', 'soundRight'])
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

exp4 = celldatabase.Experiment(subject, '2024-04-01', brainArea='left_AC', probe='NPv1-4542', recordingTrack='centerMedial_DiI', info=['facesPosterior' 'soundRight'])
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

exp5 = celldatabase.Experiment(subject, '2024-04-02', brainArea='left_AC', probe='NPv1-4542', recordingTrack='posteriorMedial_DiO', info=['facesPosterior', 'soundRight'])
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

exp6 = celldatabase.Experiment(subject, '2024-04-03', brainArea='left_AC', probe='NPv1-4542', recordingTrack='posteriorCenter_DiI', info=['facesPosterior', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp6)
# Reached target depth at 10:30am - left brain to settle for 20 minutes 
# Start pure tone at 10:51am
#  Start AM at 11:01am
# Start natural sounds at 11:10am


exp6.add_site(3300)
exp6.maxDepth = 3300
exp6.add_session('10-50-56', 'a', 'pureTones', 'am_tuning_curve')
exp6.add_session('11-01-14', 'b', 'AM', 'am_tuning_curve')
exp6.add_session('11-10-44', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp7 = celldatabase.Experiment(subject, '2024-04-04', brainArea='left_AC', probe='NPv1-4542', recordingTrack='centerCenter_DiD', info=['facesPosterior', 'soundRight'])
# Reference electrode is the tip.
# Recording track center-center but favors lateral
experiments.append(exp7)

# Reached target depth and brain left to settle for 30 min at 10:27am
# Start pure tones at 10:59am
# Start AM sounds at 11:08am
# Start natural sounds at 11:17am - done at 11:40am


exp7.add_site(3200)
exp7.maxDepth = 3200
exp7.add_session('10-58-26', 'a', 'pureTones', 'am_tuning_curve')
exp7.add_session('11-08-34', 'b', 'AM', 'am_tuning_curve')
exp7.add_session('11-17-22', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#exp8 = celldatabase.Experiment(subject, '2024-04-05', brainArea='right_AC', probe='NPv1-4542', recordingTrack='anteriorLateral_DiD', info=['facesLateral', 'soundLeft'])
# Reference electrode is the tip.

#experiments.append(exp8)
# Reached target depth at 10:45am - left brain to settle for 20 min
# Start pure tones 11:06am
# Start AM 11:17am
# Start natural sounds 11:26am
# Done - sylgard in well 12:00pm
# NOTE: After the recording was finished, we realized the data drive ran out of space during the natural sounds session. Meaning we can't use the natural sounds for this experiment. 


#exp8.add_site(3000)
#exp8.maxDepth = 3000
#exp8.add_session('11-06-17', 'a', 'pureTones', 'am_tuning_curve')
#exp8.add_session('11-17-06', 'b', 'AM', 'am_tuning_curve')
#exp8.add_session('11-26-26', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp9 = celldatabase.Experiment(subject, '2024-04-08', brainArea='right_AC', probe='NPv1-2141', recordingTrack='centerLateral_DiO', info=['facesLateral', 'soundLeft'])
# Reference electrode is the tip.
# Had some troubleshooting with probe 4542 and had to switch it out - brain left to settle at 3:57pm
# Start pure tones at 4:17pm
# Start AM at 4:26pm
# Start natural sounds at 4:35pm

experiments.append(exp9)

exp9.add_site(3000)
exp9.maxDepth = 3000
exp9.add_session('16-16-47', 'a', 'pureTones', 'am_tuning_curve')
exp9.add_session('16-26-10', 'b', 'AM', 'am_tuning_curve')
exp9.add_session('16-35-07', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp10 = celldatabase.Experiment(subject, '2024-04-09', brainArea='right_AC', probe='NPv1-2141', recordingTrack='posteriorLateral_DiI', info=['facesMedial', 'soundLeft'])

# Reference electrode is the tip.
# Reached target depth at 10:40am - left brain to settle for 30 min
# Started pure tones at 11:09am
# Started AM at 11:18am
# Started natural sounds at 11:27am


experiments.append(exp10)


exp10.add_site(3005)
exp10.maxDepth = 3005
exp10.add_session('11-09-23', 'a', 'pureTones', 'am_tuning_curve')
exp10.add_session('11-18-36', 'b', 'AM', 'am_tuning_curve')
exp10.add_session('11-27-50', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp11 = celldatabase.Experiment(subject, '2024-04-10', brainArea='right_AC', probe='NPv1-2141', recordingTrack='anteriorCenter_DiI', info=['facesLateral', 'soundLeft'])
# Reference electrode is the tip.

experiments.append(exp11)
# Camera continues to randomly switch between day and night mode - pushing the cover sensor down seems to help 
# Started pure tones 10:37am after letting brain settle for 15 min
# Start AM 10:48am
# Start natural sounds 10:58am


exp11.add_site(3000)
exp11.maxDepth = 3000
exp11.add_session('10-37-28', 'a', 'pureTones', 'am_tuning_curve')
exp11.add_session('10-48-29', 'b', 'AM', 'am_tuning_curve')
exp11.add_session('10-58-06', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp12 = celldatabase.Experiment(subject, '2024-04-11', brainArea='right_AC', probe='NPv1-2141', recordingTrack='centerCenter_DiD', info=['facesAnterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp12)
# Start pure tones at 10:53am
# Start AM at 11:03am
# Start natural sounds at 11:13am

exp12.add_site(3000)
exp12.maxDepth = 3000
exp12.add_session('10-53-21', 'a', 'pureTones', 'am_tuning_curve')
exp12.add_session('11-03-07', 'b', 'AM', 'am_tuning_curve')
exp12.add_session('11-13-58', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp13 = celldatabase.Experiment(subject, '2024-04-12', brainArea='right_AC', probe='NPv1-2141', recordingTrack='posteriorCenter_DiO', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp13)
# 10:20 reached target depth and left brain to settle for 15 min
# Start pure tones at 10:44am
# Start AM at 10:53am
# Start natural sounds at 11:03am

exp13.add_site(3000)
exp13.maxDepth = 3000
exp13.add_session('10-44-14', 'a', 'pureTones', 'am_tuning_curve')
exp13.add_session('10-53-32', 'b', 'AM', 'am_tuning_curve')
exp13.add_session('11-03-41', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp14 = celldatabase.Experiment(subject, '2024-04-15', brainArea='right_AC', probe='NPv1-2141', recordingTrack='anteriorMedial_DiO', info=['facesLateral', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp14)
# Inserted probe anterior-medial as much as possible but the medial side of the well was very close to the probe and I was worried there may be damage to the probe, so the probe is a bit closer to the center of craniotomy. 
# Some bleeding and dura removal
# Brain left to settle for 20 min at 10:06am
# Start pure tones at 10:27am
# Start AM at 10:36am
# Start natural sounds at 10:45am

exp14.add_site(3000)
exp14.maxDepth = 3000
exp14.add_session('10-27-00', 'a', 'pureTones', 'am_tuning_curve')
exp14.add_session('10-36-55', 'b', 'AM', 'am_tuning_curve')
exp14.add_session('10-45-54', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp15 = celldatabase.Experiment(subject, '2024-04-16', brainArea='right_AC', probe='NPv1-2141', recordingTrack='centerMedial_DiI', info=['facesMedial', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp15)
# Reached target depth at 10:15am - left brain to settle for 30 min
# Probe inserted medial-center and a bit anterior since the medial-posterior side of the well is in the way of the probe 
# Lots of bleeding when removing dura today
# Start pure tones 10:45am
# Start AM at 10:54am
# Start natural sounds 11:03am


exp15.add_site(3000)
exp15.maxDepth = 3000
exp15.add_session('10-45-07', 'a', 'pureTones', 'am_tuning_curve')
exp15.add_session('10-54-51', 'b', 'AM', 'am_tuning_curve')
exp15.add_session('11-03-08', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.
