from jaratoolbox import celldatabase

subject = 'poni008'
experiments=[]

probe_tip = 2974 # max depth is same for all experiments since the probe is implanted!

# probe #23299112211

### 2025-11-10 Session ###
exp0 = celldatabase.Experiment(subject, '2025-11-10', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2211',
                               info = ['faceRight','soundLeft','closedField'])
exp0.maxDepth=probe_tip

# Animal in rig at 1330

exp0.add_site(1530) # tip 1 ref
exp0.add_session('14-13-00', 'a', 'tuningFreq', 'am_tuning_curve') # 40 dB
exp0.add_session('14-21-07', 'b', 'tuningAM', 'am_tuning_curve') # 40 dB
exp0.add_session('14-28-42', 'a', 'naturalSound', 'natural_sound_detection') # 40 dB


# mouse out 1500
experiments.append(exp0)




