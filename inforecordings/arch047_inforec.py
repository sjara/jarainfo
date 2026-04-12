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

exp0.add_site(2980)
#Recoeding from all shanks, channels 97-192.
exp0.add_session('16-02-50', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('16-17-27', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#Gave water to the mouse. 
exp0.add_session('17-07-42', 'c', 'optoNaturalCategories', 'natural_sound_detection') #212 OptoNaturalCategories
exp0.add_session('16-37-08', 'd', 'optoNaturalInstances', 'natural_sound_detection') #200 OptoNaturalInstances

exp0.add_site(3699) 
# IT IS THE SAME SITE AS THE FIRST ONE(3700). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 1-9 with the laser shining outside of the brain. 
exp0.add_session('17-42-13', 'e', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('17-56-55', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

exp0.add_site(2979)
# IT IS THE SAME SITE AS THE SECOND ONE(2980). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 97-192, with the laser shining outside of the brain. 
exp0.add_session('18-14-47', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp0.add_session('18-29-33', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#...................................................................................................................

exp1 = celldatabase.Experiment(subject, '2026-04-09', brainArea='left_pStr', probe='NPv2-8253', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundRight'])

experiments.append(exp1)

#Mouse in the rig at 09:02pm
#Penetrated easily at one try. 
#The reference is tip 1.
#Red part of the probe faces medial.
#Took the mouse out at 7:05pm. 



exp1.add_site(3710) 
exp1.maxDepth = 3710

# Shank 1 Bank A
exp1.add_session('12-22-10', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 1 Bank B
exp1.add_session('12-24-03', 'j', 'tuningFreq', 'am_tuning_curve') #40 trial

#Recording from all shanks, channels 1-96.
exp1.add_session('09-34-55', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('09-49-26', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp1.add_session('10-05-32', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp1.add_session('10-32-54', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp1.add_site(2990)
#Recoeding from all shanks, channels 97-192.
exp1.add_session('10-55-53', 'c', 'optoTuningAM', 'am_tuning_curve') #440
exp1.add_session('11-10-30', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#Gave water to the mouse. 
exp1.add_session('11-28-10', 'c', 'optoNaturalCategories', 'natural_sound_detection') #212 OptoNaturalCategories
exp1.add_session('11-55-46', 'd', 'optoNaturalInstances', 'natural_sound_detection') #200 OptoNaturalInstances
#....................................................................................................................

exp2 = celldatabase.Experiment(subject, '2026-04-12', brainArea='Right_pStr', probe='NPv2-8253', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])

experiments.append(exp2)

#Mouse in the rig at 10:40pm
#Penetrated in the first try.
#The reference is tip 3.
#Red part of the probe faces medial.
#Took the mouse out at 7:05pm. 



exp2.add_site(3700) 
exp2.maxDepth = 3700

# Shank 3 Bank A
exp2.add_session('15-18-07', 'i', 'tuningFreq', 'am_tuning_curve') #40 trials

# Shank 3 Bank B
exp2.add_session('15-20-14', 'j', 'tuningFreq', 'am_tuning_curve') #40 trial

#Recording from all shanks, channels 1-96.
exp2.add_session('11-00-26', 'a', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('11-15-16', 'b', 'optoTuningFreq', 'am_tuning_curve') #640 trials
exp2.add_session('11-31-32', 'a', 'optoNaturalCategories', 'natural_sound_detection') #200 OptoNaturalCategories
exp2.add_session('11-59-45', 'b', 'optoNaturalInstances', 'natural_sound_detection') #160 OptoNaturalInstances

exp2.add_site(2980)
#Recoeding from all shanks, channels 97-192.
exp2.add_session('12-23-31', 'c', 'optoTuningAM', 'am_tuning_curve') #447
exp2.add_session('12-39-07', 'd', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#Gave water to the mouse. 
exp2.add_session('13-10-34', 'c', 'optoNaturalCategories', 'natural_sound_detection') #212 OptoNaturalCategories
exp2.add_session('13-41-27', 'd', 'optoNaturalInstances', 'natural_sound_detection') #200 OptoNaturalInstances

exp2.add_site(3699) 
# IT IS THE SAME SITE AS THE FIRST ONE(3700). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 1-9 with the laser shining outside of the brain. 
exp2.add_session('14-12-35', 'e', 'optoTuningAM', 'am_tuning_curve') #440
#The light was too much from the laser so I covered a bit with the tape so only the very tip of the fiber shines light. 
exp2.add_session('14-28-17', 'f', 'optoTuningFreq', 'am_tuning_curve') #640 trials

exp2.add_site(2979)
# IT IS THE SAME SITE AS THE SECOND ONE(2980). I JUST ADDED A NEW SITE FOR DATA ANALYSIS PURPOSES
#Recording from all shanks, channels 97-192, with the laser shining outside of the brain. 
exp2.add_session('14-44-35', 'g', 'optoTuningAM', 'am_tuning_curve') #440
exp2.add_session('14-59-17', 'h', 'optoTuningFreq', 'am_tuning_curve') #640 trials
#......................................................................................................
