from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'arch019'
experiments = []

exp0 = celldatabase.Experiment(subject, '2024-11-19', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])
experiments.append(exp0)

exp0.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp0.add_session('11-17-32','a','optoTuningAM','am_tuning_curve')  
exp0.add_session('11-32-45','a','optoNaturalCategories','natural_sound_detection')
exp0.add_session('11-59-42','b','optoTuningFreq','am_tuning_curve')
exp0.add_session('12-15-27','b','optoNaturalInstances','natural_sound_detection')

exp0.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp0.add_session('12-39-04','c','optoTuningAM','am_tuning_curve')  
exp0.add_session('12-54-02','c','optoNaturalCategories','natural_sound_detection')
exp0.add_session('13-20-54','d','optoTuningFreq','am_tuning_curve')
exp0.add_session('14-10-11','d','optoNaturalInstances','natural_sound_detection')

exp0.maxDepth = 4500

# 10:15 animal in the rig
# 10:20 sylgard off
# 10:21 ground wire in the well
# 10:38 probe in the brain
# 11:17 started recording with shanks 1-96
# 12:38 recording with shanks 97-192
# 13:46 finished recording
# 13:55 probe out of brain
# During the laser trials the LFP veiw in the open ephys was decreasing o an extant that in the range of 250 uV was disapearing and we could only monior it in the range of 1000 uV and more. 

exp1 = celldatabase.Experiment(subject, '2024-11-20', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])
experiments.append(exp1)

exp1.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp1.add_session('11-05-27','a','optoTuningAM','am_tuning_curve')  
exp1.add_session('11-21-42','a','optoNaturalCategories','natural_sound_detection') # went to 230 trials
exp1.add_session('11-53-47','b','optoTuningFreq','am_tuning_curve')
exp1.add_session('12-13-30','b','optoNaturalInstances','natural_sound_detection')

exp1.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp1.add_session('12-38-37','c','optoTuningAM','am_tuning_curve')  
exp1.add_session('12-54-15','c','optoNaturalCategories','natural_sound_detection')
exp1.add_session('13-21-27','d','optoTuningFreq','am_tuning_curve') # went to 688 trials
exp1.add_session('13-39-14','d','optoNaturalInstances','natural_sound_detection')

exp1.maxDepth = 4500

# 10:33 animal in the rig
# 10:36 sylgard off
# 10:38 ground wire in the well
# 10:45 probe in the brain
# 11:17 started recording with shanks 1-96
# 12:38 recording with shanks 97-192
# 14:01 finished recording
# 14:08 probe out of brain

exp2 = celldatabase.Experiment(subject, '2024-11-20', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])
experiments.append(exp2)

exp2.add_site(4501)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp2.add_session('15-27-14','e','optoTuningAM','am_tuning_curve')  
exp2.add_session('15-40-59','e','optoNaturalCategories','natural_sound_detection') # went to 230 trials
exp2.add_session('16-09-39','f','optoTuningFreq','am_tuning_curve')
exp2.add_session('16-26-33','f','optoNaturalInstances','natural_sound_detection')

exp2.add_site(3781)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp2.add_session('16-54-30','g','optoTuningAM','am_tuning_curve')  
exp2.add_session('17-09-25','g','optoNaturalCategories','natural_sound_detection')
exp2.add_session('17-37-31','h','optoTuningFreq','am_tuning_curve') # went to 776 trials
exp2.add_session('17-57-18','h','optoNaturalInstances','natural_sound_detection')

exp2.maxDepth = 4501

# 15:05 animal in the rig
# 15:07 sylgard off
# 15:08 ground wire in the well
# 15:20 probe in the brain
# 15:27 started recording with shanks 1-96
# 15:54 recording with shanks 97-192
# 18:22 finished recording
# 18:25 probe out of brain

exp3 = celldatabase.Experiment(subject, '2024-11-21', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundRight'])
experiments.append(exp3)

exp3.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp3.add_session('15-03-36','a','optoTuningAM','am_tuning_curve')  
exp3.add_session('15-17-07','a','optoNaturalCategories','natural_sound_detection') 
exp3.add_session('15-43-51','b','optoTuningFreq','am_tuning_curve')
exp3.add_session('15-59-33','b','optoNaturalInstances','natural_sound_detection')

exp3.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp3.add_session('16-25-52','c','optoTuningAM','am_tuning_curve')  # went to 611 trials
exp3.add_session('16-45-56','c','optoNaturalCategories','natural_sound_detection')
exp3.add_session('17-15-09','d','optoTuningFreq','am_tuning_curve') # went to 843 trials 
exp3.add_session('17-36-28','d','optoNaturalInstances','natural_sound_detection')

exp3.maxDepth = 4500

# 14:28 animal in the rig
# 14:32 sylgard off
# 14:34 ground wire in the well
# 14:42 probe in the brain
# 15:03 started recording with shanks 1-96
# 16:25 recording with shanks 97-192
# 17:58 finished recording
# 18:02 probe out of brain

exp4 = celldatabase.Experiment(subject, '2024-12-04', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_NoDye', info=['facesMedial', 'soundRight'])
experiments.append(exp4)
# This is the control recording without the optogentic inactivation with the laser light.

exp4.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp4.add_session('12-50-01','a','optoTuningAM','am_tuning_curve')  
exp4.add_session('13-06-04','a','optoNaturalCategories','natural_sound_detection') 
exp4.add_session('13-34-29','b','optoTuningFreq','am_tuning_curve')
exp4.add_session('13-51-01','b','optoNaturalInstances','natural_sound_detection')

exp4.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp4.add_session('14-15-13','c','optoTuningAM','am_tuning_curve')  # went to 536 trials
exp4.add_session('14-32-51','c','optoNaturalCategories','natural_sound_detection')
exp4.add_session('15-00-46','d','optoTuningFreq','am_tuning_curve')
exp4.add_session('15-16-22','d','optoNaturalInstances','natural_sound_detection')


exp4.maxDepth = 4500

# 12:12 animal in the rig
# 12:16 sylgard off
# 12:20 ground wire in the well
# 12:42 probe in the brain
# 12:50 started recording with shanks 1-96
# 14:15 recording with shanks 97-192
# 15:41 finished recording
# 15:47 probe out of brain

exp5 = celldatabase.Experiment(subject, '2024-12-06', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_NoDye', info=['facesLateral', 'soundLeft'])
experiments.append(exp5)
# This is the control recording without the optogentic inactivation with the laser light.

exp5.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96 

exp5.add_session('14-06-48','a','optoTuningAM','am_tuning_curve')  # went to 566 trails
exp5.add_session('14-24-52','a','optoNaturalCategories','natural_sound_detection') 
exp5.add_session('14-52-34','b','optoTuningFreq','am_tuning_curve')
exp5.add_session('15-09-55','b','optoNaturalInstances','natural_sound_detection')

exp5.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp5.add_session('15-33-52','c','optoTuningAM','am_tuning_curve')  #went to 380 trials
exp5.add_session('15-48-24','c','optoNaturalCategories','natural_sound_detection')
exp5.add_session('16-40-07','d','optoTuningFreq','am_tuning_curve')
exp5.add_session('16-57-41','d','optoNaturalInstances','natural_sound_detection')


exp5.maxDepth = 4500

# 13:29 animal in the rig
# 13:31 sylgard off
# 13:33 ground wire in the well
# 13:50 probe in the brain
# 14:06 started recording with shanks 1-96
# 15:34 recording with shanks 97-192
# 15:41 finished recording
# 15:47 probe out of brain
