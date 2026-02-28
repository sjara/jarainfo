from jaratoolbox import celldatabase

subject = 'arch050'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])

# Reference electrode is 4:tip

#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')

#2026-02-18
# Started habituation of the mice.
# Took the mice in the rig during 3 periods of 10, 15 and 20 minutes.

#2026-02-19
exp0 = celldatabase.Experiment(subject, '2026-02-19', brainArea='right_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp0)

# Mouse in the rig at 9:57 am
# The part of the ground wire that was exposed, fell down.
# I needed to remove the plastic of the tip of the wire to be able to connect it and it took me some time.
# Probe in the right depth at 11:51 am
# Power of the laser 10 mW (Dial 6.36 / screen 57.7)
# Red part of the probe faces medial
# Reference electrode is 2:tip
# Targeting right pStr
# Probe is located in the center of caniotomy
# I zero the manipulator when I first touched dura-gel. Layer of about 700 um.
# Total depth from the dura-gel 4400 um. Depth inside the brain 3700 um
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has ground wire.


exp0.add_site(3700) 

#All shanks -  1-96
exp0.add_session('12-15-56', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('12-31-28', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('12-58-14', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('13-14-27', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mice before starting the new sessions

exp0.add_site(2980) 
#All shanks -  97-192
exp0.add_session('13-43-28', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('13-57-44', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('14-25-23', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('14-41-28', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


# Shank 2 Bank A
exp0.add_session('15-04-18', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 2 Bank B
exp0.add_session('15-06-55', 'f', 'tuningFreq', 'am_tuning_curve') #40 trials

exp0.maxDepth = 3700

#2026-02-23
exp1 = celldatabase.Experiment(subject, '2026-02-23', brainArea='right_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])

experiments.append(exp1)

# Mouse in the rig at 11:19 am.
# Probe in the right depth at 12:25 am
# Power of the laser 10 mW (Dial 6.36 / screen 57.3)
# Red part of the probe faces medial
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of caniotomy
# I zero the manipulator when I first touched dura-gel. Layer of about 700 um.
# Total depth from the dura-gel 4400 um. Depth inside the brain 3700 um
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has ground wire.


exp1.add_site(3700) 

#All shanks -  1-96
exp1.add_session('12-43-18', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('12-57-55', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('13-26-19', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('13-42-18', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mice before starting the new sessions

exp1.add_site(2980) 
#All shanks -  97-192
exp1.add_session('14-10-09', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('14-24-27', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('14-51-50', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('15-08-13', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A
exp1.add_session('15-30-38', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp1.add_session('15-32-13', 'f', 'tuningFreq', 'am_tuning_curve') #40 trials

exp1.maxDepth = 3700

#2026-02-27
exp2 = celldatabase.Experiment(subject, '2026-02-27', brainArea='left_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp2)

# Mouse in the rig at 10:10 am
# Probe in the right depth at 11:20 am
# Power of the laser 10 mW (Dial 5.14 / screen 38.5)
# Red part of the probe faces medial
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of caniotomy
# I zero the manipulator when I first touched dura-gel. Layer of about 700 um.
# Total depth from the dura-gel 4300 um. Depth inside the brain 3600 um
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse does not have ground wire.
# I added saline before every session


exp2.add_site(3600) 

#All shanks -  1-96
exp2.add_session('11-43-13', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('12-10-41', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('12-40-30', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('12-58-28', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mice before starting the new sessions
#CHANGE THE ELECTRODES

exp2.add_site(2880) 
#All shanks -  97-192
exp2.add_session('14-29-19', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('14-44-09', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('15-15-12', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('15-31-25', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


#CHANGE THE ELECTRODES
#I did not add saline to know the limit from the dura
# Shank 1 Bank A
exp2.add_session('15-54-00', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp2.add_session('15-56-16', 'f', 'tuningFreq', 'am_tuning_curve') #40 trials

exp2.maxDepth = 3600
