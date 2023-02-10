from jaratoolbox import videoinfo

subject = 'acid003'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2023-02-10

videos.add_session('2023-02-10', 'prePureTones',
                   'acid003_am_tuning_curve_20230125_01pre.mkv',
                   'acid003_am_tuning_curve_20230125apre.h5', cameraParams) 

videos.add_session('2023-02-10', 'postPureTones',
                   'acid003_am_tuning_curve_20230125_01post.mkv',
                   'acid003_am_tuning_curve_20230125apost.h5', cameraParams) 
                   
  
videos.add_session('2023-02-10', 'prePureTones',
                   'acid003_am_tuning_curve_20230125_02pre.mkv',
                   'acid003_am_tuning_curve_20230125bpre.h5', cameraParams) 

videos.add_session('2023-02-10', 'postPureTones',
                   'acid003_am_tuning_curve_20230125_02post.mkv',
                   'acid003_am_tuning_curve_20230125bpost.h5', cameraParams) 


videos.add_session('2023-02-10', 'prePureTones',
                   'acid003_am_tuning_curve_20230125_03pre.mkv',
                   'acid003_am_tuning_curve_20230125cpre.h5', cameraParams) 

videos.add_session('2023-02-10', 'postPureTones',
                   'acid003_am_tuning_curve_20230125_03post.mkv',
                   'acid003_am_tuning_curve_20230125cpost.h5', cameraParams) 
                            
