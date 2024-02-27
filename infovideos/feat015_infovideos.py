from jaratoolbox import videoinfo

subject = 'feat015'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-02-23

videos.add_session('2024-02-23', 'pureTones',
                   'feat015_am_tuning_curve_20240223_01.mkv',
                   'feat015_am_tuning_curve_20240223a.h5', cameraParams) 
                   
videos.add_session('2024-02-23', 'AM',
                   'feat015_am_tuning_curve_20240223_02.mkv',
                   'feat015_am_tuning_curve_20240223b.h5', cameraParams)                    
