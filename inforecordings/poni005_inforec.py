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
exp1.add_session('13-36-11','a','BADoptoAMtone','am_tuning_curve') # laser set to 10 mW (7.76)
exp1.add_session('14-30-18','b','optoAMtone','am_tuning_curve') # laser set to 10 mW (7.76)

experiments.append(exp1)

# mouse out 1545


### 2025-08-20 session

# mouse in 1315

exp2 = celldatabase.Experiment(subject, '2025-08-19', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-5674',
                               info = ['faceLeft','soundRight'])


exp2.maxDepth=probe_tip

exp2.add_site(2250)
# recorded using left ear bud positioned next to right ear
exp2.add_session('13-27-54','a','optoAMtone','am_tuning_curve') # laser set to 10 mW (7.76)

experiments.append(exp2)

# mouse out 1500
