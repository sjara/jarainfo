from jaratoolbox import celldatabase

subject = 'poni002'
experiments=[]




### 2025-06-07 Session ###
exp0 = celldatabase.Experiment(subject, '2025-07-17', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-3082',
                               info = ['faceLeft','soundBilateral'])
exp0.maxDepth=3000

# Animal in rig at 1105

# # Shank 1 bank A  (tip#1), screen at 25 Hz
exp0.add_site(3000)
# anesthetized at 1%
# # exp0.add_session('17-20-44', 'a', 'poniSpont4x4', 'am_image_tuning') 
# exp0.add_session('17-47-55', 'b', 'poniSpont4x4', 'am_image_tuning') 
# exp0.add_session('18-14-45', 'c', 'poniSpont6x6_1-1', 'am_image_tuning')
# exp0.add_session('18-20-29', 'd', 'poniSpont6x6_1-4', 'am_image_tuning')
# exp0.add_session('18-38-46', 'e', 'poniSpont6x6_4-1', 'am_image_tuning')
# exp0.add_session('18-49-44', 'f', 'poniSpont6x6_4-4', 'am_image_tuning')
# exp0.add_session('19-05-35', 'g', 'poniSpont18x18_4-4', 'am_image_tuning')
# exp0.add_session('19-16-21', 'h', 'poniSpont18x18_4-13', 'am_image_tuning') # switched to 50% image trials instead of 25% (so only 90 trials instead of 180)
# # exp0.add_session('19-21-00', 'i', 'poniSpont18x18_13-4', 'am_image_tuning') # forgot to hit plus button in openEphys .-.
# # exp0.add_session('19-28-27', 'j', 'poniSpont18x18_13-13', 'am_image_tuning') # forgot to enable hdmi .-.
# exp0.add_session('19-34-27', 'k', 'poniSpont18x18_13-13', 'am_image_tuning')
# exp0.add_session('19-40-34', 'l', 'poniSpont18x18_13-4', 'am_image_tuning')

# exp0.add_session('17-20-44', 'a', 'poniAM4x4', 'am_image_tuning') 
exp0.add_session('17-47-55', 'b', 'poniAM4x4', 'am_image_tuning') 
exp0.add_session('18-14-45', 'c', 'poniAM6x6_1-1', 'am_image_tuning')
exp0.add_session('18-20-29', 'd', 'poniAM6x6_1-4', 'am_image_tuning')
exp0.add_session('18-38-46', 'e', 'poniAM6x6_4-1', 'am_image_tuning')
exp0.add_session('18-49-44', 'f', 'poniAM6x6_4-4', 'am_image_tuning')
exp0.add_session('19-05-35', 'g', 'poniAM18x18_4-4', 'am_image_tuning')
exp0.add_session('19-16-21', 'h', 'poniAM18x18_4-13', 'am_image_tuning') # switched to 50% image trials instead of 25% (so only 90 trials instead of 180)
# exp0.add_session('19-21-00', 'i', 'poniAM18x18_13-4', 'am_image_tuning') # forgot to hit plus button in openEphys .-.
# exp0.add_session('19-28-27', 'j', 'poniAM18x18_13-13', 'am_image_tuning') # forgot to enable hdmi .-.
exp0.add_session('19-34-27', 'k', 'poniAM18x18_13-13', 'am_image_tuning')
exp0.add_session('19-40-34', 'l', 'poniAM18x18_13-4', 'am_image_tuning')

# animal out of rig at 1953

experiments.append(exp0)

