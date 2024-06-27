from jaratoolbox import celldatabase

subject = 'feat019'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-06-12', brainArea='left_AC', probe='NPv1-4662', recordingTrack='anteriormedial_DiI', info=['facesMedial', 'soundRight']) # Reference = tip.
experiments.append(exp0)

# 14:00 in booth
# 14:12 in brain
# 14:25 reached max depth
# 14:48 started recording pureTones
# 14:56 done
# 14:57 started natural sounds
# 15:23 done
# 15:24 started AM
# 15:31 done

exp0.add_site(3000)
exp0.maxDepth = 3000
exp0.add_session('14-47-58', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('14-56-59', 'a', 'naturalSound', 'natural_sound_detection')
exp0.add_session('15-24-35', 'b', 'AM', 'am_tuning_curve')


exp1 = celldatabase.Experiment(subject, '2024-06-13', brainArea='left_AC', probe='NPv1-4432', recordingTrack='posteriormedial_DiD', info=['facesMedial', 'soundRight']) # Reference = tip.
experiments.append(exp1)
# moved the penetration slightly anterior as probe would not penetrate at most posterior position

# 14:45 in booth
# 15:00 in brain
# 15:10 reached max depth
# 15:35 started recording pureTones
# 15:34 done
# 15:44 starting natural sounds
# 16:11 done
# 16:12 started AM
# 16:20 done

exp1.add_site(3000)
exp1.maxDepth = 3000
exp1.add_session('15-35-29', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('15-44-15', 'a', 'naturalSound', 'natural_sound_detection')
exp1.add_session('16-12-36', 'b', 'AM', 'am_tuning_curve')


exp2 = celldatabase.Experiment(subject, '2024-06-14', brainArea='left_AC', probe='NPv1-4432', recordingTrack='posteriorlateral_DiI', info=['facesMedial', 'soundRight']) # Reference = tip.
experiments.append(exp2)
# Originally attempted anteriorlateral_DiD penetration however the well restricts the area and the edge of the skull is much more medial than anticipated. The craniotomy looks as if it was larger than it is.
# Because of the edge of the craniotomy being closer, posteriorlateral_DiI penetration is more medial than planned

# 13:45 in booth
# 14:20 in brain
# 14:28 reached max depth
# 14:59 started recording pureTones
# 15:08 done
# 15:09 starting natural sounds
# 15:35 done
# 15:37 started AM

exp2.add_site(3000)
exp2.maxDepth = 3000
exp2.add_session('14-59-35', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('15-08-55', 'a', 'naturalSound', 'natural_sound_detection')
exp2.add_session('15-36-34', 'b', 'AM', 'am_tuning_curve')


exp3 = celldatabase.Experiment(subject, '2024-06-17', brainArea='right_AC', probe='NPv1-4432', recordingTrack='anteriormedial_DiI', info=['facesLateral', 'soundLeft']) # Reference = tip.
experiments.append(exp3)

# 10:00 in booth
# 10:12 in brain
# 10:20 reached max depth
# 10:44 started recording pureTones
# 10:51 done
# 10:52 starting natural sounds
# 11:18 done
# 11:20 started AM
# 11:27 done

exp3.add_site(3000)
exp3.maxDepth = 3000
exp3.add_session('10-43-44', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('10-52-16', 'a', 'naturalSound', 'natural_sound_detection')
exp3.add_session('11-20-19', 'b', 'AM', 'am_tuning_curve')


exp4 = celldatabase.Experiment(subject, '2024-06-18', brainArea='right_AC', probe='NPv1-4432', recordingTrack='posteriormedial_DiD', info=['facesLateral', 'soundLeft']) # Reference = tip.
experiments.append(exp4)

# 10:15 in booth
# 10:23 in brain
# 10:32 reached max depth
# 10:52 started recording pureTones
# 11:00 done
# 11:01 starting AM
# 11:28 done
# 11:29 started natural sounds 
# am_tuning.py crashed upon attempting to start so the sound began a few seconds after th other recordings were started
# 11:36 done

exp4.add_site(3000)
exp4.maxDepth = 3000
exp4.add_session('10-52-07', 'a', 'pureTones', 'am_tuning_curve')
exp4.add_session('11-01-22', 'a', 'naturalSound', 'natural_sound_detection')
exp4.add_session('11-28-57', 'b', 'AM', 'am_tuning_curve')


exp5 = celldatabase.Experiment(subject, '2024-06-19', brainArea='right_AC', probe='NPv1-4432', recordingTrack='APcenterlateral_DiO', info=['facesLateral', 'soundLeft']) # Reference = tip.
experiments.append(exp5)

# 10:18 in booth
# 10:21 in brain
# 10:29 reached max depth
# 11:00 started recording pureTones
# 11:07 done
# 11:08 starting AM
# 11:35 done
# 11:36 started natural sounds
# 11:43 done

exp5.add_site(3000)
exp5.maxDepth = 3000
exp5.add_session('11-00-18', 'a', 'pureTones', 'am_tuning_curve')
exp5.add_session('11-08-27', 'a', 'naturalSound', 'natural_sound_detection')
exp5.add_session('11-36-20', 'b', 'AM', 'am_tuning_curve')


exp6 = celldatabase.Experiment(subject, '2024-06-27', brainArea='left_AC', probe='NPv1-4272', recordingTrack='anteriorCenter_DiD', info=['facesMedial', 'soundRight']) # Reference = tip.
experiments.append(exp6)

# Pia 2:34pm
# 2:43pm reached max depth - left brain to settle for 15 min. 
# Began session at 3:00pm
# This area of the brain doesn't look very active. Ran probe self test and it failed signal but passed all others. NP manual says that the first two self tests can be ignored, so I continued with the session.
# 3:46pm done

exp6.add_site(3000)
exp6.maxDepth = 3000
exp6.add_session('15-00-15', 'a', 'pureTones', 'am_tuning_curve')
exp6.add_session('15-10-12', 'a', 'naturalSound', 'natural_sound_detection')
exp6.add_session('15-39-17', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-06-xx', brainArea='right_AC', probe='NPv1-4432', recordingTrack='posteriorlateral_DiO', info=['facesLateral', 'soundLeft']) # Reference = tip.
#experiments.append(expX)

# Pia 
#  reached max depth
# Began recording 
#  done

#expX.add_site(3000)
#expX.maxDepth = 3000
#expX.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expX.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expX.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')

