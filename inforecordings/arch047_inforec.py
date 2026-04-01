exp0 = celldatabase.Experiment(subject, '2026-03-31', brainArea='left_pStr', probe='NPv2-8253', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])

experiments.append(exp0)

#Mouse in the rig at 2:05pm
#Penetrated after 20 minutes. 
#The reference is tip 1.
#Took the mouse out at pm.
#Red part of the probe faces medial.
#Took the mouse out at 7:05pm. 



exp0.add_site(3700) 
exp0.maxDepth = 3700

# Shank 1 Bank A
exp0.add_session('18-46-03', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp0.add_session('18-48-18', 'j', 'tuningFreq', 'am_tuning_curve') #40 trial

#Recording from all shanks, channels 1-96.
exp0.add_session('14-40-53', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('14-55-41', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp0.add_session('15-12-04', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp0.add_session('15-40-09', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp0.add_site()
#Recoeding from all shanks, channels 97-192.
exp0.add_session('16-02-50', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('16-17-27', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#Gave water to the mouse. 
exp0.add_session('17-07-42', 'c', 'optoNaturalCategories', 'natural_sound_detection') #212 OptoNaturalCategories
exp0.add_session('16-37-08', 'd', 'optoNaturalInstances', 'natural_sound_detection') #200 OptoNaturalInstances

exp0.add_site() 
# IT IS THE SAME SITE AS THE FIRST ONE (4000). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 1-9 with the laser shining outside of the brain. 
exp0.add_session('17-42-13', 'e', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('17-56-55', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

exp0.add_site()
# IT IS THE SAME SITE AS THE SECOND ONE (3280). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 97-192, with the laser shining outside of the brain. 
exp0.add_session('18-14-47', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('18-29-33', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials
