from jaratoolbox import celldatabase

subject = 'arch046'
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

#.........................................................................................

exp0 = celldatabase.Experiment(subject, '2026-03-03', brainArea='right_pStr', probe='NPv2-3973', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp0)

#Mouse in the rig at 10:30am
#Penetrated easily in the first attemp
#The reference is tip 1.
#Took the mouse out at 3:40pm.
#Mouse had noticable eye discharge at the end, I acalled the vet. 



exp0.add_site(4000) 
exp0.maxDepth = 4000

# Shank 1 Bank A
exp0.add_session('13-59-15', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('14-02-09', 'j', 'tuningFreq', 'am_tuning_curve') #40 trial

#Recording from all shanks, channels 1-96.
exp0.add_session('11-05-29', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('11-20-38', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('11-42-18', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('12-12-05', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp0.add_site(3280)
#Recoeding from all shanks, channels 97-192.
exp0.add_session('12-35-48', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('12-51-05', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('13-07-15', 'c', 'optoNaturalCategories', 'natural_sound_detection') #212 OptoNaturalCategories
exp0.add_session('13-34-36', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp0.add_site(3999) 
# IT IS THE SAME SITE AS THE FIRST ONE (4000). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 1-9 with the laser shining outside of the brain. 
exp0.add_session('14-11-14', 'e', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('14-28-02', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

exp0.add_site(3279)
# IT IS THE SAME SITE AS THE SECOND ONE (3280). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 97-192, with the laser shining outside of the brain. 
exp0.add_session('14-47-41', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('15-02-02', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials


#...............................................................................................

#2026-03-08
#exp1 = celldatabase.Experiment(subject, '2026-03-08', brainArea='right_pStr', probe='NPv2-3813', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])

#This probe has only 3 shanks.
#Tip 4 is the reference.
#mouse in the rig at 11:36am.
#The eye looks good when put the mouse in the rig.
#Pwnwtrated at 11:58am. 
#I was not able to record today because I think the probe could not detect the head stage. I could see the probe being recognized in open ephys but i could not see any signals form any shanks, banks or channels. 

#...............................................................................................
#2026-03-22
#Inserted the probe (2212um) using DiI in the center of the craniotomy, and could not go further because that was the limit of the manipulator, I should have put the probe more down.
#The data was very noisy, I tried grounding many things in the rig and it did not make it any better.
#Today, i was not able to record.

#................................................................................................

#2026-03-25
#Mouse in the rig at 10:45 am.
#The mouse does not have a ground wire, used the other well (right) as the refernce.
#Red side of the probe is towards the center.
#Insertion was super easy, the probe did not at all during insersion.
#During the sessions in which laser shines outside the animals eye becomes cloudy.
#Took the mouse out at 15:45 pm. 


exp1 = celldatabase.Experiment(subject, '2026-03-25', brainArea='left_pStr', probe='NPv2-8253', recordingTrack='centerCenter_DiD, info=['facesLateral', 'soundRight'])

experiments.append(exp1)



exp1.add_site(3750) 
exp1.maxDepth = 3750

# Shank 1 Bank A
exp1.add_session('14-18-10', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp1.add_session('14-20-26', 'j', 'tuningFreq', 'am_tuning_curve') #40 trial

#Recording from all shanks, channels 1-96.
exp1.add_session('11-12-25', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('11-27-24', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('11-43-58', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('12-11-42', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp1.add_site(3030)
#Recoeding from all shanks, channels 97-192.
exp1.add_session('12-48-20', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('13-04-06', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#Gave mouse water
exp1.add_session('13-23-49', 'c', 'optoNaturalCategories', 'natural_sound_detection') #213 OptoNaturalCategories
exp1.add_session('13-54-31', 'd', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp1.add_site(3749) 
# IT IS THE SAME SITE AS THE FIRST ONE (4000). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 1-9 with the laser shining outside of the brain. 
exp1.add_session('14-26-23', 'e', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('14-41-11', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

exp1.add_site(3029)
# IT IS THE SAME SITE AS THE SECOND ONE (3280). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 97-192, with the laser shining outside of the brain. 
exp1.add_session('14-58-02', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('15-12-29', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials
