from jaratoolbox import celldatabase

subject = 'feat018'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-06-xx', brainArea='AC_right', probe='NPv1-4432', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])
# Reference electrode is the tip.
#experiments.append(expx)


#expx.add_site(3000)
#expx.maxDepth = 3000
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')

# LEFT HEMISPHERE

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-06-06', brainArea='AC_left', probe='NPv1-4662', recordingTrack='anteriorMedial_DiI', info=['facesMedial', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp0)

#9:45am moues in booth - cleaning site, a little gunky - dura removal done at 10:20am
#10:20am pia
#10:32am reached target depth, brain left to settle for 15 minutes
# After the natural sound session was completed, I opened the rig to check on feat018 before beginning AM and found that one of the mouse corral posts had fallen onto the wheel. I adjusted it and retightened it before starting AM. 
# Done at 11:38am
# Mouse began having white film develop around eyes towards the end of AM session, indicating stress

exp0.add_site(3000)
exp0.maxDepth = 3000
exp0.add_session('10-48-50', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('10-58-30', 'a', 'naturalSound', 'natural_sound_detection')
exp0.add_session('11-30-49', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2024-06-07', brainArea='AC_left', probe='NPv1-4662', recordingTrack='anteriorLateral_DiO', info=['facesLateral', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp1)

# 10:30am - probe coated, rig test, wheel spun, probe tested, mouse in booth
# Minor dura removal - mostly had to deal with some bleeding
# 11:05am pia
# 11:15am reached target depth and left brain to settle for 15 minutes
# Saw slight white film in the eye before recording 
# Lots of white film during pure tones - it cleared up by the time natural sounds begun
# Lots of squinting too, I checked to see if the mouse had a pinched whisker of if there was something making it uncomfortable, but did not notice anything
# Done at 12:22pm


exp1.add_site(3000)
exp1.maxDepth = 3000
exp1.add_session('11-31-17', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('11-42-21', 'a', 'naturalSound', 'natural_sound_detection')
exp1.add_session('12-14-11', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp2 = celldatabase.Experiment(subject, '2024-06-10', brainArea='AC_left', probe='NPv1-4662', recordingTrack='centerLateral_DiI', info=['facesLateral', 'soundRight'])

# Reference electrode is the tip.

experiments.append(exp2)
# 3:00pm mouse in booth
# 3:08pm zeroed out at pia
# 3:18pm reached target depth - brain left to settle for 15 minutes 
# Began recording at 3:35pm
# Done at 4:23pm - sylgard in place and drying at 4:28pm


exp2.add_site(3000)
exp2.maxDepth = 3000
exp2.add_session('15-35-43', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('15-46-48', 'a', 'naturalSound', 'natural_sound_detection')
exp2.add_session('16-16-14', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp3 = celldatabase.Experiment(subject, '2024-06-11', brainArea='AC_left', probe='NPv1-4662', recordingTrack='posteriorLateral_DiD', info=['facesLateral', 'soundRight'])
# Reference electrode is the tip.
experiments.append(exp3)
# In booth 9:30am
# Pia 9:50am
# Reached target depth at 9:59am no dura removal today, yay! - left brain to settle for 20 minutes
# Done at 11:06am, waiting for sylgard to dry

exp3.add_site(3000)
exp3.maxDepth = 3000
exp3.add_session('10-19-49', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('10-29-50', 'a', 'naturalSound', 'natural_sound_detection')
exp3.add_session('10-59-31', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp4 = celldatabase.Experiment(subject, '2024-06-12', brainArea='AC_left', probe='NPv1-4662', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])

# Reference electrode is the tip.
# Penetration location is in the middle of the craniotomy and slightly medial.

experiments.append(exp4)
# In booth at 9:55am
# Reached pia 10:10am - reached target depth at 10:18am - left brain to settle for 20 min
# Done at 11:26am - probe in tergazyme at 11:30 - sylgard drying 


exp4.add_site(3000)
exp4.maxDepth = 3000
exp4.add_session('10-38-59', 'a', 'pureTones', 'am_tuning_curve')
exp4.add_session('10-48-30', 'a', 'naturalSound', 'natural_sound_detection')
exp4.add_session('11-19-22', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


#exp5 = celldatabase.Experiment(subject, '2024-06-13', brainArea='AC_left', probe='NPv1-4662', recordingTrack='posteriorMedial_DiI', info=['facesMedial', 'soundRight'])
# Reference electrode is the tip.
#experiments.append(exp5)
# Probe troubleshooting at 10:30am - probe had several noisy channels, not typical of normal channel noise. Ran probe self tests and probe failed noise test - NP manual notes that this test is not indicitive of probe health so decided to continue with recording. 
# In booth at 11am and removed dura
# 11:20am pia
# 11:28am reached target depth
# Left brain to settle for 20 minutes - after grounding the probe, the channel noise got better
# #Probe stopped working in the middle of natural sound presentation - had to stop the session and the recorded data can not be used

#exp5.add_site(3000)
#exp5.maxDepth = 3000
#exp5.add_session('11-49-32', 'a', 'pureTones', 'am_tuning_curve')
#exp5.add_session('11-58-49', 'a', 'naturalSound', 'natural_sound_detection')
#exp5.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')


# RIGHT HEMISPHERE 

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp6 = celldatabase.Experiment(subject, '2024-06-14', brainArea='AC_right', probe='NPv1-4432', recordingTrack='anteriorLateral_DiI', info=['facesLateral', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp6)
# In booth 10:30am - dura removal to 10:50am
# Reached pia at 10:50am and target depth at 10:59am. Left brain to settle for 20 minutes
# Began recording at 11:20am
# Done at 12:11am

exp6.add_site(3000)
exp6.maxDepth = 3000
exp6.add_session('11-20-22', 'a', 'pureTones', 'am_tuning_curve')
exp6.add_session('11-29-39', 'a', 'naturalSound', 'natural_sound_detection')
exp6.add_session('11-58-34', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp7 = celldatabase.Experiment(subject, '2024-06-15', brainArea='AC_right', probe='NPv1-4432', recordingTrack='anteriorCenter_DiD', info=['facesMedial', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp7)

# In booth 6:20pm
# Reached pia at 6:30pm and target depth at 6:40pm - waited 15 min for the brain to settle
# This area of the brain seems to not be as active 
# Began session at 6:54pm
# Done at 7:39pm

exp7.add_site(3000)
exp7.maxDepth = 3000
exp7.add_session('18-54-57', 'a', 'pureTones', 'am_tuning_curve')
exp7.add_session('19-04-02', 'a', 'naturalSound', 'natural_sound_detection')
exp7.add_session('19-31-55', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp8 = celldatabase.Experiment(subject, '2024-06-17', brainArea='AC_right', probe='NPv1-4432', recordingTrack='centerLateral_DiD', info=['facesLateral', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp8)
# #4:07pm reached pia
# 4:16pm reached target depth and left brain to settle for 15 minutes
# Began recording at 4:31pm
# Done at 5:18pm

exp8.add_site(3000)
exp8.maxDepth = 3000
exp8.add_session('16-31-46', 'a', 'pureTones', 'am_tuning_curve')
exp8.add_session('16-42-00', 'a', 'naturalSound', 'natural_sound_detection')
exp8.add_session('17-10-49', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp9 = celldatabase.Experiment(subject, '2024-06-18', brainArea='AC_right', probe='NPv1-4432', recordingTrack='posteriorLateral_DiO', info=['facesLateral', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp9)
# Reached pia at 12:48pm 
# Reached target depth at 12:57pm and left brain to settle for 15 minutes
# Began recording at 1:13pm
# Done at 2:00pm


exp9.add_site(3000)
exp9.maxDepth = 3000
exp9.add_session('13-13-37', 'a', 'pureTones', 'am_tuning_curve')
exp9.add_session('13-23-05', 'a', 'naturalSound', 'natural_sound_detection')
exp9.add_session('13-51-35', 'b', 'AM', 'am_tuning_curve')



