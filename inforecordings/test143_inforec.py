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

exp3 = celldatabase.Experiment(subject, '2024-07-31', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='medial_DiI', info=['facesMedial', 'soundLeft'])
experiments.append(exp3)

exp3.add_site(4000)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
exp3.add_session('12-06-01','a','AM','am_tuning_curve')
exp3.add_session('12-13-41','b','pureTones','am_tuning_curve')
exp3.add_session('12-23-41','a','naturalSound','natural_sound_detection')

exp3.add_site(3280)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp3.add_session('12-52-03','c','AM','am_tuning_curve')
exp3.add_session('13-00-01','d','pureTones','am_tuning_curve')
exp3.add_session('13-09-04','b','naturalSound','natural_sound_detection')

exp3.add_site(2560)
# Reference = 2:tip
# Electrode preset = All Shanks 193-288
exp3.add_session('13-37-05','e','AM','am_tuning_curve')
exp3.add_session('13-48-00','f','pureTones','am_tuning_curve')
exp3.add_session('13-56-47','c','naturalSound','natural_sound_detection')

exp3.add_site(1840)
# Reference = 2:tip
# Electrode preset = All Shanks 289-384
exp3.add_session('14-24-14','g','AM','am_tuning_curve')

exp3.add_site(1120)
# Reference = 2:tip
# Electrode preset = All Shanks 385-480
exp3.add_session('14-31-58','h','AM','am_tuning_curve')
exp3.maxDepth = 4000

# 9:18 painting the probe
# 9:26 animal in the rig
# 9:29 sylgard off
# 10:34 finish haircut so it doesn't interfere with recording
# 10:54 inserting the probe in the brain
# 11:23 probe started bending at 1580
# 11:43 removing dura and scar tissue
# 11:47 probe in the brain
# 12:02 ground wire in the well

exp4 = celldatabase.Experiment(subject, '2024-08-01', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='lateral_DiD', info=['facesLateral', 'soundLeft'])
experiments.append(exp4)

exp4.add_site(4000)
# Reference = 2:tip
# Electrode preset = All Shanks 1-96
exp4.add_session('16-04-27','a','AM','am_tuning_curve')
exp4.add_session('16-12-43','b','pureTones','am_tuning_curve')
exp4.add_session('16-21-20','a','naturalSound','natural_sound_detection')

exp4.add_site(3280)
# Reference = 2:tip
# Electrode preset = All Shanks 97-192
exp4.add_session('16-49-58','c','AM','am_tuning_curve')
exp4.add_session('17-03-07','d','pureTones','am_tuning_curve')
exp4.add_session('17-11-36','b','naturalSound','natural_sound_detection')

exp4.add_site(2560)
# Reference = 2:tip
# Electrode preset = All Shanks 193-288
exp4.add_session('17-39-49','e','AM','am_tuning_curve')
exp4.add_session('17-47-20','f','pureTones','am_tuning_curve')
exp4.add_session('17-55-59','c','naturalSound','natural_sound_detection')

exp4.add_site(1840)
# Reference = 2:tip
# Electrode preset = All Shanks 289-384
exp4.add_session('18-24-20','g','AM','am_tuning_curve')

exp4.add_site(1120)
# Reference = 2:tip
# Electrode preset = All Shanks 385-480
exp4.add_session('18-32-09','h','AM','am_tuning_curve')
exp4.maxDepth = 4000

# 9:18 painting the probe
# 9:26 animal in the rig
# 9:29 sylgard off
# 10:34 finish haircut so it doesn't interfere with recording
# 10:54 inserting the probe in the brain
# 11:23 probe started bending at 1580
# 11:43 removing dura and scar tissue
# 11:47 probe in the brain
# 12:02 ground wire in the well
# 12:06 started recording
# 14:40 probe out of brain

