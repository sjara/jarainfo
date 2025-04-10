from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'arch024'
experiments = []

#day 1- right hemisphere, recorded from centre of craniotomy,shanks parallet to bregma lambda axis. 
exp0 = celldatabase.Experiment(subject, '2025-04-10', brainArea='right_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundLeft'])
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
# reference = 1:tip
# Electrode preset = All Shanks 97-192
exp0.add_session('13-32-19','c','optoTuningAM','am_tuning_curve') 
exp0.add_session('13-47-10','c','optoNaturalCategories','natural_sound_detection')
exp0.add_session('14-14-23','d','optoTuningFreq','am_tuning_curve')
exp0.add_session('14-30-43','d','optoNaturalInstances','natural_sound_detection')

exp0.maxDepth = 3500

# probe in brain around 11:14am

# exp 0 finish
# =================================2025-04-11============================================
