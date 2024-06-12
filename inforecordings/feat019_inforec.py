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


#exp1 = celldatabase.Experiment(subject, '2024-06-xx', brainArea='left_AC', probe='NPv1-4662', recordingTrack='anteriorlateral_DiD', info=['facesMedial', 'soundRight']) # Reference = tip.
#experiments.append(exp1)

#  in booth
#  in brain
#  reached max depth
#  started recording pureTones
#  done
#  starting AM
#  done
#  started natural sounds
#  done

#exp1.add_site(3000)
#exp1.maxDepth = 3000
#exp1.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#exp1.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#exp1.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')



