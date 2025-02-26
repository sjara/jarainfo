from jaratoolbox import celldatabase

subject = 'test164'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-02-xx', brainArea='right_AC', probe='NPv2-1392', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])
# Reference electrode is 1:tip
#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

expX = celldatabase.Experiment(subject, '2025-02-11', brainArea='right_AC', probe='NPv2-1392', recordingTrack='posteriorMedial_DiI', info=['facesLateral', 'soundLeft'])

# Dura-Gel
# Reference electrode is 1:tip.
# Left brain to settle for 15 minutes
# Used a 32.5 angle with respect to the horizontal plane
# Used a 90 degree angle with respect to the azimuth plane
# Channels 1-96 active
# Probe is oriented to face lateral but at a slight angle (see animal wiki page for image)
# Aiming for AH
# I am seeing neural activity towards channel 1 of probe, but it is hard to tell if I am going deep enough into the brain due to the well and Dura-Gel limiting visual ability - the neural activity appears to not be sound dependent/ related
# Went down 1000um originally but forgot to take into account the bone thickness - bone thickness in this area is ~275um.  
# Very little noise and big spikes 

experiments.append(exp0)

exp0.add_site(725)
exp0.maxDepth = 725
exp0.add_session('16-57-39', 'a', 'pureTones', 'am_tuning_curve')
exp0.add_session('17-07-50', 'a', 'naturalSound', 'natural_sound_detection')
exp0.add_session('17-34-59', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp1 = celldatabase.Experiment(subject, '2025-02-13', brainArea='right_AC', probe='NPv2-1392', recordingTrack='posteriorMedial_DiD', info=['facesLateral', 'soundLeft'])

# Dura-Gel
# Reference electrode is 1:tip
# Left brain to settle for 15 minutes
# Used a 32.5 angle with respect to the horizontal plane
# Used a 90 degree angle with respect to the azimuth plane
# Channels 97-192 active
# Probe is oriented to face lateral but at a slight angle (see animal wiki page for image)
# Aiming for AH
# Penetration is also lower down (ventral) in the craniotomy than the previous penetration
# Litle noise and small spikes (hard to tell if they are sound responsive)

experiments.append(exp1)

exp1.add_site(780)
exp1.maxDepth = 1500
exp1.add_session('15-29-55', 'a', 'pureTones', 'am_tuning_curve')
exp1.add_session('15-38-57', 'a', 'naturalSound', 'natural_sound_detection')
exp1.add_session('16-06-11', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

# 2025-02-17 unable to penetrate the surfce of the brain with probe
# 2025-02-18 dura removal
# 2025-02-19 dura removal and trimmed down well

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp2 = celldatabase.Experiment(subject, '2025-02-19', brainArea='right_AC', probe='NPv2-1392', recordingTrack='anteriorCenter_DiI', info=['facesLateral', 'soundLeft'])

# Saline in well
# Reference electrode is 1:tip
# Channels 193-288 active
# Left brain to settle for 30 min
# Used a 40 angle with respect to the horizontal plane
# Used a 90 degree angle with respect to the azimuth plane
# Targeting AH and AAF
# Mouse eye is very squinty - noticed some issues with its foot earlier but it appeared to be walking fine - mouse also had eye lube on during tissue removal today which is why the mouse face appears wet
# Mouse was sqeaking a lot when placed in rig

experiments.append(exp2)


exp2.add_site(2000)
exp2.maxDepth = 1440
exp2.add_session('17-41-34', 'a', 'pureTones', 'am_tuning_curve')
exp2.add_session('17-50-14', 'a', 'naturalSound', 'natural_sound_detection')
exp2.add_session('18-17-48', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp3 = celldatabase.Experiment(subject, '2025-02-20', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerLateral_DiD', info=['facesPosterior', 'soundLeft'])

# Saline in well
# Reference electrode is 1:tip
# Shank 1 Bank A active
# Left brain to settle for 20 minutes
# Targeing VAF and A2
# Used a 32.5 angle with respect to the horizontal plane
# Used a 90 degree angle with respect to the azimuth plane
# It was pretty challening to see when the probe penetrated the surface of the brain 

experiments.append(exp3)

exp3.add_site(2000)
exp3.maxDepth = 2000
exp3.add_session('11-58-01', 'a', 'pureTones', 'am_tuning_curve')
exp3.add_session('12-07-42', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp4 = celldatabase.Experiment(subject, '2025-02-20', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerLateral_DiD', info=['facesPosterior', 'soundLeft'])

# Saline in well
# Reference electrode is 1:tip
# Shank 2 Bank A active
# Left brain to settle for 20 minutes
# Targeing VAF and A2
# Used a 32.5 angle with respect to the horizontal plane
# Used a 90 degree angle with respect to the azimuth plane
# It was pretty challening to see when the probe penetrated the surface of the brain 

experiments.append(exp4)

exp4.add_site(2000)
exp4.maxDepth = 2000
exp4.add_session('12-15-54', 'a', 'pureTones', 'am_tuning_curve')
exp4.add_session('12-24-30', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp5 = celldatabase.Experiment(subject, '2025-02-20', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerLateral_DiD', info=['facesPosterior', 'soundLeft'])

# Saline in well
# Reference electrode is 1:tip
# Shank 3 Bank A active
# Left brain to settle for 20 minutes
# Targeing VAF and A2
# Used a 32.5 angle with respect to the horizontal plane
# Used a 90 degree angle with respect to the azimuth plane
# It was pretty challening to see when the probe penetrated the surface of the brain 

experiments.append(exp5)

exp5.add_site(2000)
exp5.maxDepth = 2000
exp5.add_session('12-32-59', 'a', 'pureTones', 'am_tuning_curve')
exp5.add_session('12-41-40', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp6 = celldatabase.Experiment(subject, '2025-02-20', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerLateral_DiD', info=['facesPosterior', 'soundLeft'])

# Saline in well
# Reference electrode is 1:tip
# Shank 4 Bank A active
# Left brain to settle for 20 minutes
# Targeing VAF and A2
# Used a 32.5 angle with respect to the horizontal plane
# Used a 90 degree angle with respect to the azimuth plane
# It was pretty challening to see when the probe penetrated the surface of the brain # It was pretty challening to see when the probe penetrated the surface of the brain 

experiments.append(exp6)

exp6.add_site(2000)
exp6.maxDepth = 2000
exp6.add_session('12-49-40', 'a', 'pureTones', 'am_tuning_curve')
exp6.add_session('12-58-43', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp7 = celldatabase.Experiment(subject, '2025-02-20', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerLateral_DiD', info=['facesPosterior', 'soundLeft'])

# Saline in well
# Reference electrode is 1:tip
# All shanks bank 97-192 active
# Left brain to settle for 20 minutes
# Targeing VAF and A2
# Used a 32.5 angle with respect to the horizontal plane
# Used a 90 degree angle with respect to the azimuth plane
# It was pretty challening to see when the probe penetrated the surface of the brain # It was pretty challening to see when the probe penetrated the surface of the brain 
# The longer the mouse was in the rig, the more his eye became closed and cloudy

experiments.append(exp7)

exp7.add_site(2000)
exp7.maxDepth = 1440
exp7.add_session('13-13-09', 'a', 'pureTones', 'am_tuning_curve')
exp7.add_session('13-22-02', 'a', 'naturalSound', 'natural_sound_detection')
exp7.add_session('13-49-23', 'b', 'AM', 'am_tuning_curve')


# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

exp8 = celldatabase.Experiment(subject, '2025-02-21', brainArea='right_AC', probe='NPv2-1392', recordingTrack='centerCenter_DiO', info=['facesLateral', 'soundLeft'])

# Dura-Gel in well
# Reference electrode is 1:tip
# All shanks bank 97-192 active
# Left brain to settle for 15 min
# Looks a little noiser today
# Targetting AH, VAF, A2, AAF
# Used a 32.5 angle with respect to the horizontal plane
# Used a 97 degree angle with respect to the azimuth plane
# The Ephys gui froze around trial 140 if the natural sounds paradigm (not sure if this will affect the data) 

experiments.append(exp8)

exp8.add_site(1500)
exp8.maxDepth = 720
exp8.add_session('15-06-23', 'a', 'pureTones', 'am_tuning_curve')
exp8.add_session('15-14-44', 'a', 'naturalSound', 'natural_sound_detection')
exp8.add_session('15-47-20', 'b', 'AM', 'am_tuning_curve')

