from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'arch013'
experiments = []


exp0 = celldatabase.Experiment(subject, '2024-10-23', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])
experiments.append(exp0)

exp0.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192

# Open ephys crashed for the first time at "16-28-10" 
 
# exp0.add_session('16-31-09','_bad1','AM','am_tuning_curve')
# 395 trials into it but the open ephys crashed.
# the ephys crashed  times at "16-31-09".

exp0.add_session('16-50-11','a','optoTuningAM','am_tuning_curve')
# 403 trials were presented in "16-50-11". 
exp0.add_session('17-08-09','a','optoNaturalCategories','natural_sound_detection')


exp0.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
exp0.add_session('17-40-44','b','optoTuningAM','am_tuning_curve')
# 479 trials were presented in "17-40-44". 
exp0.add_session('17-57-36','b','optoNaturalCategories','am_tuning_curve')
# went to 42 trials and it crashed
exp0.maxDepth = 4500

# 12:55 animal in the rig
# 12:58 sylgard off
#  ground wire in the well
#  probe in the brain
#  started recording with shanks 1-96
#  recording with shanks 97-192
#  finished recording
#  probe out of brain
