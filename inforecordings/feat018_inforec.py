from jaratoolbox import celldatabase

subject = 'feat018'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-06-xx', brainArea='AC_xxx', probe='NPv1-4662', recordingTrack='medialxxx_DYE', info=['facesxx', 'soundxxx'])
# Reference electrode is the tip.
#experiments.append(expx)


#expx.add_site(3000)
#expx.maxDepth = 3000
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')

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





