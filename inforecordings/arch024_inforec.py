from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'arch024'
experiments = []

#day 1- right hemisphere, recorded from 0.2mm lateral from centre of craniotomy,shanks parallet to bregma lambda axis. 
exp0 = celldatabase.Experiment(subject, '2025-04-10', brainArea='right_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiD', info=['facesLateral', 'soundLeft'])
experiments.append(exp0)

exp0.add_site(3500)

# Reference = 4:tip
# Electrode preset = All Shanks 1-96 

exp0.add_session('11-25-33','a','optoTuningAM','am_tuning_curve')  
# extra recoding. All data are present. 12-47-46 for optoTuningAM Full recording data+video+ behavior file
exp0.add_session('11-41-40','a','optoNaturalCategories','natural_sound_detection')
# extra recording. All data are present. 13-02-41 for optoNatural Categories. Full recording data+video+behavior file
exp0.add_session('12-09-46','b','optoTuningFreq','am_tuning_curve')
exp0.add_session('12-25-46','b','optoNaturalInstances','natural_sound_detection')

exp0.add_site(2780)
# reference = 4:tip
# Electrode preset = All Shanks 97-192
exp0.add_session('13-32-19','c','optoTuningAM','am_tuning_curve') 
exp0.add_session('13-47-10','c','optoNaturalCategories','natural_sound_detection')
exp0.add_session('14-14-23','d','optoTuningFreq','am_tuning_curve')
exp0.add_session('14-30-43','d','optoNaturalInstances','natural_sound_detection')

exp0.maxDepth = 3500

# probe in brain around 11:14am

# exp 0 finish
# =================================2025-04-11============================================
#day 2- right hemisphere, recorded from centre of craniotomy,shanks parallet to bregma lambda axis. Centre of craniotomy.
exp1 = celldatabase.Experiment(subject, '2025-04-11', brainArea='right_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundLeft'])
experiments.append(exp1)

exp1.add_site(3500)

# Reference = 4:tip
# Electrode preset = All Shanks 1-96 

exp1.add_session('10-27-42','a','optoTuningAM','am_tuning_curve')  
exp1.add_session('10-42-52','a','optoNaturalCategories','natural_sound_detection')
exp1.add_session('11-10-19','b','optoTuningFreq','am_tuning_curve')
exp1.add_session('11-26-20','b','optoNaturalInstances','natural_sound_detection')

exp1.add_site(2780)
# reference = 4:tip
# Electrode preset = All Shanks 97-192
exp1.add_session('11-50-40','c','optoTuningAM','am_tuning_curve') 
exp1.add_session('12-05-09','c','optoNaturalCategories','natural_sound_detection')
exp1.add_session('12-32-15','d','optoTuningFreq','am_tuning_curve')
exp1.add_session('12-48-32','d','optoNaturalInstances','natural_sound_detection')

exp1.maxDepth = 3600



# exp 1 finish
# =================================2025-04-14============================================
#day 3- right hemisphere-Control experiment, recorded from centre of craniotomy,shanks parallet to bregma lambda axis. Centre of craniotomy.
exp2 = celldatabase.Experiment(subject, '2025-04-14', brainArea='right_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiO', info=['facesLateral', 'soundLeft'])
experiments.append(exp2)

exp2.add_site(3500)

# Reference = 4:tip
# Electrode preset = All Shanks 1-96 

exp2.add_session('11-32-37','a','optoTuningAM','am_tuning_curve')  
exp2.add_session('11-47-08','a','optoNaturalCategories','natural_sound_detection')
exp2.add_session('12-15-31','b','optoTuningFreq','am_tuning_curve')
exp2.add_session('12-31-13','b','optoNaturalInstances','natural_sound_detection')

exp2.add_site(2780)
# reference = 4:tip
# Electrode preset = All Shanks 97-192
exp2.add_session('12-57-10','c','optoTuningAM','am_tuning_curve') 
# 730 trials was recorded because I was i lab meeting.
exp2.add_session('13-20-14','c','optoNaturalCategories','natural_sound_detection')
exp2.add_session('13-51-13','d','optoTuningFreq','am_tuning_curve')
exp2.add_session('14-07-06','d','optoNaturalInstances','natural_sound_detection')

exp2.maxDepth = 3500



# exp 2 finish
# =================================2025-04-15============================================

#day 4- left hemisphere-, recorded from centre of craniotomy,shanks parallet to bregma lambda axis. Centre of craniotomy.
exp3 = celldatabase.Experiment(subject, '2025-04-15', brainArea='left_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])
experiments.append(exp3)

exp3.add_site(3500)

# Reference = 4:tip
# Electrode preset = All Shanks 1-96 

exp3.add_session('11-18-05','a','optoTuningAM','am_tuning_curve')  
exp3.add_session('11-32-19','a','optoNaturalCategories','natural_sound_detection')
exp3.add_session('12-00-21','b','optoTuningFreq','am_tuning_curve')
exp3.add_session('12-17-15','b','optoNaturalInstances','natural_sound_detection')

exp3.add_site(2780)
# reference = 4:tip
# Electrode preset = All Shanks 97-192
exp3.add_session('12-40-44','c','optoTuningAM','am_tuning_curve') 
exp3.add_session('12-55-06','c','optoNaturalCategories','natural_sound_detection')
exp3.add_session('13-22-38','d','optoTuningFreq','am_tuning_curve')
exp3.add_session('13-38-33','d','optoNaturalInstances','natural_sound_detection')

exp3.maxDepth = 3500



# exp 3 finish
# =================================2025-04-16============================================
#day 5- left hemisphere-, recorded from 0.3mm lateral from centre of craniotomy,shanks parallet to bregma lambda axis.
exp4 = celldatabase.Experiment(subject, '2025-04-16', brainArea='left_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesLateral', 'soundRight'])
experiments.append(exp4)

exp4.add_site(3500)

# Reference = 4:tip
# Electrode preset = All Shanks 1-96 

exp4.add_session('10-57-38','a','optoTuningAM','am_tuning_curve')  
exp4.add_session('11-12-51','a','optoNaturalCategories','natural_sound_detection')
exp4.add_session('11-40-52','b','optoTuningFreq','am_tuning_curve')
exp4.add_session('11-57-09','b','optoNaturalInstances','natural_sound_detection')

exp4.add_site(2780)
# reference = 4:tip
# Electrode preset = All Shanks 97-192
exp4.add_session('12-20-27','c','optoTuningAM','am_tuning_curve') 
exp4.add_session('12-34-56','c','optoNaturalCategories','natural_sound_detection')
exp4.add_session('13-02-44','d','optoTuningFreq','am_tuning_curve')
exp4.add_session('13-18-59','d','optoNaturalInstances','natural_sound_detection')

exp4.maxDepth = 3500



# exp 4 finish
# =================================2025-04-17============================================
#day 5- left hemisphere-, recorded from centre of craniotomy,shanks parallet to bregma lambda axis.
exp5 = celldatabase.Experiment(subject, '2025-04-17', brainArea='left_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiO', info=['facesMedial', 'soundRight'])
experiments.append(exp5)

exp5.add_site(3500)

# Reference = 4:tip
# Electrode preset = All Shanks 1-96 

exp5.add_session('11-13-34','a','optoTuningAM','am_tuning_curve')  
exp5.add_session('11-27-53','a','optoNaturalCategories','natural_sound_detection')
exp5.add_session('11-57-44','b','optoTuningFreq','am_tuning_curve')
exp5.add_session('12-13-28','b','optoNaturalInstances','natural_sound_detection')

exp5.add_site(2780)
# reference = 1:tip # less noisy channels
# Electrode preset = All Shanks 97-192
exp5.add_session('12-40-29','c','optoTuningAM','am_tuning_curve') 
exp5.add_session('12-54-40','c','optoNaturalCategories','natural_sound_detection')
exp5.add_session('13-22-41','d','optoTuningFreq','am_tuning_curve')
exp5.add_session('13-38-14','d','optoNaturalInstances','natural_sound_detection')

exp5.maxDepth = 3500



# exp 5 finish
