from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'test143'
experiments = []

# This is the first recording with neuropix v.2.
exp0 = celldatabase.Experiment(subject, '2024-07-19', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='NoDye', info=['facesMedial', 'soundLeft'])
experiments.append(exp0)

exp0.add_site(3000)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
exp0.add_session('17-14-07','a','AM','am_tuning_curve')

exp0.add_site(3000-720)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192

# For '17-14-07' we forgot to press pluse in openephys, it got recorded as experiment2
# exp0.add_session('17-14-07','b','AM','am_tuning_curve')
exp0.add_session('18-12-36','c','AM','am_tuning_curve')
exp0.add_session('18-29-22','d','pureTones','am_tuning_curve')


exp0.maxDepth = 3000


# 15:00 animal in the rig
# 15:30 probe insertion facing anterior
# 16:15 the shank on the right started bending at 600-700 um:
# 16:45 reached 3000
# 17:00 started recording
# 18:45 finished recording
# 18:51 probe out of brain
