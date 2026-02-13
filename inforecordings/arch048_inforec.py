from jaratoolbox import celldatabase

subject = 'arch048'
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

#2026-02-02
# Started habituation of the mice.
# Took the mice in the rig during 3 periods of ten minutes each.

#2026-02-05
exp0 = celldatabase.Experiment(subject, '2026-02-05', brainArea='right_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundLeft'])

experiments.append(exp0)

# Mouse in the rig at 11:42 am
# Probe in the right depth at 1:21 pm
# Power of the laser 10 mW (Dial 4.98 / screen 36.2)
# Red part of the probe faces lateral
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (There was a very fine layer protecting the brain)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has ground wire.


exp0.add_site(4000) 

#All shanks -  1-96
exp0.add_session('13-45-01', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('14-02-01', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('14-29-33', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('14-46-10', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mice before starting the new sessions

exp0.add_site(3280) 
#All shanks -  97-192
exp0.add_session('15-12-29', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('15-26-40', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('15-55-46', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('16-12-30', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


# Shank 1 Bank A
exp0.add_session('16-34-35', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('16-36-07', 'f', 'tuningFreq', 'am_tuning_curve') #40 trials

exp0.maxDepth = 4000

#2026-02-06
exp1 = celldatabase.Experiment(subject, '2026-02-06', brainArea='right_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundLeft'])

experiments.append(exp1)

# Mouse in the rig at 11 am
# Probe in the right depth at 12:51 pm
# Inserted the probe in the first attempt, but I took a lot of time because at 2 different depths (2000 and 2600) 2 different shanks started bending
# Power of the laser 10 mW (Dial 4.98 / screen 36.1)
# Red part of the probe faces lateral
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (There was a very fine layer protecting the brain)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has ground wire.


exp1.add_site(4400) 

#All shanks -  1-96
exp1.add_session('13-04-42', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('13-18-56', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('13-46-12', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('14-01-53', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mice before starting the new sessions

exp1.add_site(3680) 
#All shanks -  97-192
exp1.add_session('14-26-36', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('14-41-19', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('15-08-22', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('15-24-11', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


# Shank 1 Bank A
exp1.add_session('15-46-40', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp1.add_session('15-49-04', 'f', 'tuningFreq', 'am_tuning_curve') #40 trials

exp1.maxDepth = 4400


#2026-02-09
exp2 = celldatabase.Experiment(subject, '2026-02-09', brainArea='left_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundRight'])

experiments.append(exp2)

# Mouse in the rig at 10:44 am
# Probe in the right depth at 11:30 am (first attempt)
# Power of the laser 10 mW (Dial 5.6 / screen 45.7)
# Red part of the probe faces lateral
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (There was a very fine layer protecting the brain).
# During the surgery, when doing the left ccraniotomy, at the time I removed the piece of skull
# the brain was already bulging out. I'm not very sure about the depth for that reason.
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has ground wire.


exp2.add_site(4500) 

#All shanks -  1-96
exp2.add_session('11-43-08', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('11-58-42', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('12-26-53', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('12-42-52', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mice before starting the new sessions
 
#All shanks -  1-96 (I forgot to change the set of electrodes and recorded from the same bank
exp2.add_session('13-07-19', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('13-22-31', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('13-50-10', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('14-07-28', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#All shanks -  1-96 #I recorded this session for the LFP and then figured out my mistake about the selection of electrodes
exp2.add_session('14-29-33', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

#Gave water to the mice before starting the new sessions
exp2.add_site(3780) 
#All shanks -  97-192
exp2.add_session('14-38-27', 'f', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('14-53-22', 'e', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('15-20-36', 'g', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('15-36-23', 'f', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A
exp2.add_session('15-58-26', 'h', 'tuningFreq', 'am_tuning_curve') #41 trials

# Shank 1 Bank B
exp2.add_session('16-00-04', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

exp2.maxDepth = 4500

#2026-02-12
exp3 = celldatabase.Experiment(subject, '2026-02-12', brainArea='left_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundRight'])

experiments.append(exp3)

# Mouse in the rig at 10:46 am
# Probe in the right depth at 11:39 am
# Power of the laser 10 mW (Dial 5.6 / screen 45.7)
# Red part of the probe faces medial
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (There was a very fine layer protecting the brain)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse does not have ground wire.
# I added saline before starting to record every session.


exp3.add_site(4200) 

#All shanks -  1-96
exp3.add_session('11-55-57', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp3.add_session('12-12-26', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp3.add_session('12-40-28', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp3.add_session('12-58-53', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mice before starting the new sessions

exp3.add_site(3480) 
#All shanks -  97-192
exp3.add_session('13-26-09', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp3.add_session('13-46-05', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp3.add_session('14-15-17', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp3.add_session('14-33-20', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Control sessions
#NO OPTIC FIBER CONNECTED but turned on outside of the brain
#I gave water to the mouse before to start recording

#Site 4201 corresponds to the same penetration as the first recording (4200)
#I just added a new site for analysis purposes. To be able to separate control from normal sessions.
exp3.add_site(4201)
#All shanks -  1-96
exp3.add_session('15-16-24', 'e', 'optoTuningAM', 'am_tuning_curve') #440
exp3.add_session('15-30-32', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

#Site 3481 corresponds to the same penetration as the first recording (3480)
#I just added a new site for analysis purposes. To be able to separate control from normal sessions.
exp3.add_site(3481)
#All shanks -  97-192
exp3.add_session('15-48-39', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp3.add_session('16-03-51', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials

# Shank 1 Bank A
exp3.add_session('16-19-40', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp3.add_session('16-22-44', 'j', 'tuningFreq', 'am_tuning_curve') #40 trials

exp3.maxDepth = 4200

