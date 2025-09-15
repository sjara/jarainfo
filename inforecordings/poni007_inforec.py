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
exp0.add_site(3023) # tip 3 ref
exp0.add_session('12-39-15', 'a', 'tuningFreq', 'am_tuning_curve')

exp0.add_site(2300) # tip 3 ref
exp0.add_session('12-49-35', 'b', 'tuningFreq', 'am_tuning_curve') # accidentally did sound left :(

experiments.append(exp0)


# mouse out 1258


