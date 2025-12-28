from jaratoolbox import celldatabase

subject = 'arch043'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])

#experiments.append(expx)

# Reference electrode is 4:tip


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')

#2025-12-15
exp0 = celldatabase.Experiment(subject, '2025-12-15', brainArea='left_pStr', probe='NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp0)

# Started habituation of the mouse at 12:45 pm
# Left mice for periods of 8 minutes in the rig and put it back in the cage (I did this 3 times)
# Mouse in the rig (after 3 times of taking it in and out) at 1:28 pm
# Probe in the right positioning at 2:08 pm (First attempt)
# Power of the laser 10 mW (Dial 5.74 / screen 48)
# Red part of the probe faces medial
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (1 mm tick)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse has ground wire.


exp0.add_site(4500) 
exp0.maxDepth = 4500

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp0.add_session('14-33-46', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('14-48-36', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('15-16-12', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('15-32-44', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 1 Bank A
exp0.add_session('15-57-46', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('16-00-58', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials


#2025-12-18
exp1 = celldatabase.Experiment(subject, '2025-12-18', brainArea='left_pStr', probe='NPv2-1134', recordingTrack='anteriorCenter_DiD', info=['facesLateral', 'soundRight'])

experiments.append(exp1)

# Mouse in the rig at 10 am
# I went with the probe till 2400 um and one electrode started bending.
# I don't know if it's because of the positioning of the probe.
# I took it out, coated it again and changed the placement of the probe
# Probe in the right positioning at 12:35 pm 
# Power of the laser 10 mW (Dial 5.74 / screen 47.8)
# Red part of the probe faces medial
# Reference electrode is 1:tip
# Targeting left pStr
# Probe is located in the center of craniotomy, a little more anterior than previous penetration (The one on 2025-12-15)
# I zero the manipulator when I first touched dura-gel (there's a very fine layer of duragel)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse does not have ground wire.
#I added saline before starting to record every session


exp1.add_site(4000) 
exp1.maxDepth = 4000

#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp1.add_session('12-47-38', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('13-04-16', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('13-32-49', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('13-50-11', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shanks 1 and 2
exp1.add_session('14-12-04', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials # I forgot to select the bank A

# Shank 1 Bank A
exp1.add_session('14-15-18', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials 

# Shank 1 Bank B
exp1.add_session('14-17-16', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

#LASER TURNED ON BUT NOT GOING INSIDE THE BRAIN
#I gave water to the mouse before starting the new sessions
#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
exp1.add_session('14-35-02', 'f', 'optoTuningAM', 'am_tuning_curve') #440 #I forgot to manually select the shanks
exp1.add_session('14-46-32', 'g', 'optoTuningAM', 'am_tuning_curve') #440 
exp1.add_session('15-05-14', 'c', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('15-35-51', 'h', 'optoTuningFreq', 'am_tuning_curve') #643 trials
exp1.add_session('15-53-01', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#2025-12-19
exp2 = celldatabase.Experiment(subject, '2025-12-19', brainArea='right_pStr', probe='NPv2-3082', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])

experiments.append(exp2)

# Mouse in the rig at 10:20 am
# Started to penetrate on the right hemisphere and there was some resistance after the dura-gel.
# I pushed the shanks too much and 1 shank broke midway. I continued with the remaining shank till the desired depth (4600)
# When I checked the signals, I realized that the remaining shank had also broke.
# I took a new probe, coated it with DiD and went again till 4600
# The tickness of the dura-gel is about 1.1 mm
# Probe in the right positioning at 12:45 pm (First attempt with new probe)
# Power of the laser 10 mW (Dial 5.1 / screen 37.8)
# Red part of the probe faces medial
# Reference electrode is 3:tip
# Targeting right pStr
# Probe is located in the center of craniotomy
# I zero the manipulator when I first touched dura-gel (1.1 mm tick)
# I recorded 2 fast sessions to check whether we can tell air-dura-gel-brain apart by looking at the LFPs
# The mouse does not have ground wire, so I removed the layer of dura-gel in the corner to put the ground wire and add saline


exp2.add_site(4600) 
exp2.maxDepth = 4600

#Shanks 3 and 4. Manually selected channels 1-96 and 97-192.
exp2.add_session('13-01-43', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('13-17-32', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('13-46-22', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('14-03-07', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

# Shank 3 Bank A
exp2.add_session('14-26-11', 'c', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 3 Bank B
exp2.add_session('14-28-09', 'd', 'tuningFreq', 'am_tuning_curve') #40 trials
