
from jaratoolbox import celldatabase

subject = 'inpi003'
experiments=[]

exp0 = celldatabase.Experiment(subject, '2025-03-10', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundLeft'])
# Animal in rig at 15:25

# Shank 1 bank A  (tip#1)
exp0.add_site(4001)
exp0.add_session('15-30-45', 'a', 'Freq', 'am_tuning_curve')
exp0.add_session('16-17-01', 'e','AM','am_tuning_curve')

# Shank 2 bank A (tip#2)
exp0.add_site(4002)
exp0.add_session('15-43-57', 'b', 'Freq', 'am_tuning_curve')
exp0.add_session('16-31-36','f','AM','am_tuning_curve')

# Shank 3 bank A (tip#3)
exp0.add_site(4003)
exp0.add_session('15-55-03', 'c', 'Freq', 'am_tuning_curve')
exp0.add_session('16-40-22','g','AM','am_tuning_curve')

# Shank 4 bank A (tip#4)
exp0.add_site(4004)
exp0.add_session('16-06-35', 'd', 'Freq', 'am_tuning_curve')
exp0.add_session('16-51-00','h','AM','am_tuning_curve')

# animal out of rig at 17:15

experiments.append(exp0)

# all shanks, 193-288, tip#2 reference


exp1 = celldatabase.Experiment(subject, '2025-03-17', 'right_AC', 
                               'centerCenter_DiI',probe='NPv2-3813',
                               info = ['faceRight','soundLeft'])

# mouse in rig1 16:15

exp1.add_site(4000)
exp1.add_session('16-18-44','a','Freq','am_tuning_curve')
exp1.add_session('16-28-03','b','AM','am_tuning_curve')
exp1.add_session('16-35-57','a','naturalSound','natural_souund_detection')

# mouse out at 17:15
experiments.append(exp1)


