"""
test155
"""

from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'test155'
experiments = []

# exp start
# This is the first recording with neuropix v.2.
exp0 = celldatabase.Experiment(subject, '2024-12-05', brainArea='left_pStr', probe = 'NPv2-0282', recordingTrack='CenterLateral_NoDye', info=['facesLateral', 'soundRight'])
experiments.append(exp0)
# record time stamps of important events
# 13:45 animal kept in the probe.
# 15:30 probe at depth 4500um.

exp0.add_site(4500)
# Reference = ground
# Electrode preset = All Shanks 1-96
exp0.add_session('15-53-46','a','AM','am_tuning_curve')

exp0.add_site(4501)
# Reference = 4:tip
# Electrode preset = All Shanks 1-96
exp0.add_session('16-07-12','b','AM','am_tuning_curve')

exp0.maxDepth = 4500
# exp end

# exp start
exp1 = celldatabase.Experiment(subject, '2024-12-20', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='CenterLateral_NoDye', info=['facesLateral', 'sound_binaural'])
experiments.append(exp1)

exp1.add_site(4500)
# Reference = 1:tip
# Electrode preset = Shank 1 Bank A
exp1.add_session('16-18-23','a','AM','am_tuning_curve')
# After stopping the recording, I started the sound presentation again (run for two trials) before saving the sound presentation. So the sound presentation includes 238+2 trials (but ephys only 238).
exp1.add_session('16-29-20','b','AM','am_tuning_curve')

exp1.maxDepth = 4500
# There were two additional sessions (<1min each) recorded by mistake. These have been deleted.
# exp end

# exp start
exp2 = celldatabase.Experiment(subject, '2024-12-26', brainArea='right_pStr', probe = 'NPv2-0282', recordingTrack='CenterLateral_DiD', info=['facesLateral', 'sound_binaural'])
experiments.append(exp2)
exp2.add_site(4500)
# Reference = 1:tip
# Electrode preset = Shank 1 Bank A
exp2.add_session('13-56-22','a','AM','am_tuning_curve')
#exp2.add_session('14-05-28','y','AM','am_tuning_curve')   # Sound presentation not saved.
#exp2.add_session('14-14-49','x','AM','am_tuning_curve')  # 224 trials
exp2.add_session('14-25-46','b','AM','am_tuning_curve')
#12-05-28 is the wrong session as i terminated the sound presentation without saving it. So, recording new one. I had recorded 220 trails, but terminated sound data without saving it.
#hence, with this, the video and recording "20241226-08" is waste.

# The next two sessions, I wanted to check how the same neurons behaved spiked when the sound was presented from only left ear instead of binaural as I did in above two sessions. So, next 'c' and 'd' are recordings with sound presentation from left.
exp2.add_session('14-35-21','c','AM','am_tuning_curve')
exp2.add_session('14-43-35','d','AM','am_tuning_curve')
exp2.maxDepth = 4500
#exp end

