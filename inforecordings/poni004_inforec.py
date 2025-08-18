from jaratoolbox import celldatabase

subject = 'poni004'
experiments=[]




### 2025-08-07 Session ###
# mouse in 1420
exp0 = celldatabase.Experiment(subject, '2025-08-07', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-3082',
                               info = ['faceLeft','soundBilateral'])

exp0.maxDepth=4004  # Xpia=13800, Xfinal=17800

# exp0.add_site(4001)
# exp0.add_session('18-02-41','d','optoAM','am_tuning_curve') # laser set to 9.76 (10mW) 


exp0.add_site(4002) # shank 2 bank A, tip2
exp0.add_session('17-24-38','a','tuningFreq','am_tuning_curve')
exp0.add_session('18-11-51','e','optoAM','am_tuning_curve')

# #4000-2880 = 1120
# exp0.add_site(1122) # shank 2 bank B, tip 2
# exp0.add_session('17-41-23','b','tuningFreq','am_tuning_curve')

exp0.add_site(4003) # shank 3 bank A, tip 3
exp0.add_session('17-53-33','c','tuningFreq','am_tuning_curve')
exp0.add_session('18-21-12','f','optoAM','am_tuning_curve')


# exp0.add_site(4004) # shank 4 bank A, tip 4
# exp0.add_session('18-30-20','g','optoAM','am_tuning_curve')





exp1 = celldatabase.Experiment(subject, '2025-08-07', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-3082',
                               info = ['faceFront','soundBilateral'])
exp1.maxDepth=4014 # Xpia=14000, Xfinal=18000

exp1.add_site(4014) # shank 4 bank A tip 4
exp1.add_session('19-36-04','h','tuningFreq','am_tuning_curve')
exp1.add_session('19-57-16','j','optoAM','am_tuning_curve')

exp1.add_site(4010) #1-96, tip2
exp1.add_session('19-48-18','i','optoAM','am_tuning_curve')

# exp1.add_site(3290) #97-192 tip2 (4010-720)
# exp1.add_session('20-08-00','k','optoAM','am_tuning_curve')

exp1.add_site(2570) #193-288 tip2 (4010-720*2)
exp1.add_session('20-17-40','l','optoAM','am_tuning_curve')

exp1.add_site(1850) #289-384 tip2 (4010-720*3)
exp1.add_session('20-27-43','m','optoAM','am_tuning_curve')

# mouse out 2040

experiments.append(exp0)
experiments.append(exp1)


### 2025-08-14 Session

# mouse in 1100

exp2 = celldatabase.Experiment(subject, '2025-08-14', 'left_AC', 
                               'centerCenter_DiD',probe='NPv2-3082',
                               info = ['faceLeft','soundBilateral'])


exp2.maxDepth=2504  # Xpia=13200, Xfinal=15722
# finished inserting probe at 13:00

exp2.add_site(2501) # shank 1 bank A, tip 2
exp2.add_session('13-06-46','a','tuningFreq','am_tuning_curve') 


exp2.add_site(2504) # shank 4 bank A, tip 2
exp2.add_session('13-17-45','b','tuningFreq','am_tuning_curve')



exp3 = celldatabase.Experiment(subject, '2025-08-14', 'left_AC', 
                               'centerCenter_DiD',probe='NPv2-3082',
                               info = ['faceLeft','soundBilateral'])


# advanced probe by additional 500 um to get all of shank4's bank A inside the brain
exp3.maxDepth=2824  # Xpia=13200, Xfinal=16180

exp3.add_site(2821) # shank 1 bank A, tip 2
exp3.add_session('13-34-45','d','tuningFreq','am_tuning_curve') 


exp3.add_site(2824) # shank 4 bank A, tip 2
exp3.add_session('13-29-01','c','tuningFreq','am_tuning_curve')


exp4 = celldatabase.Experiment(subject, '2025-08-14', 'left_AC', 
                               'centerCenter_DiD',probe='NPv2-3082',
                               info = ['faceLeft','soundBilateral'])

# advanced another 20 um to get a round number
exp4.maxDepth=3004  # Xpia=13200, Xfinal=16200

exp4.add_site(3001) # shank 1 bank A, tip 2
exp4.add_session('13-41-10','e','tuningFreq','am_tuning_curve') 
exp4.add_session('14-38-14','j','optoAM_10mW','am_tuning_curve')  # laser set to 9.76 (10 mW)

exp4.add_site(3002) # shank 2 bank A, tip2
exp4.add_session('14-24-59','i','optoAM_10mW','am_tuning_curve') # laser set to 9.76 (10 mW)


exp4.add_site(3003) # shank 3 bank A, tip 2
exp4.add_session('14-11-03','h','optoAM_10mW','am_tuning_curve') # laser set to 9.76 (10 mW)


exp4.add_site(3004) # shank 4 bank A, tip 2
exp4.add_session('13-47-57','f','tuningFreq','am_tuning_curve')
exp4.add_session('13-57-39','g','optoAM_10mW','am_tuning_curve') # laser set to 9.76 (10 mW)


exp4.add_site(1564) # 193-288, tip 2
exp4.add_session('14-51-35','k','tuningFreq','am_tuning_curve')
exp4.add_session('14-57-18','l','optoAM_10mW','am_tuning_curve') # laser set to 9.76 (10 mW)
exp4.add_session('15-14-04','m','optoAM_5mW','am_tuning_curve') # laser set to 4.31 (5 mW)


exp4.add_site(2284) 
exp4.add_session('15-28-18','n','tuningFreq','am_tuning_curve') 
exp4.add_session('15-34-54','o','optoAM_10mW','am_tuning_curve') # laser set to 9.76 (10 mW)
exp4.add_session('15-49-16','p','optoAM_5mW','am_tuning_curve') # laser set to 4.31 (5 mW)

exp4.add_site(121)
exp4.add_session('16-04-30','q','tuningFreq','am_tuning_curve') # for ID of pia on shank 1

exp4.add_site(124)
exp4.add_session('16-05-29','r','tuningFreq','am_tuning_curve') # for ID of pia on shank 4

# experiments.append(exp2)
# experiments.append(exp3)
experiments.append(exp4)
### mouse out 1632



### 2025-08-15 Session

# mouse in 1300


exp5 = celldatabase.Experiment(subject, '2025-08-15', 'left_AC', 
                               'centerCenter_DiI',probe='NPv2-3082',
                               info = ['faceFront','soundBilateral'])

exp5.maxDepth=3014    #Xpia=14800, Xf = 17800

exp5.add_site(3014) # shank 4 bank A, tip 4
exp5.add_session('14-25-40','a','tuningFreq','am_tuning_curve')
exp5.add_session('15-19-58','e','optoAM_2mW','am_tuning_curve') # laser set to 1.70 (2 mW)
exp5.add_session('17-13-55','n','optoAM_5mW','am_tuning_curve') # laser set to 4.31 (5 mW)
exp5.add_session('17-26-45','o','tuningFreq_end','am_tuning_curve')

exp5.add_site(3013) # shank 3 bank A, tip 4
exp5.add_session('16-51-38','l','tuningFreq','am_tuning_curve')
exp5.add_session('16-59-17','m','optoAM_2mW','am_tuning_curve') # laser set to 1.70 (2 mW)

exp5.add_site(2290) # 97-192, tip 4
exp5.add_session('14-42-30','b','tuningFreq','am_tuning_curve')
exp5.add_session('14-52-25','c','optoAM_2mW','am_tuning_curve') # laser set to 1.70 (2 mW)
exp5.add_session('15-37-47','f','optoAM_5mW','am_tuning_curve') # laser set to 4.31 (5 mW)
exp5.add_session('16-38-23','k','optoAM_10mW','am_tuning_curve') # laser set to 9.76 (10 mW)

exp5.add_site(1570) # 193-288, tip 4
exp5.add_session('16-30-04','j','tuningFreq','am_tuning_curve')
exp5.add_session('15-06-34','d','optoAM_2mW','am_tuning_curve') # laser set to 1.70 (2 mW)
exp5.add_session('15-51-25','g','optoAM_5mW','am_tuning_curve') # laser set to 4.31 (5 mW)
exp5.add_session('16-05-58','h','optoAM_1mW','am_tuning_curve') # laser set to 1.04 (1 mW)
exp5.add_session('16-14-23','i','optoAM_10mW','am_tuning_curve') # laser set to 9.76 (10 mW)

experiments.append(exp5)

# mouse out 1740