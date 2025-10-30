from jaratoolbox import celldatabase

subject = 'poni005'
experiments=[]

probe_tip = 2974 # max depth is same for all experiments since the probe is implanted!


### 2025-08-18 Session ###
exp0 = celldatabase.Experiment(subject, '2025-08-18', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight'])
exp0.maxDepth=probe_tip

# Animal in rig at 1030

# # Shank 1 bank A  (ext)
# exp0.add_site(2971)
# exp0.add_session('10-39-50', 'a', 'tuningFreq', 'am_tuning_curve') 

# # Shank 3 bank A  (ext)
# exp0.add_site(2973)
# exp0.add_session('10-50-33', 'b', 'tuningFreq', 'am_tuning_curve') 

# # all shanks 385-480  (ext), for measuring pia
# exp0.add_site(2974-2880)
# exp0.add_session('11-00-37', 'pia', 'tuningFreq', 'am_tuning_curve')  

# shanks 1,2 (2160-1440), 3 (2160-720), tip 2 reference
exp0.add_site(2250)
exp0.add_session('11-13-40','c','tuningFreq','am_tuning_curve')
exp0.add_session('11-21-47','d','tuningAM','am_tuning_curve')
exp0.add_session('11-30-48','a','naturalSound','natural_sound_detection')

experiments.append(exp0)
# mouse out 1200


# --- 2025-08-19 Session ---

# mouse in 1300

exp1 = celldatabase.Experiment(subject, '2025-08-19', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundBilateral'])
exp1.maxDepth=probe_tip

exp1.add_site(2250)
# exp1.add_session('13-36-11','a','BADoptoAMtone','am_tuning_curve') # laser set to 10 mW (7.76)
exp1.add_session('14-30-18','b','optoAMtone','am_tuning_curve') # laser set to 10 mW (7.76)

experiments.append(exp1)

# mouse out 1545


### 2025-08-20 session

# mouse in 1315

exp2 = celldatabase.Experiment(subject, '2025-08-20', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight'])



exp2.maxDepth=probe_tip

exp2.add_site(2250)
# recorded using left ear bud positioned next to right ear (bdata says soundLeft but it is actually on the right!!!)
exp2.add_session('13-27-54','a','optoAMtone','am_tuning_curve') # laser set to 10 mW (7.76)

experiments.append(exp2)

# mouse out 1500

### 2025-08-21 session

# mouse in 1623

exp3 = celldatabase.Experiment(subject,'2025-08-21','left_AC',
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight'])

# recorded using left ear bud positioned next to right ear (bdata says soundLeft but it is actually on the right!!!)
exp3.maxDepth=probe_tip
exp3.add_site(2250)
exp3.add_session('16-25-49','a','optoTuningFreq','am_tuning_curve') # laser at 10 mW (7.76)
exp3.add_session('16-53-23','b','optoTuningAMtone','am_tuning_curve') # laser at 10 mW (7.76)

experiments.append(exp3)
# mouse out 1820

### 2025-08-28 session

# mouse in 1425

exp4 = celldatabase.Experiment(subject,'2025-08-28','left_AC',
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight'])

# recorded using left ear bud positioned next to right ear (bdata says soundLeft but it is actually on the right!!!)
exp4.maxDepth=probe_tip
exp4.add_site(2250) # tip #2
exp4.add_session('14-38-13','a','poniAMtone_2x1','am_image_tuning') # minidisplay set to 100hz, maximum power

experiments.append(exp4)
# mouse out 1640



### 2025-10-24 session ###

# mouse in 1310

exp5 = celldatabase.Experiment(subject,'2025-10-24','left_AC',
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight','closedField'])

exp5.maxDepth=probe_tip


# had lots of oscillatory (60Hz ish) noise when using tip2 reference, but seems much better using tip3
exp5.add_site(2970) # tip #3 ref, 1530-2250 on shanks 1&3, 1530-2970 on shank 2
exp5.add_session('13-24-39','a','tuningFreq','am_tuning_curve') # 40 dB
exp5.add_session('13-32-57','b','tuningAM','am_tuning_curve') # 40 dB
exp5.add_session('13-40-57','a','naturalSound','natural_sound_detection') # 40 dB

exp5.add_session('14-07-45','c','tuningAMtone','am_tuning_curve') # 40 dB


# exp5.add_site(2253)
# exp5.add_session('15-00-37','tmp1','tuningFreq','am_tuning_curve')

# exp5.add_site(-633)
# exp5.add_session('15-02-37','tmp2','tuningFreq','am_tuning_curve')

# mouse out 1510

experiments.append(exp5)


### 2025-10-28 session ###

# mouse in 1600

exp6 = celldatabase.Experiment(subject,'2025-10-28','left_AC',
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight','closedField'])

exp6.maxDepth=probe_tip


# had lots of oscillatory (60Hz ish) noise when using tip2 reference, but seems much better using tip3
exp6.add_site(2250) # tip #3 ref, 810-1530 on shanks 1&2, 810-2250 on shank 3
exp6.add_session('16-12-46','a','tuningFreq','am_tuning_curve') # 40 dB
exp6.add_session('16-20-35','b','tuningAM','am_tuning_curve') # 40 dB
exp6.add_session('16-28-02','a','naturalSound','natural_sound_detection') # 40 dB

exp6.add_session('16-54-41','c','tuningAMtone','am_tuning_curve') # 40 dB


# mouse out 1745

experiments.append(exp6)

### 2025-10-28 session ###

# mouse in 1600

exp6 = celldatabase.Experiment(subject,'2025-10-28','left_AC',
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight','closedField'])

exp6.maxDepth=probe_tip


# had lots of oscillatory (60Hz ish) noise when using tip2 reference, but seems much better using tip3
exp6.add_site(2250) # tip #3 ref, 810-1530 on shanks 1&2, 810-2250 on shank 3
exp6.add_session('16-12-46','a','tuningFreq','am_tuning_curve') # 40 dB
exp6.add_session('16-20-35','b','tuningAM','am_tuning_curve') # 40 dB
exp6.add_session('16-28-02','a','naturalSound','natural_sound_detection') # 40 dB

exp6.add_session('16-54-41','c','tuningAMtone','am_tuning_curve') # 40 dB


# mouse out 1745

experiments.append(exp6)


### 2025-10-29 session ###

# mouse in 1045

exp7 = celldatabase.Experiment(subject,'2025-10-29','left_AC',
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight','closedField'])

exp7.maxDepth=probe_tip


# had lots of oscillatory (60Hz ish) noise when using tip2 reference, but seems much better using tip3
exp7.add_site(2250) # tip #3 ref, 810-1530 on shanks 1&2, 810-2250 on shank 3
exp7.add_session('11-03-03','a','optoTuningAMtone','am_tuning_curve') # 40 dB, 5 mW (3.58)
exp7.add_session('12-12-28','b','optoTuningFreq','am_tuning_curve') # 40 dB, 5 mW (3.58)


# mouse out 1240

experiments.append(exp7)


