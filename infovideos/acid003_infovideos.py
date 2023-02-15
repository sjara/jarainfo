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
