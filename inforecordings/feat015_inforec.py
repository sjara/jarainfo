from jaratoolbox import celldatabase

subject = 'feat015'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2024-xx-xx', brainArea='AC_right', probe='NPv1-4542', recordingTrack='medialxxx_DYE', info=['facesxx', 'soundLeft'])
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

exp0 = celldatabase.Experiment(subject, '2024-02-23', brainArea='AC_right', probe='NPv1-4542', recordingTrack='posteriorlateral_na', info=['facesAnterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp0)
# 12:52 sylgard removed added saline
# 1:02 attached headstage
# 1:06 probe to pia
# 1:09 probe in brain and added saline
# 1:18 reached target depth
# 1:37 15 minutes for brain to settle

exp0.add_site(1100)
exp0.maxDepth = 1100
exp0.add_session('13-38-29', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('13-51-22', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2024-02-27', brainArea='AC_right', probe='NPv1-4542', recordingTrack='posteriorMedial_DiI', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp1)
# Dil dye used - electrode inserted posterior and to the left of the craniotomy
# Removed dura 11:30am
# 11:50am probe to pia
# 11:53am probe in brain and added saline
# 11:57am reached target depth
# 11:58am 20 minutes for brain to settle

exp1.add_site(2900)
exp1.maxDepth = 2900
exp1.add_session('12-19-12', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('12-31-30', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp2 = celldatabase.Experiment(subject, '2024-02-28', brainArea='AC_right', probe='NPv1-4542', recordingTrack='anteriorMedial_DiO', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp2)
# DiO dye used - electrode inserted anterior and to the left of the craniotomy
#  probe to pia 6:00pm
#  probe in brain and added saline
#  6:30pm reached target depth
#  6:35pm 15 minutes for brain to settle

exp2.add_site(1700)
exp2.maxDepth = 1700
exp2.add_session('18-48-54', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('18-59-42', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp3 = celldatabase.Experiment(subject, '2024-03-01', brainArea='AC_right', probe='NPv1-4542', recordingTrack='posteriorCenter_DiD', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp3)

# DiD dye used - electrode inserted posterior and middle of the craniotomy
#  11:44am probe to pia 
#  11:50am probe in brain and added saline 
#  reached target depth 11:58am and set 15 minutes for brain to settle

exp3.add_site(3500)
exp3.maxDepth = 3500
exp3.add_session('12-20-12', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('12-33-34', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp4 = celldatabase.Experiment(subject, '2024-03-06', brainArea='AC_right', probe='NPv1-4542', recordingTrack='medialCenter_DiO', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp4)

# 4:22pm started pure tones 
# 4:58pm done and mouse in cage

exp4.add_site(3000)
exp4.maxDepth = 3000
exp4.add_session('16-20-44', 'a', 'pureTones', 'am_tuning_curve')
exp4.add_session('16-31-52', 'b', 'AM', 'am_tuning_curve')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


exp5 = celldatabase.Experiment(subject, '2024-03-20', brainArea='AC_right', probe='NPv1-4542', recordingTrack='lateralAnterior_DiI', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp5)
#10:30am set 20 timer for brain to settle 
#probe manipulator got stuck at 2413.3 and couldn't go further down
# night mode flickered in and out. Covered one of the camera lights - 3 originally were uncovered, and this appeared to fix the issue for the time being.
 #pure tones started at 11:05am - disovered there was something wrong with the left speaker - this recording is NULL
 # pure tones started at 12:16pm - 352 trials
 # AM started at 12:26pm - 250 trials
# Natural sounds started 12:38pm
# NOTE: the behavior file will report that the sound was presented to the right side but it was presented LEFT. This is because we had to switch out the left speaker cable for the right. 
 # 1:10pm done
 
exp5.add_site(2413)
exp5.maxDepth = 2413
exp5.add_session('12-15-53', 'a', 'pureTones', 'am_tuning_curve')
exp5.add_session('12-26-13', 'b', 'AM', 'am_tuning_curve')
exp5.add_session('12-37-25', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp6 = celldatabase.Experiment(subject, '2024-03-21', brainArea='AC_right', probe='NPv1-4542', recordingTrack='centerCenter_DiO', info=['facesPosterior', 'soundLeft'])
# Reference electrode is the tip.
experiments.append(exp6)

# NOTE: The sound was mistakenly presented to both sides of the mouse rather than contralateral to the recording site.

# Minor dura removal 
# 11:45am pure tones done
# 11:55am AM tones done
# 12:22pm natural sounds done

exp6.add_site(3000)
exp6.maxDepth = 3000
exp6.add_session('11-36-34', 'a', 'pureTones', 'am_tuning_curve')
exp6.add_session('11-47-33', 'b', 'AM', 'am_tuning_curve')
exp6.add_session('11-58-36', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp7 = celldatabase.Experiment(subject, '2024-03-22', brainArea='AC_right', probe='NPv1-4542', recordingTrack='anteriorCenter_DiD', info=['facesanterior', 'soundLeft'])


# Reference electrode is the tip.
experiments.append(exp7)
# minor dura removal
# 3:38pm reached target depth and let brain settle for 15 min
# Brain looks a little worse for wear - today will be the last day I record with this mouse
# pure tones start 4:00pm
# AM start 4:12pm

exp7.add_site(3000)
exp7.maxDepth = 3000
exp7.add_session('16-01-05', 'a', 'pureTones', 'am_tuning_curve')
exp7.add_session('16-12-22', 'b', 'AM', 'am_tuning_curve')
exp7.add_session('16-27-30', 'a', 'naturalSound', 'natural_sound_detection')

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.


