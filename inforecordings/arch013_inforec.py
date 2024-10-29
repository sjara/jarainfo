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

exp2 = celldatabase.Experiment(subject, '2024-10-29', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCateral_DiO', info=['facesMedial', 'soundRight'])
experiments.append(exp2)

exp2.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp2.add_session('','a','optoTuningAM','am_tuning_curve')  # went to 460 trials 
exp2.add_session('','a','optoNaturalCategories','natural_sound_detection')
exp2.add_session('','b','optoTuningFreq','am_tuning_curve')
exp2.add_session('','b','optoNaturalInstances','natural_sound_detection')

exp2.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp2.add_session('','c','optoTuningAM','am_tuning_curve')  
exp2.add_session('','c','optoNaturalCategories','natural_sound_detection')
exp2.add_session('','d','optoTuningFreq','am_tuning_curve')
exp2.add_session('','d','optoNaturalInstances','natural_sound_detection')

exp2.maxDepth = 4500
# 9:55 animal in the rig
# 9:58 sylgard off
# 13:40 ground wire in the well
# 15:32 probe in the brain
# 15:50 started recording with shanks 1-96
# 17:31 recording with shanks 97-192
# 18:42 finished recording
# 18:55 probe out of brain
