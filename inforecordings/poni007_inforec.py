from jaratoolbox import celldatabase

subject = 'poni007'
experiments=[]

probe_tip = 3024 # max depth is same for all experiments since the probe is implanted!


### 2025-09-15 Session ###
exp0 = celldatabase.Experiment(subject, '2025-09-15', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight'])
exp0.maxDepth=probe_tip

# Animal in rig at 1200
# exp0.add_site(3023) # tip 3 ref
# exp0.add_session('12-39-15', 'a', 'tuningFreq', 'am_tuning_curve')

exp0.add_site(2300) # tip 3 ref
exp0.add_session('12-49-35', 'b', 'tuningFreq', 'am_tuning_curve') # accidentally did sound left :(

experiments.append(exp0)


# mouse out 1258

### 2025-09-29 Session ###
exp1 = celldatabase.Experiment(subject, '2025-09-29', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight'])
exp1.maxDepth=probe_tip

# Animal in rig at 1330
# exp0.add_site(3023) # tip 3 ref
# exp0.add_session('12-39-15', 'a', 'tuningFreq', 'am_tuning_curve')

exp1.add_site(2300) # tip 3 ref
exp1.add_session('13-34-29', 'a', 'tuningFreq', 'am_tuning_curve') 
exp1.add_session('13-43-02', 'b', 'tuningAM', 'am_tuning_curve') 
exp1.add_session('13-51-46', 'a', 'naturalSound', 'natural_sound_detection') 
experiments.append(exp1)


# mouse out 1420



### 2025-10-14 Session ###
exp2 = celldatabase.Experiment(subject, '2025-10-14', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight'])
exp2.maxDepth=probe_tip

# Animal in rig at 1205

# using closed-field rig configuration, sound intensity set to 50 dB

exp2.add_site(2300) # tip 3 ref
exp2.add_session('12-17-59', 'a', 'AMtone', 'am_tuning_curve')  # 1600 trials

exp2.add_site(1580) # tip 3 ref
exp2.add_session('13-07-02', 'b', 'tuningFreq', 'am_tuning_curve') # 320 trials
exp2.add_session('13-17-51', 'c', 'AMtone', 'am_tuning_curve') # 640 trials (only 4 & 64 Hz)

experiments.append(exp2)


# mouse out 1340


