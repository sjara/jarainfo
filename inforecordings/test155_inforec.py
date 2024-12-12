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
exp0.add_session('15-53-46','a','AM','am_tuning_curve')
#Reference = 4:tip
exp0.add_session('16-07-12','b','AM','am_tuning_curve')
exp0.maxDepth = 4500

#record time stamps of important events
#13:45 animal kept in the probe.
#15:30 probe at depth 4500um.




