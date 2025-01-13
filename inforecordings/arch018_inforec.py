from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'arch018'
experiments = []


exp0 = celldatabase.Experiment(subject, '2024-12-09', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])
experiments.append(exp0)

exp0.add_site(4500)
# Reference = 4:tip
# Electrode preset = All Shanks 1-96 

exp0.add_session('11-19-33','a','optoTuningAM','am_tuning_curve')  
exp0.add_session('11-33-51','a','optoNaturalCategories','natural_sound_detection')
exp0.add_session('12-01-02','b','optoTuningFreq','am_tuning_curve')
exp0.add_session('12-18-27','b','optoNaturalInstances','natural_sound_detection')

exp0.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp0.add_session('12-45-28','c','optoTuningAM','am_tuning_curve')  
exp0.add_session('12-59-14','c','optoNaturalCategories','natural_sound_detection')
exp0.add_session('13-26-50','d','optoTuningFreq','am_tuning_curve')
exp0.add_session('13-42-27','d','optoNaturalInstances','natural_sound_detection')

exp0.maxDepth = 4500

# 10:12 animal in the rig
# 10:17 sylgard off
# 10:27 ground wire in the well
# 11:04 probe in the brain
# 11:19 started recording with shanks 1-96
# 12:45 recording with shanks 97-192
# 14:12 finished recording
# 14:18 probe out of brain

exp1 = celldatabase.Experiment(subject, '2024-12-10', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])
experiments.append(exp1)

exp1.add_site(4500)
# Reference = 4:tip
# Electrode preset = All Shanks 1-96 

exp1.add_session('11-18-35','a','optoTuningAM','am_tuning_curve')  
exp1.add_session('11-34-26','a','optoNaturalCategories','natural_sound_detection')
exp1.add_session('12-01-00','b','optoTuningFreq','am_tuning_curve')
exp1.add_session('12-17-22','b','optoNaturalInstances','natural_sound_detection')

exp1.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp1.add_session('12-39-32','c','optoTuningAM','am_tuning_curve')  
exp1.add_session('12-59-00','c','optoNaturalCategories','natural_sound_detection')
exp1.add_session('13-25-52','d','optoTuningFreq','am_tuning_curve')
exp1.add_session('13-41-12','d','optoNaturalInstances','natural_sound_detection')

exp1.maxDepth = 4500

# 10:12 animal in the rig
# 10:17 sylgard off
# 10:27 ground wire in the well
# 11:04 probe in the brain
# 11:19 started recording with shanks 1-96
# 12:45 recording with shanks 97-192
# 14:12 finished recording
# 14:18 probe out of brain

exp2 = celldatabase.Experiment(subject, '2024-12-16', brainArea='right_pStr', probe = 'NPv2-0312', recordingTrack='centerCenter_NoDye', info=['facesLateral', 'soundLeft'])
experiments.append(exp2)

exp2.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp2.add_session('11-48-33','a','optoTuningAM','am_tuning_curve')  
exp2.add_session('12-02-58','a','optoNaturalCategories','natural_sound_detection')
exp2.add_session('12-42-38','b','optoTuningFreq','am_tuning_curve')
exp2.add_session('13-02-32','b','optoNaturalInstances','natural_sound_detection') # went to 272

exp2.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp2.add_session('13-38-41','c','optoTuningAM','am_tuning_curve')  
exp2.add_session('13-52-48','c','optoNaturalCategories','natural_sound_detection')
exp2.add_session('14-19-13','d','optoTuningFreq','am_tuning_curve')
exp2.add_session('14-41-18','d','optoNaturalInstances','natural_sound_detection')

exp2.maxDepth = 4500

# 10:30 animal in the rig
# 10:31 sylgard off
# 10:35 ground wire in the well
# 11:12 probe in the brain
# 11:42 started recording with shanks 1-96
# 12:45 recording with shanks 97-192
# 14:12 finished recording
# 14:18 probe out of brain

exp3 = celldatabase.Experiment(subject, '2024-12-17', brainArea='left_pStr', probe = 'NPv2-0312', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])
experiments.append(exp3)

exp3.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp3.add_session('12-26-49','a','optoTuningAM','am_tuning_curve')  
exp3.add_session('12-40-22','a','optoNaturalCategories','natural_sound_detection')
exp3.add_session('13-07-41','b','optoTuningFreq','am_tuning_curve')
exp3.add_session('13-22-56','b','optoNaturalInstances','natural_sound_detection') # went to 272

exp3.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp3.add_session('13-47-09','c','optoTuningAM','am_tuning_curve') # went to 1190 
exp3.add_session('14-02-46','c','optoNaturalCategories','natural_sound_detection')
exp3.add_session('14-29-53','d','optoTuningFreq','am_tuning_curve')
exp3.add_session('14-45-03','d','optoNaturalInstances','natural_sound_detection')

exp3.maxDepth = 4500

# 11:22 animal in the rig
# 11:33 sylgard off
# 11:42 ground wire in the well
# 12:09 probe in the brain
# 12:26 started recording with shanks 1-96
# 13:47 recording with shanks 97-192
# 14:45 finished recording
# 14:58 probe out of brain

exp4 = celldatabase.Experiment(subject, '2024-12-18', brainArea='left_pStr', probe = 'NPv2-0312', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundRight'])
experiments.append(exp4)

exp4.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp4.add_session('10-41-53','a','optoTuningAM','am_tuning_curve')  
exp4.add_session('10-55-57','a','optoNaturalCategories','natural_sound_detection')
exp4.add_session('11-25-54','b','optoTuningFreq','am_tuning_curve')
exp4.add_session('11-41-11','b','optoNaturalInstances','natural_sound_detection') # went to 272

exp4.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp4.add_session('13-12-51','c','optoTuningAM','am_tuning_curve') # went to 1190 
exp4.add_session('13-27-22','c','optoNaturalCategories','natural_sound_detection')
exp4.add_session('13-54-41','d','optoTuningFreq','am_tuning_curve')
exp4.add_session('14-11-01','d','optoNaturalInstances','natural_sound_detection')

exp4.maxDepth = 4500

# 10:12 animal in the rig
# 10:13 sylgard off
# 10:17 ground wire in the well
# 10:25 probe in the brain
# 10:41 started recording with shanks 1-96
# 13:47 recording with shanks 97-192
# 15:04 finished recording
# 15:12 probe out of brain

exp5 = celldatabase.Experiment(subject, '2025-01-12', brainArea='left_pStr', probe = 'NPv2-0312', recordingTrack='centerCenter_NoDye', info=['facesMedial', 'soundRight'])
experiments.append(exp5)

exp5.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp5.add_session('13-36-44','a','optoTuningAM','am_tuning_curve')  
exp5.add_session('13-53-58','a','optoNaturalCategories','natural_sound_detection')
exp5.add_session('14-21-31','b','optoTuningFreq','am_tuning_curve')
exp5.add_session('14-37-30','b','optoNaturalInstances','natural_sound_detection') # went to 272

exp5.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp5.add_session('15-04-07','c','optoTuningAM','am_tuning_curve') # went to 1190 
exp5.add_session('15-18-07','c','optoNaturalCategories','natural_sound_detection')
exp5.add_session('15-44-43','d','optoTuningFreq','am_tuning_curve')
exp5.add_session('15-59-56','d','optoNaturalInstances','natural_sound_detection')

exp5.maxDepth = 4500

# 11:56 animal in the rig
# 12:05 sylgard off
# 12:11 ground wire in the well
# 12:23 probe in the brain
# 13:36 started recording with shanks 1-96
# 15:04 recording with shanks 97-192
# 16:21 finished recording
# 16:25 probe out of brain
