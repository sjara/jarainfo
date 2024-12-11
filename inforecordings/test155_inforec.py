from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'test155'
experiments = []

# This is the first recording with neuropix v.2.
exp0 = celldatabase.Experiment(subject, '2024-12-05', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='CenterLateral_NoDye', info=['facesLateral', 'soundRight'])
experiments.append(exp0)

exp0.add_site(4500)
# Reference = ground
# Electrode preset = All Shanks 1-96
exp0.add_session('10-50-17','a','AM','am_tuning_curve')

exp0.maxDepth = 4500


#13:45 animal kept in the probe.
#15:30 probe at depth 4500um.



#Example
# 10:08 animal in the rig
# 10:23 sylgard off
# 10:35 probe in the brain
# 10:37 ground wire in the well
# 10:45 started recording with shanks 1-96
# 12:05 recording with shanks 97-192
# 12:48 finished recording
# 12:55 probe out of brain
