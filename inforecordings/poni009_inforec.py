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


exp2.add_site(1520) # all shanks (145-240), tip 2 ref
exp2.add_session('14-44-48','a','tuningFreq','am_tuning_curve') # 40 dB
exp2.add_session('14-52-51','b','tuningAM','am_tuning_curve') # 40 dB
exp2.add_session('15-00-33','a','naturalSound','natural_sound_detection') # 40 dB

exp2.add_session('15-27-11','c','tuningAMtone','am_tuning_curve') # 40 dB


# mouse out 1620
experiments.append(exp2)



### 2025-11-04 session ###

# mouse in 1135

exp3 = celldatabase.Experiment(subject, '2025-11-04', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp3.maxDepth=probe_tip


exp3.add_site(1521) # 1520 shanks 1 and 2, 1160 shanks 3 and 4; tip 2 ref
exp3.add_session('11-48-54','a','tuningFreq','am_tuning_curve') # 40 dB
exp3.add_session('11-56-54','b','tuningAM','am_tuning_curve') # 40 dB
exp3.add_session('12-10-13','a','naturalSound','natural_sound_detection') # 40 dB

exp3.add_session('12-37-44','c','tuningAMtone','am_tuning_curve') # 40 dB



# exp3.add_site(2604) # shank 4, tip 2 ref
# exp3.add_session('13-04-42','test','testFreq','am_tuning_curve') # 70 dB


# mouse out 1310
experiments.append(exp3)



### 2025-11-05 session ###

# mouse in 1430

exp4 = celldatabase.Experiment(subject, '2025-11-05', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp4.maxDepth=probe_tip


exp4.add_site(1520) # all shanks (145-240), tip 2 ref
exp4.add_session('14-47-39','a','optoTuningAMtone','am_tuning_curve') # 40 dB, 10 mW (7.74)
exp4.add_session('15-58-27','b','optoTuningFreq','am_tuning_curve') # 40 dB, 10 mW (7.74)


# mouse out 1640
experiments.append(exp4)




### 2025-11-11 session ###

# mouse in 1230

exp5 = celldatabase.Experiment(subject, '2025-11-11', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp5.maxDepth=probe_tip


exp5.add_site(1520) # all shanks (145-240), tip 2 ref
exp5.add_session('13-20-29','a','optoTuningAMtone','am_tuning_curve') # 40 dB, 10 mW (7.74)
exp5.add_session('14-29-30','b','optoTuningFreq','am_tuning_curve') # 40 dB, 10 mW (7.74)


# mouse out 1515
experiments.append(exp5)


### 2025-11-12 session ###

# mouse in 1430

exp6 = celldatabase.Experiment(subject, '2025-11-12', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp6.maxDepth=probe_tip


exp6.add_site(1520) # all shanks (145-240), tip 2 ref
exp6.add_session('14-50-59','a','optoTuningAMtone','am_tuning_curve') # 40 dB, 10 mW (7.74)
exp6.add_session('16-00-33','b','optoTuningFreq','am_tuning_curve') # 40 dB, 10 mW (7.74)


# mouse out 1640
experiments.append(exp6)


### 2025-11-17 session ###

# mouse in 1310

exp7 = celldatabase.Experiment(subject, '2025-11-17', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp7.maxDepth=probe_tip


exp7.add_site(1520) # all shanks (145-240), tip 2 ref
exp7.add_session('13-14-58','a','optoTuningAMtone','am_tuning_curve') # 40 dB, 10 mW (7.74)
exp7.add_session('14-24-33','b','optoTuningFreq','am_tuning_curve') # 40 dB, 10 mW (7.74)


# mouse out 1500
experiments.append(exp7)



### 2025-12-04 session ###

# mouse in 1625

exp8 = celldatabase.Experiment(subject, '2025-12-04', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft','closedField'])
exp8.maxDepth=probe_tip


exp8.add_site(1520) # all shanks (145-240), tip 2 ref
exp8.add_session('16-32-39','a','optoShamAMtone','am_tuning_curve') # 40 dB, 10 mW (7.74)

# mouse out 1745
experiments.append(exp8)


### 2025-12-12 session ###

# mouse in 1520

exp9 = celldatabase.Experiment(subject, '2025-12-12', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundBinaural','closedField'])
exp9.maxDepth=probe_tip


exp9.add_site(1520) # all shanks (145-240), tip 2 ref
# exp9.add_session('15-25-26','a','naturalSoundLoc','natural_sound_detection') # 40 dB
exp9.add_session('15-57-02','b','naturalSoundLoc','natural_sound_detection') # 40 dB

# noticed the left ear tube had come out ~220 trials in, fixed it and started a new session
##. to capture the remaining trials

# mouse out 1715
experiments.append(exp9)
