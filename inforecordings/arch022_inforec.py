from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'arch022'
experiments = []


exp0 = celldatabase.Experiment(subject, '2025-03-13', brainArea='left_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])
experiments.append(exp0)

exp0.add_site(2780)
# what is site number for 1-96 and what for 97-192?
# Reference = 1:tip
# Electrode preset = All Shanks 97-192 

exp0.add_session('13-24-08','a','optoTuningAM','am_tuning_curve')  
exp0.add_session('13-42-12','a','optoNaturalCategories','natural_sound_detection')
exp0.add_session('14-22-00','b','optoTuningFreq','am_tuning_curve')
#665 trials recorded.
exp0.add_session('14-39-45','b','optoNaturalInstances','natural_sound_detection')

exp0.add_site(3500)

# Reference = 1:tip
# Electrode preset = All Shanks 1-96
exp0.add_session('15-06-32','c','optoTuningAM','am_tuning_curve') 
exp0.add_session('15-23-05','c','optoNaturalCategories','natural_sound_detection')
exp0.add_session('15-50-29','d','optoTuningFreq','am_tuning_curve')
exp0.add_session('16-06-29','d','optoNaturalInstances','natural_sound_detection')

exp0.maxDepth = 3500

# probe in brain around 13:00 pm
# 13:24 started recording with shanks 97-192
# 15:06- started optonatural categories for shank 1-96.
# 16:38 probe out of brain
# exp 0 finish
