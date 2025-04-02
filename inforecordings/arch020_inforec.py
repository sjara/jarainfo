from jaratoolbox import celldatabase
import importlib
importlib.reload(celldatabase)


subject = 'arch020'
experiments = []

#day 1- right hemisphere, recorded from 0.5mm medial from centre of craniotomy,shanks parallet to bregma lambda axis. Had opened left craniotomy, but the craniotomy was very posterior and was unable to see due to the wells. So, decided to record right first.
exp0 = celldatabase.Experiment(subject, '2025-03-24', brainArea='right_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundLeft'])
experiments.append(exp0)

exp0.add_site(3500)

# Reference = 1:tip
# Electrode preset = All Shanks 1-96 

exp0.add_session('13-24-04','a','optoTuningAM','am_tuning_curve')  
exp0.add_session('13-40-36','a','optoNaturalCategories','natural_sound_detection')
exp0.add_session('14-10-43','b','optoTuningFreq','am_tuning_curve')
exp0.add_session('14-28-12','b','optoNaturalInstances','natural_sound_detection')

exp0.add_site(2780)
# reference = 1:tip
# Electrode preset = All Shanks 97-192
exp0.add_session('14-56-45','c','optoTuningAM','am_tuning_curve') 
exp0.add_session('15-11-44','c','optoNaturalCategories','natural_sound_detection')
exp0.add_session('15-41-41','d','optoTuningFreq','am_tuning_curve')
exp0.add_session('15-58-18','d','optoNaturalInstances','natural_sound_detection')

exp0.maxDepth = 3500

# probe in brain around 13:00 pm

# exp 0 finish
# =================================2025-03-25============================================
# exp 1 start.
# shanks placed parallel to bregma-lambda axis, and around same position as yesterday.
exp1 = celldatabase.Experiment(subject, '2025-03-25', brainArea='right_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundLeft'])
experiments.append(exp1)

exp1.add_site(3500)

# Reference = 1:tip
# Electrode preset = All Shanks 1-96 
exp1.add_session('12-48-53','a','optoTuningAM','am_tuning_curve')  
#recorded 506 trials instead of 440.
exp1.add_session('13-56-00','a','optoNaturalCategories','natural_sound_detection')
# Its video behavior file got substituted with next one by mistake-vdofile recorded at  13:47, so recording this optonautralCategories again. first file for this is 13-05-22, and second is 13-56-00.
# The paradigm file(-extra) and ephy recoding is available for both 13-05-22 and 13-56-00.
exp1.add_session('13-32-36','b','optoTuningFreq','am_tuning_curve')
exp1.add_session('14-23-42','b','optoNaturalInstances','natural_sound_detection')

exp1.add_site(2780)
# reference = 1:tip
# Electrode preset = All Shanks 97-192
exp1.add_session('14-48-56','c','optoTuningAM','am_tuning_curve') 
exp1.add_session('15-03-05','c','optoNaturalCategories','natural_sound_detection')
exp1.add_session('15-32-03','d','optoTuningFreq','am_tuning_curve')
exp1.add_session('15-48-12','d','optoNaturalInstances','natural_sound_detection')

exp1.maxDepth = 3500
# exp1 finish

#========================================================================
#control exp start
#Same location as yesterday, 0.5mm medial to centre centre and parallel to Bregma-Lambda axis.
exp2 = celldatabase.Experiment(subject, '2025-03-27', brainArea='right_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_NoDye', info=['facesMedial', 'soundLeft'])
experiments.append(exp2)

exp2.add_site(3500)

# Reference = 1:tip
# Electrode preset = All Shanks 1-96 

exp2.add_session('12-24-00','a','optoTuningAM','am_tuning_curve')  
exp2.add_session('12-39-54','a','optoNaturalCategories','natural_sound_detection')
exp2.add_session('13-11-05','b','optoTuningFreq','am_tuning_curve')
exp2.add_session('13-28-35','b','optoNaturalInstances','natural_sound_detection')

exp2.add_site(2780)
# reference = 1:tip
# Electrode preset = All Shanks 97-192
exp2.add_session('13-51-14','c','optoTuningAM','am_tuning_curve') 
exp2.add_session('14-06-20','c','optoNaturalCategories','natural_sound_detection')
exp2.add_session('14-33-50','d','optoTuningFreq','am_tuning_curve')
exp2.add_session('14-52-51','d','optoNaturalInstances','natural_sound_detection')

exp2.maxDepth = 3500



# exp2 control finish


#exp finish


#========================================================================
#exp3 start=Left hemisphere 1st penetration.
#location: very centre of craniotomy- parallel to bregma lambda axis. 
exp3 = celldatabase.Experiment(subject, '2025-03-31', brainArea='left_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiD', info=['facesMedial', 'soundRight'])
experiments.append(exp3)

exp3.add_site(3500)

# Reference = 1:tip
# Electrode preset = All Shanks 1-96 
# optpNaturalCategories file was recorded at 12-36-21 successfully, but later only paradigm file was replaced with OptoNatural Instances, so repeated the second paradigm again.
exp3.add_session('12-21-12','a','optoTuningAM','am_tuning_curve')  
exp3.add_session('13-58-50','a','optoNaturalCategories','natural_sound_detection')
# Recording this again, as this file got replaced with Opto natural instances. So, two files- 12-36-21, which is extra and repeated one is 13-58-50.
exp3.add_session('13-03-14','b','optoTuningFreq','am_tuning_curve')
# More than 950 trials were recorded as I was in lab meeting, therefore couldn't stop the recording.
exp3.add_session('13-31-01','b','optoNaturalInstances','natural_sound_detection')
# This file replaced the Optonatural categories file, so recording Optonatural categories again.

exp3.add_site(2780)
# reference = 1:tip
# Electrode preset = All Shanks 97-192
exp3.add_session('14-36-28','c','optoTuningAM','am_tuning_curve') 
exp3.add_session('14-52-18','c','optoNaturalCategories','natural_sound_detection')
exp3.add_session('15-19-11','d','optoTuningFreq','am_tuning_curve')
exp3.add_session('15-37-10','d','optoNaturalInstances','natural_sound_detection')

exp3.maxDepth = 3500



# exp3 finish




#========================================================================
#exp4 start=Left hemisphere 2nd penetration.
#location: very centre of craniotomy- parallel to bregma lambda axis. 
exp4 = celldatabase.Experiment(subject, '2025-04-01', brainArea='left_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiI', info=['facesMedial', 'soundRight'])
experiments.append(exp4)
#went max depth 4000 as didn't see the depth, but pulled up the shanks again and recorded from 3500 and 2780.

exp4.add_site(3500)

# Reference = 1:tip
# Electrode preset = All Shanks 1-96 
exp4.add_session('11-11-06','a','optoTuningAM','am_tuning_curve')  
exp4.add_session('11-26-57','a','optoNaturalCategories','natural_sound_detection')
exp4.add_session('11-54-18','b','optoTuningFreq','am_tuning_curve')
exp4.add_session('12-12-24','b','optoNaturalInstances','natural_sound_detection')

exp4.add_site(2780)
# reference = 1:tip
# Electrode preset = All Shanks 97-192
exp4.add_session('12-37-07','c','optoTuningAM','am_tuning_curve') 
exp4.add_session('12-53-27','c','optoNaturalCategories','natural_sound_detection')
exp4.add_session('13-20-40','d','optoTuningFreq','am_tuning_curve')
exp4.add_session('13-36-37','d','optoNaturalInstances','natural_sound_detection')

exp4.maxDepth = 3500



# exp4 finish




#========================================================================
#exp5 start=Left hemisphere 3rd penetration-control.
#location: 0.2mm-0.3mm towards lateral of craniotomy- parallel to bregma lambda axis. 
exp5 = celldatabase.Experiment(subject, '2025-04-02', brainArea='left_pStr', probe = 'NPv2-1134', recordingTrack='centerCenter_DiO', info=['facesMedial', 'soundRight'])
experiments.append(exp5)

exp5.add_site(3500)

# Reference = 1:tip
# Electrode preset = All Shanks 1-96 
exp5.add_session('11-47-44','a','optoTuningAM','am_tuning_curve')  
exp5.add_session('12-02-15','a','optoNaturalCategories','natural_sound_detection')
exp5.add_session('12-31-11','b','optoTuningFreq','am_tuning_curve')
exp5.add_session('12-47-54','b','optoNaturalInstances','natural_sound_detection')

exp5.add_site(2780)
# reference = 1:tip
# Electrode preset = All Shanks 97-192
exp5.add_session('13-09-03','c','optoTuningAM','am_tuning_curve') 
exp5.add_session('13-23-43','c','optoNaturalCategories','natural_sound_detection')
exp5.add_session('13-52-04','d','optoTuningFreq','am_tuning_curve')
exp5.add_session('14-10-20','d','optoNaturalInstances','natural_sound_detection')

exp5.maxDepth = 3500



# exp5 finish















