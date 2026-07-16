from jaratoolbox import celldatabase

subject = 'arch045'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]). 
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])

# Reference electrode is 3:tip

#experiments.append(expx)


#expx.add_site(1500)
#expx.maxDepth = 1500
#expx.add_session('xx-xx-xx', 'a', 'pureTones', 'am_tuning_curve')
#expx.add_session('xx-xx-xx', 'a', 'naturalSound', 'natural_sound_detection')
#expx.add_session('xx-xx-xx', 'b', 'AM', 'am_tuning_curve')

#.................................................................................

exp0 = celldatabase.Experiment(subject, '2026-02-24', brainArea='right_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp0)


#Mouse in the rig at 11:57am
#Probe inserted at 12:30pm
#The data was very noisy I think because the ground wire fell, but not compeletely so it is probably touching the head bar creating a loop, I used the saline well wire.
#Took the mouse out at 5:00 pm
#I zeroed the manipulator when I first touched dura-gel

exp0.add_site(4000) 
exp0.maxDepth = 4000

#Recording from all shanks, channels 1-96.
exp0.add_session('13-44-52', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('14-05-01', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('14-24-52', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('14-54-49', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp0.add_site(3999) 
# IT IS THE SAME SITE AS THE FIRST ONE. I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recoeding from all shanks, channels 97-192.
exp0.add_session('15-27-33', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('15-43-40', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('16-01-07', 'c', 'optoNaturalCategories', 'natural_sound_detection') #212 OptoNaturalCategories
exp0.add_session('16-32-18', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


exp0.add_site(3998) #The tip is in the depth of 4000, I wrote 3998 because of having specific site for each. 
# Shank 3 Bank A
exp0.add_session('16-54-44', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

exp0.add_site(1120) 
# Shank 3 Bank B
exp0.add_session('16-59-35', 'f', 'tuningFreq', 'am_tuning_curve') #40 trial


#...............................................................................................................

exp1 = celldatabase.Experiment(subject, '2026-03-11', brainArea='Right_pStr', probe='NPv2-3813', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundLeft'])

experiments.append(exp1)

exp1.add_site(3700) 
exp1.maxDepth = 3700

#Mouse in rig at 10:37am.
#This mouse did not have a ground wire so I did the well grounding.
#Took the mouse out at 13:20pm.
#I zeroed the manipulator when I first touched dura-gel


#Recording from 1 and 3, channels 1-96, and recording from shank 4 channels 1-192.(Not recording from shank 2).
exp1.add_session('11-37-38', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('11-53-02', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('12-09-47', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('12-38-23', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances


exp1.add_site(3698) #The tip is in the depth of 3700, I wrote 3698 because of having specific site for each. 
# Shank 3 Bank A
exp1.add_session('13-06-24', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

exp1.add_site(820)
# Shank 3 Bank B
exp1.add_session('13-08-47', 'f', 'tuningFreq', 'am_tuning_curve') #40 trial


#........................................................................................................
exp2 = celldatabase.Experiment(subject, '2026-04-14', brainArea='left_pStr', probe='NPv2-8253', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp2)

#I tried alot and exactly at this depth one of the shanks tended to bend, I believe it is touching the optic fiber, i still decided to record to sessions in case.
#I zeroed the manipulator when I first touched dura-gel



exp2.add_site(2568) 
exp2.maxDepth = 2568


#Recording from all shanks, channels 1-96.
exp2.add_session('13-14-00', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('13-29-29', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials


exp2.add_site(2566) #The tip is in the depth of 3700, I wrote 3698 because of having specific site for each. 
# Shank 3 Bank A
exp2.add_session('13-47-59', 'e', 'tuningFreq', 'am_tuning_curve') #40 trials

exp2.add_site(312) #The actual dept is -312
# Shank 3 Bank B
exp2.add_session('13-50-07', 'f', 'tuningFreq', 'am_tuning_curve') #40 trial

#.....................................................................................................
exp3 = celldatabase.Experiment(subject, '2026-04-16', brainArea='left_pStr', probe='NPv2-8253', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundRight'])

experiments.append(exp3)

#Mouse in the rig at 10:15pm
#Penetrated easly.
#The reference is tip 3.
#Red part of the probe faces medial.
#I zeroed the manipulator when I first touched dura-gel.



exp3.add_site(3510) 
exp3.maxDepth = 3570


#Recording from all shanks, channels 1-96.
exp3.add_session('10-51-48', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp3.add_session('11-07-34', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp3.add_session('11-24-20', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp3.add_session('11-52-13', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp3.add_site(2789) 
# IT IS THE SAME SITE AS THE FIRST ONE(3700). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 1-9 with the laser shining outside of the brain. 
exp3.add_session('12-20-25', 'c', 'optoTuningAM', 'am_tuning_curve') #488
exp3.add_session('12-36-33', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials

exp3.add_site(3508) 
# Shank 3 Bank A
exp3.add_session('12-57-41', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

exp3.add_site(630) 
# Shank 3 Bank B
exp3.add_session('12-59-50', 'j', 'tuningFreq', 'am_tuning_curve') #40 trial
#...................................................................................
exp4 = celldatabase.Experiment(subject, '2026-04-19', brainArea='left_pStr', probe='NPv2-8253', recordingTrack='centerRight_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp4)

#Mouse in the rig at 10:15pm
#I had to remove the dura-get to be able to penetrate. After removing the duragel penetrated easily.
#The reference is tip 3.
#Red part of the probe faces medial.
#This mouse does not have a ground wire. I used the saline well for grounding.
#The probe was fine when checked bbefore inseriting, Although it is very noisy when decided to record. I tried grounding as best as I could but the results where not satisfactory. I could see spikes so I decided to record anyways.
#zeroed from the surface of the brain.
#I zeroed the manipulator when I first touched dura-gel



exp4.add_site(3600) 
exp4.maxDepth = 3602


#Recording from all shanks, channels 97-192.
exp4.add_session('12-03-14', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp4.add_session('12-18-47', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp4.add_session('12-34-49', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp4.add_session('13-01-56', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

#gave water to the mouse
exp4.add_site(2880) 
# IT IS THE SAME SITE AS THE FIRST ONE. I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recoeding from all shanks, channels 1-96.
exp4.add_session('13-28-55', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp4.add_session('13-28-55', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#The mouse's eye becoming cloudy. 
exp4.add_session('13-59-45', 'c', 'optoNaturalCategories', 'natural_sound_detection') #203 OptoNaturalCategories
exp4.add_session('14-27-44', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp4.add_site(3599) 
#Recording from all shanks, channels 1-96.
exp4.add_session('14-55-44', 'e', 'optoTuningAM', 'am_tuning_curve') #440
#Vaterycin applied to the eyes. 
exp4.add_session('15-13-41', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

#Gave mouse water
exp4.add_site(2879) 
#Recording from all shanks, channels 97-192.
exp4.add_session('15-32-42', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp4.add_session('15-46-56', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials



exp4.add_site(3598) 
# Shank 3 Bank A
exp4.add_session('16-03-26', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

exp4.add_site(720)
# Shank 3 Bank B
exp4.add_session('16-05-22', 'j', 'tuningFreq', 'am_tuning_curve') #40 trial
