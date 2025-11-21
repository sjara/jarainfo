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


### 2025-11-13 Session ###
exp1 = celldatabase.Experiment(subject, '2025-11-13', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2211',
                               info = ['faceRight','soundLeft','closedField'])
exp1.maxDepth=probe_tip

# Animal in rig at 0910

exp1.add_site(1530) # tip 1 ref
exp1.add_session('09-33-53', 'a', 'tuningAMtone', 'am_tuning_curve') # 40 dB


# mouse out 1025
experiments.append(exp1)


### 2025-11-17 Session ###
exp2 = celldatabase.Experiment(subject, '2025-11-17', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2211',
                               info = ['faceRight','soundLeft','closedField'])
exp2.maxDepth=probe_tip

# Animal in rig at 0945

exp2.add_site(1530) # tip 1 ref
exp2.add_session('09-56-20', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 40 dB
exp2.add_session('11-06-58', 'b', 'optoTuningFreq', 'am_tuning_curve') # 40 dB


# mouse out 1150
experiments.append(exp2)


### 2025-11-19 Session ###
exp3 = celldatabase.Experiment(subject, '2025-11-19', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2211',
                               info = ['faceRight','soundLeft','closedField'])
exp3.maxDepth=probe_tip

# Animal in rig at 0930

exp3.add_site(1530) # tip 1 ref
exp3.add_session('09-39-13', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 40 dB
exp3.add_session('10-48-49', 'b', 'optoTuningFreq', 'am_tuning_curve') # 40 dB


# mouse out 1130
experiments.append(exp3)


### 2025-11-21 Session ###
exp4 = celldatabase.Experiment(subject, '2025-11-21', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2211',
                               info = ['faceRight','soundLeft','closedField'])
exp4.maxDepth=probe_tip

# Animal in rig at 1030

exp4.add_site(1530) # tip 1 ref
exp4.add_session('10-41-56', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 40 dB
exp4.add_session('11-51-39', 'b', 'optoTuningFreq', 'am_tuning_curve') # 40 dB

# noticed squeaking from the wheel at the end, not sure if it was present throughout the session

# mouse out 1232
experiments.append(exp4)




