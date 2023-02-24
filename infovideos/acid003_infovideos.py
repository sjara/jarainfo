from jaratoolbox import videoinfo

subject = 'acid003'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2023-02-10

videos.add_session('2023-02-10', 'prePureTones',
                   'acid003_am_tuning_curve_20230210_01pre.mkv',
                   'acid003_am_tuning_curve_20230125apre.h5', cameraParams) 

videos.add_session('2023-02-10', 'postPureTones',
                   'acid003_am_tuning_curve_20230210_01post.mkv',
                   'acid003_am_tuning_curve_20230125apost.h5', cameraParams) 
                   
  
videos.add_session('2023-02-10', 'prePureTones',
                   'acid003_am_tuning_curve_20230210_02pre.mkv',
                   'acid003_am_tuning_curve_20230125bpre.h5', cameraParams) 

videos.add_session('2023-02-10', 'postPureTones',
                   'acid003_am_tuning_curve_20230210_02post.mkv',
                   'acid003_am_tuning_curve_20230125bpost.h5', cameraParams) 


videos.add_session('2023-02-10', 'prePureTones',
                   'acid003_am_tuning_curve_20230210_03pre.mkv',
                   'acid003_am_tuning_curve_20230125cpre.h5', cameraParams) 

videos.add_session('2023-02-10', 'postPureTones',
                   'acid003_am_tuning_curve_20230210_03post.mkv',
                   'acid003_am_tuning_curve_20230125cpost.h5', cameraParams) 


# 2023-02-15

videos.add_session('2023-02-15', 'prePureTones',
                   'acid003_am_tuning_curve_20230215_01pre.mkv',
                   'acid003_am_tuning_curve_20230215apre.h5', cameraParams) 

videos.add_session('2023-02-15', 'postPureTones',
                   'acid003_am_tuning_curve_20230215_01post.mkv',
                   'acid003_am_tuning_curve_20230215apost.h5', cameraParams) 
                   
  
videos.add_session('2023-02-15', 'prePureTones',
                   'acid003_am_tuning_curve_20230215_02pre.mkv',
                   'acid003_am_tuning_curve_20230215bpre.h5', cameraParams) 

videos.add_session('2023-02-15', 'postPureTones',
                   'acid003_am_tuning_curve_20230215_02post.mkv',
                   'acid003_am_tuning_curve_20230215bpost.h5', cameraParams) 


videos.add_session('2023-02-15', 'prePureTones',
                   'acid003_am_tuning_curve_20230215_03pre.mkv',
                   'acid003_am_tuning_curve_20230215cpre.h5', cameraParams) 

videos.add_session('2023-02-15', 'postPureTones',
                   'acid003_am_tuning_curve_20230215_03post.mkv',
                   'acid003_am_tuning_curve_20230215cpost.h5', cameraParams)
                   

# 2023-02-16

videos.add_session('2023-02-16', 'prePureTones',
                   'acid003_am_tuning_curve_20230216_01pre.mkv',
                   'acid003_am_tuning_curve_20230216apre.h5', cameraParams) 

videos.add_session('2023-02-16', 'preHighFreq',
                   'acid003_oddball_sequence_20230216_01pre.mkv',
                   'acid003_oddball_sequence_20230216apre', cameraParams) 

videos.add_session('2023-02-16', 'preLowFreq',
                   'acid003_oddball_sequence_20230216_02pre.mkv',
                   'acid003_oddball_sequence_20230216bpre', cameraParams)

videos.add_session('2023-02-16', 'preFM_Down',
                   'acid003_oddball_sequence_20230216_03pre.mkv',
                   'acid003_oddball_sequence_20230216cpre', cameraParams)
                   
videos.add_session('2023-02-16', 'preFM_Up',
                   'acid003_oddball_sequence_20230216_04pre.mkv',
                   'acid003_oddball_sequence_20230216dpre', cameraParams)
# Saline

videos.add_session('2023-02-16', 'postPureTones',
                   'acid003_am_tuning_curve_20230216_01post.mkv',
                   'acid003_am_tuning_curve_20230216apost.h5', cameraParams) 

videos.add_session('2023-02-16', 'postHighFreq',
                   'acid003_oddball_sequence_20230216_01post.mkv',
                   'acid003_oddball_sequence_20230216apost', cameraParams) 

videos.add_session('2023-02-16', 'postLowFreq',
                   'acid003_oddball_sequence_20230216_02post.mkv',
                   'acid003_oddball_sequence_20230216bpost', cameraParams)

videos.add_session('2023-02-16', 'postFM_Down',
                   'acid003_oddball_sequence_20230216_03post.mkv',
                   'acid003_oddball_sequence_20230216cpost', cameraParams)
                   
videos.add_session('2023-02-16', 'postFM_Up',
                   'acid003_oddball_sequence_20230216_04post.mkv',
                   'acid003_oddball_sequence_20230216dpost', cameraParams)
                   

# 2023-02-22
# bad data. ephys computer ran out of space
#videos.add_session('2023-02-22', 'prePureTones',
#                   'acid003_am_tuning_curve_20230222_01pre.mkv',
#                   'acid003_am_tuning_curve_20230222apre.h5', cameraParams) 

#videos.add_session('2023-02-22', 'postPureTones',
#                   'acid003_am_tuning_curve_20230222_01post.mkv',
#                   'acid003_am_tuning_curve_20230222apost.h5', cameraParams) 
                   

# 2023-02-24

videos.add_session('2023-02-24', 'prePureTones',
                   'acid003_am_tuning_curve_20230224_01pre.mkv',
                   'acid003_am_tuning_curve_20230224apre.h5', cameraParams) 

videos.add_session('2023-02-24', 'postPureTones',
                   'acid003_am_tuning_curve_20230224_01post.mkv',
                   'acid003_am_tuning_curve_20230224apost.h5', cameraParams) 
                     
videos.add_session('2023-02-24', 'prePureTones',
                   'acid003_am_tuning_curve_20230224_02pre.mkv',
                   'acid003_am_tuning_curve_20230224bpre.h5', cameraParams) 

videos.add_session('2023-02-24', 'postPureTones',
                   'acid003_am_tuning_curve_20230224_02post.mkv',
                   'acid003_am_tuning_curve_20230224bpost.h5', cameraParams) 

videos.add_session('2023-02-24', 'prePureTones',
                   'acid003_am_tuning_curve_20230224_03pre.mkv',
                   'acid003_am_tuning_curve_20230224cpre.h5', cameraParams) 

videos.add_session('2023-02-24', 'postPureTones',
                   'acid003_am_tuning_curve_20230224_03post.mkv',
                   'acid003_am_tuning_curve_20230224cpost.h5', cameraParams) 
