from jaratoolbox import celldatabase

subject = 'feat016'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp0 = celldatabase.Experiment(subject, '2024-03-21', brainArea='left_AC', probe='NPv1-4542', recordingTrack='anteriormedial_DiI', info=['facesAnterior', 'soundRight']) # Reference = tip.
experiments.append(exp0)

# 13:50 in booth
# 13:58 in brain
# 14:06 reached max depth
# 14:27 started recording pureTones
# 14:35 done
# 14:37 starting AM
# 14:44 done
# 14:45 started natural sounds
# 15:06 done

exp0.add_site(3000)
exp0.maxDepth = 3000
exp0.add_session('14-27-23', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('14-37-04', 'b', 'AM', 'am_tuning_curve')
exp0.add_session('14-45-47', 'a', 'naturalSound', 'natural_sound_detection')


exp1 = celldatabase.Experiment(subject, '2024-03-22', brainArea='left_AC', probe='NPv1-4542', recordingTrack='posteriormedial_DiD', info=['facesAnterior', 'soundRight']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp1)

# 10:23 in booth
# 10:29 in brain
# 10:33 reached max depth
# 10:55 started recording pureTones
# 11:02 done
# 11:04 starting AM
# 11:12 done
# 11:12 started natural sounds
# 11:33 done

exp1.add_site(3000)
exp1.maxDepth = 3000
exp1.add_session('10-54-55', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('11-04-27', 'b', 'AM', 'am_tuning_curve')
exp1.add_session('11-12-25', 'a', 'naturalSound', 'natural_sound_detection')


exp2 = celldatabase.Experiment(subject, '2024-03-23', brainArea='left_AC', probe='NPv1-4542', recordingTrack='APcenterMLCenter_DiO', info=['facesAnterior', 'soundRight']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp2)

# 11:22 in booth
# 11:29 in brain
# 11:33 reached max depth
# 11:53 started recording pureTones
# 12:00 done
# 12:02 starting AM
# 12:09 done
# 12:11 started natural sounds
# 12:32 done

exp2.add_site(3000)
exp2.maxDepth = 3000
exp2.add_session('11-53-21', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('12-02-35', 'b', 'AM', 'am_tuning_curve')
exp2.add_session('12-11-24', 'a', 'naturalSound', 'natural_sound_detection')


exp3 = celldatabase.Experiment(subject, '2024-03-24', brainArea='left_AC', probe='NPv1-4542', recordingTrack='posteriorlateral_DiI', info=['facesAnterior', 'soundRight']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp3)

# 13:14 in booth
# 13:20 in brain
# 13:25 reached max depth
# 13:45 started recording pureTones
# 13:52 done
# 13:53 starting AM
# 14:00 done
# 14:01 started natural sounds
# 14:22 done

exp3.add_site(3000)
exp3.maxDepth = 3000
exp3.add_session('13-45-06', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('13-53-09', 'b', 'AM', 'am_tuning_curve')
exp3.add_session('14-01-23', 'a', 'naturalSound', 'natural_sound_detection')


exp4 = celldatabase.Experiment(subject, '2024-04-04', brainArea='right_AC', probe='NPv1-4542', recordingTrack='posteriormedial_DiO', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp4)

# 14:40 in booth
# 15:00 in brain
# 15:08 reached max depth
# 15:41 started recording pureTons
# 15:50 done
# 15:50 starting AM
# 15:57 done
# 15:58 started natural sounds
# 16:18 done

exp4.add_site(3000)
exp4.maxDepth = 3000
exp4.add_session('15-41-39', 'a', 'pureTones', 'am_tuning_curve')
exp4.add_session('15-50-05', 'b', 'AM', 'am_tuning_curve')
exp4.add_session('15-58-13', 'a', 'naturalSound', 'natural_sound_detection')


exp5 = celldatabase.Experiment(subject, '2024-03-08', brainArea='right_AC', probe='NPv1-4542', recordingTrack='anteriorlateral_DiD', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp5)

# 10:45 in booth
# 11:20 in brain
# 11:27 reached max depth
# 11:50 started recording pureTones
# 11:57 done
# 11:59 starting AM
# 12:06 done
# 12:09 started natural sounds
# 12:30 done

exp5.add_site(3000)
exp5.maxDepth = 3000
exp5.add_session('11-50-23', 'a', 'pureTones', 'am_tuning_curve')
exp5.add_session('11-58-58', 'b', 'AM', 'am_tuning_curve')
exp5.add_session('12-08-59', 'a', 'naturalSound', 'natural_sound_detection')


exp6 = celldatabase.Experiment(subject, '2024-04-09', brainArea='right_AC', probe='NPv1-2141', recordingTrack='anteriormedial_DiI', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp6)

# 13:15 in booth
# 13:30 in brain
# 13:39 reached max depth
# 13:59 started recording pureTones
# 14:07 done
# 14:07 starting AM 
# 14:15 done (went to 260 rather than target 220 trails by mistake)
# 14:18 started natural sounds
# 14:40 done

exp6.add_site(3000)
exp6.maxDepth = 3000
exp6.add_session('13-59-11', 'a', 'pureTones', 'am_tuning_curve')
exp6.add_session('14-07-39', 'b', 'AM', 'am_tuning_curve')
exp6.add_session('14-18-43', 'a', 'naturalSound', 'natural_sound_detection')


exp7 = celldatabase.Experiment(subject, '2024-04-10', brainArea='right_AC', probe='NPv1-2141', recordingTrack='posteriorlateral_DiI', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp7)

# 15:47 in booth
# 16:15 in brain
# 16:25 reached max depth
# 16:46 started recording pureTones
# 16:54 done
# 16:55 starting AM
# 17:02 done
# 17:03 started natural sounds
# 17:24 done

exp7.add_site(3000)
exp7.maxDepth = 3000
exp7.add_session('16-46-04', 'a', 'pureTones', 'am_tuning_curve')
exp7.add_session('16-55-05', 'b', 'AM', 'am_tuning_curve')
exp7.add_session('17-03-11', 'a', 'naturalSound', 'natural_sound_detection')


exp8 = celldatabase.Experiment(subject, '2024-04-11', brainArea='right_AC', probe='NPv1-2141', recordingTrack='APcentermedial_DiD', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp8)

# 13:18 in booth
# 13:42 in brain
# 13:50 reached max depth
# 14:14 started recording pureTones
# 14:22 done
# 14:22 starting AM
# 14:30 done
# 14:32 started natural sounds
# 14:53 done

exp8.add_site(3000)
exp8.maxDepth = 3000
exp8.add_session('14-14-16', 'a', 'pureTones', 'am_tuning_curve')
exp8.add_session('14-22-56', 'b', 'AM', 'am_tuning_curve')
exp8.add_session('14-32-22', 'a', 'naturalSound', 'natural_sound_detection')


exp9 = celldatabase.Experiment(subject, '2024-04-12', brainArea='right_AC', probe='NPv1-2141', recordingTrack='APcenterlateral_DiO', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp9)

# 13:28 in booth
# 14:00 in brain
# 14:08 reached max depth
# 14:30 started recording pureTones
# 14:38 done
# 14:38 starting AM
# 14:45 done
# 14:47 started natural sounds
# 15:09 done

exp9.add_site(3000)
exp9.maxDepth = 3000
exp9.add_session('14-30-24', 'a', 'pureTones', 'am_tuning_curve')
exp9.add_session('14-38-47', 'b', 'AM', 'am_tuning_curve')
exp9.add_session('14-47-25', 'a', 'naturalSound', 'natural_sound_detection')



exp10 = celldatabase.Experiment(subject, '2024-04-17', brainArea='left_AC', probe='NPv1-2141', recordingTrack='anteriorlateral_DiD', info=['facesAnterior', 'soundRight']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp10)

# 10:55 in booth
# 11:02 in brain
# 11:10 reached max depth
# 11:30 started recording pureTones
# 11:38 done
# 11:39 starting AM
# 11:45 done
# 11:47 started natural sounds
# 12:09 done

exp10.add_site(3000)
exp10.maxDepth = 3000
exp10.add_session('11-30-12', 'a', 'pureTones', 'am_tuning_curve')
exp10.add_session('11-38-52', 'b', 'AM', 'am_tuning_curve')
exp10.add_session('11-47-47', 'a', 'naturalSound', 'natural_sound_detection')

