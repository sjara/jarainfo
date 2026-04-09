from jaratoolbox import celldatabase

subject = 'arch051'
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

#2026-03-04
# Started habituation of the mouse.
# Took the mouse in the rig during 3 periods of 10, 15 and 20 minutes.

#2026-03-05
exp0 = celldatabase.Experiment(subject, '2026-03-05', brainArea='right_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundLeft'])

experiments.append(exp0)

# Mouse in the rig at 9:57 am
# Probe in the right depth at 12:04  am
# Power of the laser 10 mW (Dial 6.75 / screen 63.8)
# Red part of the probe faces lateral
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel. Layer of about 1 mm.
# Total depth from the dura-gel 4600 um. Depth inside the brain 3600 um.
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has no ground wire.
#I added saline before starting to record every session


exp0.add_site(3600) 

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp0.add_session('12-24-49', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('12-41-58', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('13-10-57', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('13-28-35', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A
exp0.add_session('13-50-50', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('13-54-03', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials

exp0.maxDepth = 3600


#2026-03-06

# Mouse in the rig at 10:44 am
# I was able to penetrate the brain but at a depth of 1270 um one shank started bending
# After multiple attempts and 2 different locations,
# I could not go beyond that point today.
# I used DiD

#2026-03-19
exp1 = celldatabase.Experiment(subject, '2026-03-19', brainArea='left_pStr', probe='NPv2-2171', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp1)

# Mouse in the rig at 9:40 am
# Probe in the right depth at 11:17 am
# Power of the laser 10 mW (Dial 7 / screen 67.8)
# Red part of the probe faces medial
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel. Layer of about 800 um.
# Total depth from the dura-gel 4400 um. Depth inside the brain 3600 um
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has no ground wire.
# Particularly today, the mouse is running almost all the time and that is creating big peaks in the signals


exp1.add_site(3600) 

#All shanks -  1-96
exp1.add_session('11-32-21', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('11-53-59', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('12-21-25', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('12-39-36', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mouse before starting the new sessions
exp1.add_site(2880) 
#All shanks -  97-192
exp1.add_session('13-05-15', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('13-21-52', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('13-50-58', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('14-08-02', 'd', 'optoNaturalInstances', 'natural_sound_detection') #165 OptoNaturalInstances

#Control sessions
#NO OPTIC FIBER CONNECTED
#Fiber on but outside of the brain
#It is the same site (3600), I just added a new site for data analysis purposes
#All shanks -  1-96
exp1.add_site(3601)
exp1.add_session('14-57-38', 'e', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('15-12-06', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

#CHANGE THE ELECTRODES
#All shanks -  97-192
exp1.add_site(2881) 
exp1.add_session('15-23-58', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('15-37-50', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#CHANGE THE ELECTRODES


#CHANGE THE ELECTRODES
# Shank 1 Bank A
exp1.add_session('15-54-16', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

#CHANGE THE ELECTRODES
# Shank 1 Bank B
exp1.add_session('15-56-03', 'j', 'tuningFreq', 'am_tuning_curve') #40 trials

exp1.maxDepth = 3600


#2026-03-20
exp2 = celldatabase.Experiment(subject, '2026-03-20', brainArea='left_pStr', probe='NPv2-2171', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])

experiments.append(exp2)

# Mouse in the rig at 10:10 am
# Probe in the right depth at 11:55  am
# Power of the laser 10 mW (Dial 7 / screen 67.8)
# Red part of the probe faces Lateral
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel. Layer of about 800 um.
# Total depth from the dura-gel 4400 um. Depth inside the brain 3600 um
# I did not record the sessions to check the LFPs
# The mouse has no ground wire.
# The mouse is running at a high speed over time

exp2.add_site(3600) 

#All shanks -  1-96
exp2.add_session('12-05-15', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('12-19-41', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('12-48-08', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('13-05-04', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#Gave water to the mouse before starting the new sessions
exp2.add_site(2880) 
#All shanks -  97-192
exp2.add_session('13-30-07', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('13-46-10', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('14-16-13', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('14-33-14', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp2.maxDepth = 3600


#2026-03-23
# I was able to penetrate on the right hemispshere
# Once the probe was inside the brain, when checking the signals I realized that those were very noisy
# I tried moving things around and asked help from Santiago but we couldn't figure out the problem
# So I had to take the probe out without recording
# I used DiD and the depth was 4400 from the dura (layer of about 1mm)

#2026-03-26
exp3 = celldatabase.Experiment(subject, '2026-03-26', brainArea='right_pStr', probe='NPv2-8253', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundLeft'])

experiments.append(exp3)

# Mouse in the rig at 10:30 am
# Probe in the right depth at 11:35 am
# Power of the laser 10 mW (Dial 6.75 / screen 63.9)
# Red part of the probe faces lateral
# Reference electrode is 1:tip
# Targeting right pStr
# Probe is located in the center of craniotomy. This penetration is more medial than the one on 2026-03-05
# I zero the manipulator when I first touched dura-gel. Layer of about 800 um.
# Total depth from the dura-gel 4400 um. Depth inside the brain 3600 um
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has no ground wire.


exp3.add_site(3600) 

#All shanks -  1-96
exp3.add_session('11-47-02', 'a', 'optoTuningAM', 'am_tuning_curve') #442
exp3.add_session('12-04-08', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp3.add_session('12-32-30', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp3.add_session('12-49-32', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances
#CHANGE THE ELECTRODES

#Gave water to the mouse before starting the new sessions

#CHANGE THE ELECTRODES
exp3.add_site(2880) 
#All shanks -  97-192
exp3.add_session('13-14-44', 'c', 'optoTuningAM', 'am_tuning_curve') #444
exp3.add_session('13-31-14', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp3.add_session('14-00-14', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp3.add_session('14-17-09', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances
#CHANGE THE ELECTRODES

#Control sessions
#NO OPTIC FIBER CONNECTED
#Fiber on but outside of the brain
#It is the same site (3600), I just added a new site for data analysis purposes
#CHANGE THE ELECTRODES
#All shanks -  1-96
exp3.add_site(3601)
exp3.add_session('14-55-15', 'e', 'optoTuningAM', 'am_tuning_curve') #440
exp3.add_session('15-10-56', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

#CHANGE THE ELECTRODES
#All shanks -  97-192
exp3.add_site(2881) 
exp3.add_session('15-28-25', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp3.add_session('15-43-22', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#CHANGE THE ELECTRODES


#CHANGE THE ELECTRODES
# Shank 1 Bank A
exp3.add_session('15-59-21', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

#CHANGE THE ELECTRODES
# Shank 1 Bank B
exp3.add_session('16-01-53', 'j', 'tuningFreq', 'am_tuning_curve') #40 trials

exp3.maxDepth = 3600

