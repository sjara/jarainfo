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

exp1 = celldatabase.Experiment(subject, '2024-07-26', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='posteriorcoronal_DiI', info=['facesanterior', 'soundRight'])
experiments.append(exp1)

exp1.add_site(3000)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
exp1.add_session('16-27-43','a','AM','am_tuning_curve')
exp1.add_session('16-39-03','b','pureTones','am_tuning_curve')
exp1.add_session('16-50-44','a','naturalSound','natural_sound_detection')

exp1.add_site(2280)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp1.add_session('17-22-34','c','AM','am_tuning_curve')
exp1.add_session('17-31-33','d','pureTones','am_tuning_curve')
exp1.add_session('17-40-55','b','naturalSound','natural_sound_detection')
exp1.maxDepth = 3000

# 15:07 animal in the rig
# 15:15 sylgard off
# 15:48 probe in the brain
# 15:55 ground wire in the well
# 16:25 started recording with shanks 1-96
# 17:22 recording with shanks 97-192
# 18:12 finished recording
# 18:19 probe out of brain

exp2 = celldatabase.Experiment(subject, '2024-07-30', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='posteriormedial_DiD', info=['facesAnterior', 'soundRight'])
experiments.append(exp2)

exp2.add_site(4000)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
exp2.add_session('11-48-08','a','AM','am_tuning_curve')
exp2.add_session('11-56-51','b','pureTones','am_tuning_curve')
exp2.add_session('12-07-07','a','naturalSound','natural_sound_detection')

exp2.add_site(3280)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp2.add_session('12-35-13','c','AM','am_tuning_curve')
exp2.add_session('12-43-24','d','pureTones','am_tuning_curve')
exp2.add_session('12-52-54','b','naturalSound','natural_sound_detection')

exp2.add_site(2560)
# Reference = 2:tip
# Electrode preset = All Shanks 193-288
exp2.add_session('13-23-10','e','AM','am_tuning_curve')
exp2.add_session('13-31-03','f','pureTones','am_tuning_curve')
exp2.add_session('13-39-45','c','naturalSound','natural_sound_detection')

exp2.add_site(1840)
# Reference = 2:tip
# Electrode preset = All Shanks 289-384
exp2.add_session('14-09-20','g','AM','am_tuning_curve')

exp2.add_site(1120)
# Reference = 2:tip
# Electrode preset = All Shanks 385-480
exp2.add_session('14-18-41','h','AM','am_tuning_curve')
exp2.maxDepth = 4000

# 9:04 painting the probe
# 9:15 animal in the rig
# 9:17 sylgard off
# 9:55 the probe didn't penetrate the right craniotomy. we went for the left craniotomy
# 10:03 probe in the brain
# 10:27 reached 4000
# 10:33 ground wire in the well
# 14:25 finished recording
# 14:30 probe out of brain

