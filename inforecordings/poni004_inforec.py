from jaratoolbox import celldatabase

subject = 'poni004'
experiments=[]




### 2025-08-07 Session ###
# mouse in 1420
exp0 = celldatabase.Experiment(subject, '2025-08-07', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-3082',
                               info = ['faceLeft','soundBilateral'])

exp0.maxDepth=4004  # Xpia=13800, Xfinal=17800

exp0.add_site(4001)
exp0.add_session('18-02-41','d','optoValidation','am_tuning_curve') # laser set to 9.76 (10mW) 


exp0.add_site(4002) # shank 2 bank A, tip2
exp0.add_session('17-24-38','a','tuningFreq','am_tuning_curve')
exp0.add_session('18-11-51','e','optoValidation','am_tuning_curve')

#4000-2880 = 1120
exp0.add_site(1122) # shank 2 bank B, tip 2
exp0.add_session('17-41-23','b','tuningFreq','am_tuning_curve')

exp0.add_site(4003) # shank 3 bank A, tip 3
exp0.add_session('17-53-33','c','tuningFreq','am_tuning_curve')
exp0.add_session('18-21-12','f','optoValidation','am_tuning_curve')


exp0.add_site(4004) # shank 4 bank A, tip 4
exp0.add_session('18-30-20','g','optoValidation','am_tuning_curve')





exp1 = celldatabase.Experiment(subject, '2025-08-07', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-3082',
                               info = ['faceFront','soundBilateral'])
exp1.maxDepth=4004 # Xpia=14000, Xfinal=18000

exp1.add_site(4004) # shank 4 bank A tip 4
exp1.add_session('19-36-04','h','tuningFreq','am_tuning_curve')
exp1.add_session('19-57-16','j','optoValidation','am_tuning_curve')

exp1.add_site(4000) #1-96, tip2
exp1.add_session('19-48-18','i','optoValidation','am_tuning_curve')

exp1.add_site(4000- 720) #97-192 tip2
exp1.add_session('20-08-00','k','optoValidation','am_tuning_curve')

exp1.add_site(4000- 2*720) #193-288 tip2
exp1.add_session('20-17-40','l','optoValidation','am_tuning_curve')

exp1.add_site(4000- 3*720) #289-384 tip2
exp1.add_session('20-27-43','m','optoValidation','am_tuning_curve')

# mouse out 2040

experiments.append(exp0)
experiments.append(exp1)

