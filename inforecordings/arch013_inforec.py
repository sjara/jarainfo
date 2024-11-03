from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'arch013'
experiments = []


exp0 = celldatabase.Experiment(subject, '2024-10-23', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundRight'])
experiments.append(exp0)

exp0.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192

# Open ephys crashed for the first time at "16-28-10" 
 
# exp0.add_session('16-31-09','_bad1','AM','am_tuning_curve')
# 395 trials into it but the open ephys crashed.
# the ephys crashed  times at "16-31-09".

exp0.add_session('16-50-11','a','optoTuningAM','am_tuning_curve')  # 403 trials 
 
exp0.add_session('17-08-09','a','optoNaturalCategories','natural_sound_detection')


exp0.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
exp0.add_session('17-40-44','b','optoTuningAM','am_tuning_curve')  # 479 trials 

exp0.add_session('17-57-36','b','optoNaturalCategories','natural_sound_detection')  # went to 42 trials and it crashed

exp0.maxDepth = 4500

# 12:55 animal in the rig
# 12:58 sylgard off
# 13:02 ground wire in the well
# 15:22 probe in the brain
# 16:14 started recording with shanks 97-192
# 17:40 recording with shanks 1-96
# 18:02 finished recording
# 18:16 probe out of brain

exp1 = celldatabase.Experiment(subject, '2024-10-25', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCateral_DiD', info=['facesLateral', 'soundRight'])
experiments.append(exp1)

exp1.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp1.add_session('15-55-02','a','optoTuningAM','am_tuning_curve')  # went to 460 trials 
exp1.add_session('16-11-49','a','optoNaturalCategories','natural_sound_detection')
exp1.add_session('16-42-25','b','optoTuningFreq','am_tuning_curve')
exp1.add_session('17-00-37','b','optoNaturalInstances','natural_sound_detection')

exp1.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp1.add_session('17-31-21','c','optoTuningAM','am_tuning_curve')  
exp1.add_session('17-45-43','c','optoNaturalCategories','natural_sound_detection')
exp1.add_session('18-13-43','d','optoTuningFreq','am_tuning_curve')
exp1.add_session('18-30-46','d','optoNaturalInstances','natural_sound_detection')

exp1.maxDepth = 4500

# 13:33 animal in the rig
# 13:36 sylgard off
# 13:40 ground wire in the well
# 15:32 probe in the brain
# 15:50 started recording with shanks 1-96
# 17:31 recording with shanks 97-192
# 18:42 finished recording
# 18:55 probe out of brain

exp2 = celldatabase.Experiment(subject, '2024-10-29', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerLateral_DiD', info=['facesMedial', 'soundRight'])
experiments.append(exp2)

exp2.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp2.add_session('15-43-43','a','optoTuningAM','am_tuning_curve')  
exp2.add_session('15-57-43','a','optoNaturalCategories','natural_sound_detection')
exp2.add_session('16-24-34','b','optoTuningFreq','am_tuning_curve')
exp2.add_session('16-41-01','b','optoNaturalInstances','natural_sound_detection')

exp2.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp2.add_session('17-05-11','c','optoTuningAM','am_tuning_curve')  
exp2.add_session('17-19-08','c','optoNaturalCategories','natural_sound_detection')
exp2.add_session('17-46-15','d','optoTuningFreq','am_tuning_curve')
exp2.add_session('18-01-51','d','optoNaturalInstances','natural_sound_detection')

exp2.maxDepth = 4500
# 13:17 animal in the rig
# 13:22 sylgard off
# 13:40 ground wire in the well
# 15:40 probe in the brain
# 15:43 started recording with shanks 1-96
# 17:05 recording with shanks 97-192
# 18:42 finished recording
# 18:55 probe out of brain

exp3 = celldatabase.Experiment(subject, '2024-11-01', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCentral_DiD', info=['facesAnterior', 'soundRight'])
experiments.append(exp3)

exp3.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp3.add_session('10-15-29','a','optoTuningAM','am_tuning_curve')  
exp3.add_session('10-33-25','a','optoNaturalCategories','natural_sound_detection')
exp3.add_session('11-01-13','b','optoTuningFreq','am_tuning_curve')
exp3.add_session('11-23-21','b','optoNaturalInstances','natural_sound_detection')

exp3.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp3.add_session('11-48-17','c','optoTuningAM','am_tuning_curve')  
exp3.add_session('12-05-47','c','optoNaturalCategories','natural_sound_detection')
exp3.add_session('12-32-55','d','optoTuningFreq','am_tuning_curve')
exp3.add_session('12-52-08','d','optoNaturalInstances','natural_sound_detection')

exp3.add_site(3060)
# Reference = 2:tip
# Electrode preset = All Shanks 193-288
exp3.add_session('13-17-29','e','optoTuningAM','am_tuning_curve')  # went to 638

exp3.maxDepth = 4500

# 9:31 animal in the rig
# 9:35 sylgard off
# 9:38 ground wire in the well
# 9:51 probe in the brain
# 10:15 started recording with shanks 1-96
# 11:46 recording with shanks 97-192
# 18:42 finished recording
# 18:55 probe out of brain
