
from jaratoolbox import celldatabase

subject = 'poni001'
experiments=[]

probe_tip = 2364 # max depth is same for all experiments since the probe is implanted!


### 2025-06-07 Session ###
exp0 = celldatabase.Experiment(subject, '2025-06-07', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3082',
                               info = ['faceRight','soundLeft'])
exp0.maxDepth=probe_tip

# Animal in rig at 1300

# # Shank 1 bank A  (tip#1)
# exp0.add_site(2361)
# exp0.add_session('14-07-32', 'a', 'Freq', 'am_tuning_curve') 
# exp0.add_session('14-45-38', 'e','AM','am_tuning_curve')

# # Shank 2 bank A (tip#2)
# exp0.add_site(2362)
# exp0.add_session('14-16-23', 'b', 'Freq', 'am_tuning_curve')
# exp0.add_session('14-55-28','f','AM','am_tuning_curve')

# Shank 3 bank A (tip#3)
exp0.add_site(2363)
exp0.add_session('14-25-37', 'c', 'Freq', 'am_tuning_curve')
exp0.add_session('15-03-36','g','AM','am_tuning_curve')

# Shank 4 bank A (tip#4)
exp0.add_site(2364) 
exp0.add_session('14-36-14', 'd', 'Freq', 'am_tuning_curve')
exp0.add_session('15-11-28','h','AM','am_tuning_curve')

# # bank 385-480 (tip #2)
# exp0.add_site(2360)
# exp0.add_session('15-22-13','i','Freq','am_tuning_curve')
# exp0.add_session('15-30-29','j','AM','am_tuning_curve')

# animal out of rig at 1547

experiments.append(exp0)
