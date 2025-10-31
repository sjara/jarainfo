from jaratoolbox import celldatabase

subject = 'poni009'
experiments=[]

probe_tip = 2604 # max depth is same for all experiments since the probe is implanted!

# probe #23299112911

### 2025-10-17 Session ###
exp0 = celldatabase.Experiment(subject, '2025-10-17', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp0.maxDepth=probe_tip

# Animal in rig at 1230
# exp0.add_site(2603) # tip 3 ref
# exp0.add_session('12-43-44', 'test', 'tuningFreq', 'am_tuning_curve') # 50 dB
# exp0.add_session('12-51-10', 'test2', 'tuningFreq', 'am_tuning_curve') # 70 dB
# # no clear responses on shank 3


# exp0.add_site(2602) # tip 2 ref
# exp0.add_session('12-57-01', 'test3', 'tuningFreq', 'am_tuning_curve') # 50 dB
# # some clear responses on shank 2

exp0.add_site(1160) # tip 2 ref
# exp0.add_session('13-02-37', 'test4', 'tuningFreq', 'am_tuning_curve') # 50 dB
# # now appears to be responses on all shanks? will continue with this site and see 
# # how it look in the spike sorted data


exp0.add_session('13-06-55', 'a', 'tuningFreq', 'am_tuning_curve') # 50 dB
exp0.add_session('13-17-20', 'b', 'tuningAM', 'am_tuning_curve') # 50 dB
exp0.add_session('13-25-08', 'a', 'naturalSound', 'natural_sound_detection') # 50 dB

exp0.add_site(1880) # tip 2 ref
exp0.add_session('13-52-40', 'c', 'tuningFreq', 'am_tuning_curve') # 50 dB

# NOTE: tube shifted position at some point between 1306 and 1400, unsure of when

experiments.append(exp0)


# mouse out 1404


### 2025-10-20 session ###

# mouse in 1110

exp1 = celldatabase.Experiment(subject, '2025-10-20', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp1.maxDepth=probe_tip

exp1.add_site(2603) # shanks 3/4, tip 3 ref
exp1.add_session('11-27-20','a','tuningFreq','am_tuning_curve') # 50 dB
exp1.add_session('11-41-30','b','tuningFreq','am_tuning_curve') # 70 dB

# experiments.append(exp1)

# mouse out 1150


# mouse in 1610


exp1.add_site(1520) # all shanks, tip 2 ref
exp1.add_session('16-11-05','c','tuningFreq','am_tuning_curve') # 50 dB
exp1.add_session('16-18-58','d','tuningAM','am_tuning_curve') # 50 dB
exp1.add_session('16-26-03','a','naturalSound','natural_sound_detection') # 50 dB

experiments.append(exp1)

# mouse out 1655



### 2025-10-31 session ###

# mouse in 1425

exp2 = celldatabase.Experiment(subject, '2025-10-31', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp2.maxDepth=probe_tip


exp2.add_site(1520) # all shanks (146-240), tip 2 ref
exp2.add_session('14-44-48','a','tuningFreq','am_tuning_curve') # 40 dB
exp2.add_session('14-52-51','b','tuningAM','am_tuning_curve') # 40 dB
exp2.add_session('15-00-33','a','naturalSound','natural_sound_detection') # 40 dB

exp2.add_session('15-27-11','c','tuningAMtone','am_tuning_curve') # 40 dB


# mouse out 1620
experiments.append(exp2)





