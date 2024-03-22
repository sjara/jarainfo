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


#exp2 = celldatabase.Experiment(subject, '2024-03-xx', brainArea='left_AC', probe='NPv1-4542', recordingTrack='posteriorlateral_DiD', info=['facesAnterior', 'soundRight']) # Reference = tip.
# Check sound location with Craniotomy
#experiments.append(exp2)

#  in booth
#  in brain
#  reached max depth
#  started recording pureTones
#  done
#  starting AM
#  done
#  started natural sounds
#  done

#exp2.add_site(3000)
#exp2.maxDepth = 3000
#exp2.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#exp2.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')
#exp2.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')

