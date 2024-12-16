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
exp1.add_session('','d','optoNaturalInstances','natural_sound_detection')

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
