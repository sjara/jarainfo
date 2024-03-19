from jaratoolbox import celldatabase

subject = 'feat014'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


# Test experiment using dummy probe
# exp0 = celldatabase.Experiment(subject, '2024-02-19', brainArea='left_AC', probe='NPv1-DUMMY', recordingTrack='posteriorlateral_DiD', info=['facesMedial', 'soundRight']) # Reference = tip.

# 11:20 in booth
# 11:31 in brain
# 11:36 reached max depth
# 11:56 started recording
# 13:09 done

# exp0.add_site(1000)
# exp0.maxDepth = 1000
# exp0.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
# exp0.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')


# mistake, recorded from left_AC with sound from left instead of right
exp1 = celldatabase.Experiment(subject, '2024-02-22', brainArea='left_AC', probe='NPv1-4542', recordingTrack='APcenter-MLcenter_Na', info=['facesMedial', 'soundLeft']) # Reference = tip.
experiments.append(exp1)

# 16:30 in booth
# 16:40 in brain
# 16:49 reached max depth
# 17:10 started recording pureTones
# 17:18 done
# 17:25 starting AM
# 17:34 done

exp1.add_site(1000)
exp1.maxDepth = 1000
exp1.add_session('17-10-12', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('17-25-38', 'b', 'AM', 'am_tuning_curve')


exp2 = celldatabase.Experiment(subject, '2024-02-28', brainArea='right_AC', probe='NPv1-4542', recordingTrack='posteriorlateral_Na', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
# top electrode selected #384
experiments.append(exp2)

# 12:20 in booth
# 12:25 in brain
# 12:30 reached max depth
# 12:42 started recording pureTones
# 12:52 done
# 12:54 starting AM
# 13:01 done

exp2.add_site(2900)
exp2.maxDepth = 2900
exp2.add_session('12-41-38', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('12-54-04', 'b', 'AM', 'am_tuning_curve')


exp3 = celldatabase.Experiment(subject, '2024-02-29', brainArea='right_AC', probe='NPv1-4542', recordingTrack='APcenter-MLcenter_Na', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp3)

# 12:35 in booth
# 12:40 in brain
# 12:52 reached max depth
# 13:10 started recording pureTones
# 13:20 done
# 13:20 starting AM
# 13:29 done

exp3.add_site(3000)
exp3.maxDepth = 3000
exp3.add_session('13-10-04', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('13-20-37', 'b', 'AM', 'am_tuning_curve')


exp4 = celldatabase.Experiment(subject, '2024-03-04', brainArea='right_AC', probe='NPv1-4542', recordingTrack='anteriormedial_Na', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp4)

# 13:00 in booth
# 13:30 in brain
# 13:36 reached max depth
# 13:56 started recording pureTones
# 14:04 done
# 14:05 starting AM
# 14:12 done

exp4.add_site(3000)
exp4.maxDepth = 3000
exp4.add_session('13-55-55', 'a', 'pureTones', 'am_tuning_curve')
exp4.add_session('14-04-43', 'b', 'AM', 'am_tuning_curve')


exp5 = celldatabase.Experiment(subject, '2024-03-06', brainArea='right_AC', probe='NPv1-4542', recordingTrack='APcenter-MLcenter_DiO', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp5)

# 11:40 in booth
# 11:48 in brain
# 11:59 reached max depth
# 12:16 started recording pureTones
# 12:24 done
# 12:24 starting AM
# 12:33 done

exp5.add_site(3000)
exp5.maxDepth = 3000
exp5.add_session('12-16-32', 'a', 'pureTones', 'am_tuning_curve')
exp5.add_session('12-24-46', 'b', 'AM', 'am_tuning_curve')


exp6 = celldatabase.Experiment(subject, '2024-03-16', brainArea='left_AC', probe='NPv1-4542', recordingTrack='posteriorlateral_DiO', info=['facesAnterior', 'soundRight']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp6)

# 14:00 in booth
# 14:20 in brain
# 14:33 reached max depth
# 14:56 started recording pureTones
# 15:04 done
# 15:04 starting AM
# 15:11 done
# 15:13 started natural sounds
# 15:36 done

exp6.add_site(3000)
exp6.maxDepth = 3000
exp6.add_session('14-56-06', 'a', 'pureTones', 'am_tuning_curve')
exp6.add_session('15-04-31', 'b', 'AM', 'am_tuning_curve')
exp6.add_session('15-13-29', 'a', 'naturalSound', 'natural_sound_detection')


exp7 = celldatabase.Experiment(subject, '2024-03-18', brainArea='left_AC', probe='NPv1-4542', recordingTrack='anterior-MLcenter_DiI', info=['facesAnterior', 'soundRight']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp7)
# wheel was squeaking during recording

# 16:45 in booth
# 17:02 in brain
# 17:08 reached max depth
# 17:25 started recording pureTones
# 17:34 done
# 17:36 starting AM
# 17:43 done
# 17:44 started natural sounds
# 18:05 done

exp7.add_site(3000)
exp7.maxDepth = 3000
exp7.add_session('17-25-19', 'a', 'pureTones', 'am_tuning_curve')
exp7.add_session('17-36-07', 'b', 'AM', 'am_tuning_curve')
exp7.add_session('17-44-07', 'a', 'naturalSound', 'natural_sound_detection')


exp8 = celldatabase.Experiment(subject, '2024-03-19', brainArea='left_AC', probe='NPv1-4542', recordingTrack='anteriormedial_DiD', info=['facesAnterior', 'soundRight']) # Reference = tip.
# Check sound location with Craniotomy
experiments.append(exp8)

# 11:53 in booth
# 12:05 in brain
# 12:14 reached max depth
# 12:34 started recording pureTones
# 12:42 done
# 12:43 starting AM
# 12:50 done
# 12:56 started natural sounds
# 13:18 done

exp8.add_site(3000)
exp8.maxDepth = 3000
exp8.add_session('12-34-33', 'a', 'pureTones', 'am_tuning_curve')
exp8.add_session('12-43-05', 'b', 'AM', 'am_tuning_curve')
exp8.add_session('12-56-42', 'a', 'naturalSound', 'natural_sound_detection')


#exp9 = celldatabase.Experiment(subject, '2024-03-xx', brainArea='right_AC', probe='NPv1-4542', recordingTrack='posteriorlateral_DiD', info=['facesAnterior', 'soundLeft']) # Reference = tip.
# Check sound location with Craniotomy
#experiments.append(exp9)

#  in booth
#  in brain
#  reached max depth
#  started recording pureTones
#  done
#  starting AM
#  done
#  started natural sounds
#  done

#exp9.add_site(3000)
#exp9.maxDepth = 3000
#exp9.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#exp9.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')
#exp9.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')



