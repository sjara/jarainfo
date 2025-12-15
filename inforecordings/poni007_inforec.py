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



exp3 = celldatabase.Experiment(subject, '2025-10-24', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp3.maxDepth=probe_tip

# Animal in rig at 1525

exp3.add_site(1580) # tip 3 ref, sounds at 40 dB
exp3.add_session('15-35-24', 'a', 'tuningFreq', 'am_tuning_curve') 
exp3.add_session('15-43-50', 'b', 'tuningAM', 'am_tuning_curve') # accidentally hit start again before saving, one extra trial at end of bdata
exp3.add_session('15-51-08', 'a', 'naturalSound', 'natural_sound_detection') 


exp3.add_session('16-17-37', 'c', 'tuningAMtone', 'am_tuning_curve') 

# mouse out 1710
experiments.append(exp3)


### 2025-10-29 session

exp4 = celldatabase.Experiment(subject, '2025-10-29', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp4.maxDepth=probe_tip

# Animal in rig at 1540

exp4.add_site(2300) # tip 3 ref, sounds at 40 dB
exp4.add_session('15-57-30', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 10 mW (7.74)
exp4.add_session('17-06-21', 'b', 'optoTuningFreq', 'am_tuning_curve') # 10 mW (7.74)


# mouse out 1745
experiments.append(exp4)


### 2025-11-06 session

exp5 = celldatabase.Experiment(subject, '2025-11-06', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp5.maxDepth=probe_tip

# Animal in rig at 1215

exp5.add_site(1580) # tip 3 ref, sounds at 40 dB
exp5.add_session('12-25-13', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 10 mW (7.74)
exp5.add_session('13-34-27', 'b', 'optoTuningFreq', 'am_tuning_curve') # 10 mW (7.74)


# mouse out 1410
experiments.append(exp5)


### 2025-11-07 session

exp6 = celldatabase.Experiment(subject, '2025-11-07', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp6.maxDepth=probe_tip

# Animal in rig at 1400

exp6.add_site(1580) # tip 3 ref, sounds at 40 dB
exp6.add_session('14-09-54', 'a', 'optoTuningFreq', 'am_tuning_curve') # 10 mW (7.74)
exp6.add_session('14-42-09', 'b', 'optoTuningAMtone', 'am_tuning_curve') # 10 mW (7.74)


# mouse out 1555
experiments.append(exp6)



### 2025-11-11 session

exp7 = celldatabase.Experiment(subject, '2025-11-11', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp7.maxDepth=probe_tip

# Animal in rig at 1520

# failed to get sync light in frame of the video :(

exp7.add_site(1580) # tip 3 ref, sounds at 40 dB
exp7.add_session('15-29-52', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 10 mW (7.74)
exp7.add_session('16-40-33', 'b', 'optoTuningFreq', 'am_tuning_curve') # 10 mW (7.74)


# mouse out 1720
experiments.append(exp7)


### 2025-11-13 session

exp8 = celldatabase.Experiment(subject, '2025-11-13', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp8.maxDepth=probe_tip

# Animal in rig at 1340


exp8.add_site(1580) # tip 3 ref, sounds at 40 dB
exp8.add_session('13-56-06', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 10 mW (7.74)
exp8.add_session('15-14-57', 'b', 'optoTuningFreq', 'am_tuning_curve') # 10 mW (7.74)


# mouse out 1552
experiments.append(exp8)


### 2025-11-18 session

exp9 = celldatabase.Experiment(subject, '2025-11-18', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp9.maxDepth=probe_tip

# Animal in rig at 1120


exp9.add_site(2300) # tip 3 ref, sounds at 40 dB
exp9.add_session('11-27-06', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 10 mW (7.74)
exp9.add_session('12-36-12', 'b', 'optoTuningFreq', 'am_tuning_curve') # 10 mW (7.74)


# mouse out 1350

#### screw for securing GRIN lens cover broke off, had to re-affix a new one. hopefully it holds 
experiments.append(exp9)


### 2025-11-21 session

exp10 = celldatabase.Experiment(subject, '2025-11-21', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp10.maxDepth=probe_tip

# Animal in rig at 1350


exp10.add_site(2300) # tip 3 ref, sounds at 40 dB
exp10.add_session('14-06-50', 'a', 'optoTuningAMtone', 'am_tuning_curve') # 10 mW (7.74)
exp10.add_session('15-17-42', 'b', 'optoTuningFreq', 'am_tuning_curve') # 10 mW (7.74)


# mouse out 1600

experiments.append(exp10)



### 2025-12-04 session

exp11 = celldatabase.Experiment(subject, '2025-12-04', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp11.maxDepth=probe_tip

# Animal in rig at 0940


exp11.add_site(1580) # tip 2 ref, sounds at 40 dB
exp11.add_session('09-42-55','a','naturalSoundLoc','natural_sound_detection')
exp11.add_session('11-08-49', 'a', 'optoShamAMtone', 'am_tuning_curve') # 10 mW (7.74)


# mouse out 1220

experiments.append(exp11)



### 2025-12-05 session

exp12 = celldatabase.Experiment(subject, '2025-12-05', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp12.maxDepth=probe_tip

# Animal in rig at 1520


exp12.add_site(2300) # tip 2 ref, sounds at 40 dB
exp12.add_session('15-34-27', 'a', 'optoShamAMtone', 'am_tuning_curve') # 10 mW (7.74)
exp12.add_session('16-46-09','a','naturalSoundLoc','natural_sound_detection')


# mouse out 1820

experiments.append(exp12)


### 2025-12-15 session

exp13 = celldatabase.Experiment(subject, '2025-12-15', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5422',
                               info = ['faceLeft','soundRight', 'closedField'])
exp13.maxDepth=probe_tip

# Animal in rig at 1210


exp13.add_site(1520) # tip 2 ref, sounds at 40 dB
exp13.add_session('12-18-15', 'a', 'tuningAMtone', 'am_tuning_curve') # 40 dB

# ground wire was broken when I opened the cage, should still be fine for spiking activity
# mouse out 1315

experiments.append(exp13)