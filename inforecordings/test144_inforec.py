from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'test144'
experiments = []

# This is the first recording with neuropix v.2.
exp0 = celldatabase.Experiment(subject, '2024-08-26', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundLeft'])
experiments.append(exp0)

exp0.add_site(4500)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
exp0.add_session('10-50-17','a','AM','am_tuning_curve')
exp0.add_session('10-58-13','b','pureTones','am_tuning_curve')
exp0.add_session('11-08-09','a','naturalSound','natural_sound_detection')
exp0.add_site(3780)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp0.add_session('12-22-56','c','AM','am_tuning_curve')
exp0.add_session('12-30-21','d','pureTones','am_tuning_curve')
exp0.maxDepth = 4500

# 10:08 animal in the rig
# 10:23 sylgard off
# 10:35 probe in the brain
# 10:37 ground wire in the well
# 10:45 started recording with shanks 1-96
# 12:05 recording with shanks 97-192
# 12:48 finished recording
# 12:55 probe out of brain

exp1 = celldatabase.Experiment(subject, '2024-08-26', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='centerLateral_DiI', info=['facesMedial', 'soundLeft'])
experiments.append(exp1)

exp1.add_site(4501)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
# the sync light was on for the whole experiment.
# The probe was inserted 4000 but not many spikes were observed so we moved it more lateral. 
exp1.add_session('16-55-48','e','AM','am_tuning_curve')
exp1.add_session('17-05-20','f','pureTones','am_tuning_curve')
exp1.add_session('17-21-40','b','naturalSound','natural_sound_detection')

exp1.add_site(3781)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp1.add_session('17-49-06','g','AM','am_tuning_curve')
exp1.add_session('17-57-53','h','pureTones','am_tuning_curve')
exp1.add_session('18-06-13','c','naturalSound','natural_sound_detection')
exp1.maxDepth = 4500

# 10:08 animal in the rig
# 10:23 sylgard off
# 10:35 probe in the brain
# 10:37 ground wire in the well
# 10:45 started recording with shanks 1-96
# 11:38 recording with shanks 97-192
# 12:35 finished recording
# 12:40 probe out of brain

exp2 = celldatabase.Experiment(subject, '2024-08-27', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])
experiments.append(exp2)

exp2.add_site(4000)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
# the sync light was on for the whole experiment.
# The probe was inserted 4000 but not many spikes were observed so we moved it more lateral.
# first AM tuning went to 282 trials. Second AM tuning went to 244 trials.
#  
exp2.add_session('13-24-15','a','AM','am_tuning_curve')
exp2.add_session('13-33-42','b','pureTones','am_tuning_curve')
exp2.add_session('13-43-43','a','naturalSound','natural_sound_detection')

exp2.add_site(3280)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp2.add_session('14-11-50','c','AM','am_tuning_curve')
exp2.add_session('14-21-20','d','pureTones','am_tuning_curve')
exp2.add_session('14-30-43','b','naturalSound','natural_sound_detection')
exp2.maxDepth = 4000

# 13:01 animal in the rig
# 13:05 sylgard off
# 13:07 ground wire in the well
# 13:24 probe in the brain
# 13:30 started recording with shanks 1-96
# 14:12 recording with shanks 97-192
# 14:53 finished recording
# 14:57 probe out of brain

exp3 = celldatabase.Experiment(subject, '2024-08-28', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='CenterLateral_DiI', info=['facesMedial', 'soundRight'])
experiments.append(exp3)

exp3.add_site(4000)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
# the sync light was on for the whole experiment. 
exp3.add_session('11-05-55','a','AM','am_tuning_curve')
exp3.add_session('11-13-34','b','pureTones','am_tuning_curve')
exp3.add_session('13-43-43','a','naturalSound','natural_sound_detection')

exp3.add_site(3280)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp3.add_session('11-50-38','c','AM','am_tuning_curve')
exp3.add_session('11-58-04','d','pureTones','am_tuning_curve')
exp3.add_session('12-06-41','b','naturalSound','natural_sound_detection')
exp3.maxDepth = 4000

# 10:30 animal in the rig
# 10:37 sylgard off
# 10:40 ground wire in the well
# 10:55 probe in the brain
# 11:05 started recording with shanks 1-96
# 12:12 recording with shanks 97-192
# 12:53 finished recording
# 12:57 probe out of brain
