from jaratoolbox import celldatabase

subject = 'poni009'
experiments=[]

probe_tip = 2604 # max depth is same for all experiments since the probe is implanted!

# probe #23299112911

### 2025-10-17 Session ###
exp0 = celldatabase.Experiment(subject, '2025-10-17', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-2911',
                               info = ['faceRight','soundLeft'])
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



