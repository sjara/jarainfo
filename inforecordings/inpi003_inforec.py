
from jaratoolbox import celldatabase

subject = 'inpi003'
experiments=[]

probe_tip = 4004 # max depth is same for all experiments since the probe is implanted!

exp0 = celldatabase.Experiment(subject, '2025-03-10', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundLeft'])
exp0.maxDepth=probe_tip

# Animal in rig at 15:25

# Shank 1 bank A  (tip#1)
exp0.add_site(4001)
exp0.add_session('15-30-45', 'a', 'Freq', 'am_tuning_curve')
exp0.add_session('16-17-01', 'e','AM','am_tuning_curve')

# Shank 2 bank A (tip#2)
exp0.add_site(4002)
exp0.add_session('15-43-57', 'b', 'Freq', 'am_tuning_curve')
exp0.add_session('16-31-36','f','AM','am_tuning_curve')

# Shank 3 bank A (tip#3)
exp0.add_site(4003)
exp0.add_session('15-55-03', 'c', 'Freq', 'am_tuning_curve')
exp0.add_session('16-40-22','g','AM','am_tuning_curve')

# Shank 4 bank A (tip#4)
exp0.add_site(4004)
exp0.add_session('16-06-35', 'd', 'Freq', 'am_tuning_curve')
exp0.add_session('16-51-00','h','AM','am_tuning_curve')

# animal out of rig at 17:15

experiments.append(exp0)


# all shanks, 193-288, tip#2 reference
exp1 = celldatabase.Experiment(subject, '2025-03-17', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundLeft'])

exp1.maxDepth=probe_tip

# mouse in rig1 16:15

# used 3rd bank of 96 electrodes, so deepest trode was 4000-2*720=2560um
exp1.add_site(2560)
exp1.add_session('16-18-44','a','Freq','am_tuning_curve')
exp1.add_session('16-28-03','b','AM','am_tuning_curve')
exp1.add_session('16-35-57','a','naturalSound','natural_sound_detection')

# mouse out at 17:15
experiments.append(exp1)




# all shanks, 193-288, tip#1 reference
exp2 = celldatabase.Experiment(subject, '2025-04-02', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundLeft'])

exp2.maxDepth=probe_tip

# mouse in rig1 at 11:45

exp2.add_site(2560)
#exp2.add_session('12-17-11','','Spont','') # weird artifacts from poor tether connection
exp2.add_session('12-52-13','','Spont','')
exp2.add_session('13-23-12','a','Freq','am_tuning_curve')
exp2.add_session('13-31-22','b','AM','am_tuning_curve')
exp2.add_session('13-39-23','a','naturalSound','natural_sound_detection')

# mouse out at 14:20
experiments.append(exp2)



# mouse in at 11:15, noticed chane in black spot, seems to be dried blood

exp3 = celldatabase.Experiment(subject, '2025-04-09', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundLeft'])

exp3.maxDepth=probe_tip
# using all shanks #385-480, 4000-2880 = 1120um
exp3.add_site(1120)

# tip#1 reference

exp3.add_session('11-56-39','','Spont','')
exp3.add_session('12-27-15','a','Freq','am_tuning_curve') # 330 trials
exp3.add_session('12-35-59','b','AM','am_tuning_curve') # 224 trials
exp3.add_session('12-43-46','a','naturalSound','natural_sound_detection') # 201 trials


# mouse out at 13:15
experiments.append(exp3)





 
