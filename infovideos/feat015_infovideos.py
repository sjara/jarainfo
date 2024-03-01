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
                   
#2024-02-27

videos.add_session('2024-02-27', 'pureTones',
                   'feat015_am_tuning_curve_20240227_01.mkv',
                   'feat015_am_tuning_curve_20240227a.h5', cameraParams) 
                   
videos.add_session('2024-02-27', 'AM',
                   'feat015_am_tuning_curve_20240227_02.mkv',
                   'feat015_am_tuning_curve_20240227b.h5', cameraParams) 
                   
 #2024-02-28

videos.add_session('2024-02-28', 'pureTones',
                   'feat015_am_tuning_curve_20240228_01.mkv',
                   'feat015_am_tuning_curve_20240228a.h5', cameraParams) 
                   
videos.add_session('2024-02-28', 'AM',
                   'feat015_am_tuning_curve_20240228_02.mkv',
                   'feat015_am_tuning_curve_20240228b.h5', cameraParams)  
                   
#2024-03-01

videos.add_session('2024-03-01', 'pureTones',
                   'feat015_am_tuning_curve_20240301_01.mkv',
                   'feat015_am_tuning_curve_20240301a.h5', cameraParams) 
                   
videos.add_session('2024-03-01', 'AM',
                   'feat015_am_tuning_curve_20240301_02.mkv',
                   'feat015_am_tuning_curve_20240301b.h5', cameraParams)                                           
