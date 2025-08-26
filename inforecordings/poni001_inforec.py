from jaratoolbox import celldatabase

subject = 'poni001'
experiments=[]

probe_tip = 2364 # max depth is same for all experiments since the probe is implanted!


### 2025-06-07 Session ###
exp0 = celldatabase.Experiment(subject, '2025-06-07', 'right_AC', 
                               'centerCenter_DiD',probe='NPv2-3082',
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


### 2025-06-09 Session ###

# mouse in at 1030

exp1 = celldatabase.Experiment(subject, '2025-06-09', 'right_AC', 
                               'centerCenter_DiD',probe='NPv2-3082',
                               info = ['faceRight','soundLeft'])
exp1.maxDepth=probe_tip


# bank 1-192 of shanks 3 & 4, tip#3 reference
exp1.add_site(2360)

exp1.add_session('10-54-38','a','Freq','am_tuning_curve')
exp1.add_session('11-02-53','b','AM','am_tuning_curve')
exp1.add_session('11-10-08','a','naturalSound','natural_sound_detection')

experiments.append(exp1)

# mouse out at 1200

### 2025-06-10 Experiment

# mouse in at 1530

exp2 = celldatabase.Experiment(subject, '2025-06-10','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundBilateral'])

exp2.add_site(2360)
exp2.maxDepth=probe_tip

# using headphones
# exp2.add_session('15-47-35','a','L2R3_L2R1_L1R2_L3R2','sound_localization') # with 3/17 sine&noise calibrations
exp2.add_session('16-07-57','b','L2R3_L2R1_L1R2_L3R2','sound_localization') # with 5/6 sine&noise calibrations

# back to 3/17 sine&noise calibrations, using regular speakers

exp2.add_session('17-20-19','a','optoFreq','am_tuning_curve')
exp2.add_session('17-39-32','b','optoAM','am_tuning_curve')

# mouse out at 1800

experiments.append(exp2)



### 2025-06-13 session

# mouse in at 1345

exp3 = celldatabase.Experiment(subject, '2025-06-13','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundBilateral'])

exp3.maxDepth=probe_tip
exp3.add_site(2360)

exp3.add_session('13-56-15','a','optoNaturalSound','natural_sound_detection')
exp3.add_session('14-59-34','a','optoSoundLoc','sound_localization')


experiments.append(exp3)

# mosue out at 1540


### 2025-06-25 session

# mouse in 1615

exp4 = celldatabase.Experiment(subject,'2025-06-25','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundBilateral'])

exp4.maxDepth=probe_tip
exp4.add_site(2360)
# shanks 3&4 1-192, tip 3 reference, 50 Hz minidisplay refresh rate
exp4.add_session('16-27-00','a','poniSpont_4x4','am_image_tuning')
exp4.add_session('16-43-57','b','poniFreq_4x1','am_image_tuning')

experiments.append(exp4)

# mouse out 1800


### 2025-06-30 session

# mouse in 1230

exp5 = celldatabase.Experiment(subject,'2025-06-30','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundBilateral'])

exp5.maxDepth=probe_tip
exp5.add_site(2360)
# shanks 3&4 1-192, tip 3 reference, 100 Hz minidisplay refresh rate
exp5.add_session('12-58-51','a','poniFreq_4x1','am_image_tuning') # 1600 trials, 4x1
exp5.add_session('13-59-56','b','poniFreq_1x4','am_image_tuning') # 1600 trials, 1x4
exp5.add_session('14-59-47','c','poniSpont_4x4','am_image_tuning') # 320 trials, 4x4

experiments.append(exp5)

# mouse out 1530

### 2025-07-18 session

# mouse in 1520

exp6 = celldatabase.Experiment(subject,'2025-07-18','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundBilateral'])
exp6.maxDepth=probe_tip
exp6.add_site(2360)
# shanks 3&4 1-192, tip 3 reference, 100 Hz minidisplay refresh rate
exp6.add_session('15-42-52','a','poniSpont_4x4','am_image_tuning') # 
exp6.add_session('16-17-46','b','poniFreq_4x1','am_image_tuning') # 
exp6.add_session('17-36-06','c','poniFreq_4x4_C2R3_2x2','am_image_tuning') # 

experiments.append(exp6)

# moue out 1840

### 2025-08-05 session

# mouse in 1400

exp7 = celldatabase.Experiment(subject,'2025-08-05','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundLeft'])
exp7.maxDepth=probe_tip
exp7.add_site(2360)
# shanks 3&4 1-192, tip 3 reference
exp7.add_session('14-04-09','a','AMtone','am_tuning_curve')


experiments.append(exp7)

# mouse out 1459



### 2025-08-12 Recording Session ###


exp8 = celldatabase.Experiment(subject,'2025-08-12','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundBilateral'])
# mouse in 1212
exp8.maxDepth=probe_tip
exp8.add_site(2360)
#exp8.add_session('12-15-01','a','tuningFreq_soundLeft','am_tuning_curve') # soundLeft
#exp8.add_session('12-23-13','b','tuningFreq_soundRight','am_tuning_curve') # soundRight
#exp8.add_session('12-35-59','c','tuningFreq_soundBilateral','am_tuning_curve') # soundBilateral
# used wrong speakers ^ :(

exp8.add_session('12-40-45','d','tuningFreq_soundLeft','am_tuning_curve') # soundLeft
exp8.add_session('12-50-04','e','tuningFreq_soundRight','am_tuning_curve') # soundRight
exp8.add_session('12-59-15','f','tuningFreq_soundBilateral','am_tuning_curve') # soundBilateral

exp8.add_session('13-07-57','g','AMtone','am_tuning_curve') # soundLeft

experiments.append(exp8)

# mouse out 1400


### -- 2025-08-19 session ---

# mouse in 1609

exp9 = celldatabase.Experiment(subject,'2025-08-19','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundBilateral'])

exp9.maxDepth=probe_tip
exp9.add_site(2360)
exp9.add_session('16-14-53','a','optoAMtone','am_tuning_curve') # laser at 10 mW (7.76) 

experiments.append(exp9)

# mouse out 1730

### 2025-08-20 session

# mouse in 1020

exp10 = celldatabase.Experiment(subject,'2025-08-20','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundLeft'])

exp10.maxDepth=probe_tip
exp10.add_site(2360)
exp10.add_session('10-34-29','a','optoAMtone','am_tuning_curve') # laser at 10 mW (7.76)

experiments.append(exp10)
# mouse out 1200


### 2025-08-21 session

# mouse in 1320

exp11 = celldatabase.Experiment(subject,'2025-08-21','right_AC',
                               'centerCenter_DiD',probe='NPv2-3082',
                               info=['faceRight','soundLeft'])

exp11.maxDepth=probe_tip
exp11.add_site(2360)
exp11.add_session('14-16-21','a','optoFreq','am_tuning_curve') # laser at 10 mW (7.76)
exp11.add_session('14-50-14','b','optoAMtone','am_tuning_curve') # laser at 10 mW (7.76)

experiments.append(exp11)
# mouse out 1620
