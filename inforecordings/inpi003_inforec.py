
from jaratoolbox import celldatabase

subject = 'inpi003'
experiments=[]

probe_tip = 4004 # max depth is same for all experiments since the probe is implanted!


### 2025-03-10 Session ###
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
### NOTE: Weird noise in multiple groups of channels
exp0.add_site(4003)
exp0.add_session('15-55-03', 'c', 'Freq', 'am_tuning_curve')
exp0.add_session('16-40-22','g','AM','am_tuning_curve')

# Shank 4 bank A (tip#4)
### NOTE: Weird noise in multiple groups of channels
exp0.add_site(4004) 
exp0.add_session('16-06-35', 'd', 'Freq', 'am_tuning_curve')
exp0.add_session('16-51-00','h','AM','am_tuning_curve')

# animal out of rig at 17:15

experiments.append(exp0)

### 2025-03-17 Session ###
# all shanks, 193-288, tip#2 reference
exp1 = celldatabase.Experiment(subject, '2025-03-17', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundLeft'])

exp1.maxDepth=probe_tip

# mouse in rig1 16:15

# used 3rd bank of 96 electrodes (193-288), so deepest trode was 4000-2*720=2560um
### NOTE: weird noise in multiple groups of channels in shanks 3&4
exp1.add_site(2560)
exp1.add_session('16-18-44','a','Freq','am_tuning_curve')
exp1.add_session('16-28-03','b','AM','am_tuning_curve')
exp1.add_session('16-35-57','a','naturalSound','natural_sound_detection')

# mouse out at 17:15
experiments.append(exp1)



### 2025-04-02 Session ###
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


### 2025-04-09 Session ###
# mouse in at 11:15, noticed change in black spot, seems to be dried blood

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


### 2025-04-28 session ###
# mouse in at 14:45
exp4 = celldatabase.Experiment(subject, '2025-04-28', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundLeft'])


exp4.maxDepth = probe_tip

# using shank 1 bank B, same depth as 385-480 (but add 1 um to indicate shank)
exp4.add_site(1121)

# using external reference
exp4.add_session('15-25-36','a','Freq','am_tuning_curve') # 322  trials
exp4.add_session('15-33-55','b','AM','am_tuning_curve') # 222 trials

# using tip of shank 1 as reference
exp4.add_session('15-42-06','c','Freq','am_tuning_curve') # 331 trials
exp4.add_session('15-50-41','d','AM','am_tuning_curve') # 224 trials
exp4.add_session('15-58-13','a','naturalSound','natural_sound_detection') # 201 trials

# mouse out at 16:27

experiments.append(exp4)


# Joe's experiment 2025-05-09
# experiments.append(exp5)

# 12-12-21, 'a', ild vs abv, sound_localization.py



### Joe's experiment 2025-05-20 ###
# mouse in at 11:59
exp5 = celldatabase.Experiment(subject, '2025-05-20', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundBilateral'])
                               
                               
exp5.maxDepth = probe_tip     
exp5.add_site(1120)
                         
#using tip 1 as reference, recording all shanks 385-480                             
exp5.add_session('11-39-29','a','L2R3_L2R1_L1R2_L3R2','sound_localization') # 401 trials

# mouse out at 12:17

experiments.append(exp5)

### Joe's experiment 2025-06-02 ###
# mouse in at 11:00
exp6 = celldatabase.Experiment(subject, '2025-06-02', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundBilateral'])
                               
                               
exp6.maxDepth = probe_tip     
exp6.add_site(1120)
                         
#using tip 1 as reference, recording all shanks 385-480                             
exp6.add_session('11-09-19','a','L2R3_L2R1_L1R2_L3R2','sound_localization') # 432 trials
exp6.add_session('11-41-31','a','tuningFreq','am_tuning_curve') # 337 trials

# mouse out at 1152


experiments.append(exp6)




### 20250606

# mouse in at 1505
exp7 = celldatabase.Experiment(subject, '2025-06-06', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundBilateral'])

exp7.maxDepth=probe_tip
# using all shanks #385-480, 4000-2880 = 1120um
exp7.add_site(1120)

# tip#1 reference
exp7.add_session('15-06-39','a','Freq','am_tuning_curve') # 334 trials, soundLeft
exp7.add_session('15-15-30','b','Freq','am_tuning_curve') # 340 trials, soundBilateral
#exp7.add_session('15-24-38','','AM','am_tuning_curve') # soundLeft, FORGOT TO SAVE BEHAVSESSION
exp7.add_session('15-32-30','c','AM','am_tuning_curve') # 241 trials, soundLeft
exp7.add_session('15-41-24','d','AM','am_tuning_curve') # 239 trials, soundBilateral
exp7.add_session('15-49-33','a','naturalSound','natural_sound_detection') # 201 trials, soundLeft
exp7.add_session('16-16-12','b','naturalSound','natural_sound_detection') # 201 trials, soundBilateral
exp7.add_session('16-43-29''','Spont','')


experiments.append(exp7)

# mouse out at 1755
