from jaratoolbox import videoinfo

subject = 'feat017'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-03-25

videos.add_session('2024-03-25', 'pureTones',
                   'feat017_am_tuning_curve_20240325_01.mkv',
                   'feat017_am_tuning_curve_20240325a.h5', cameraParams) 
                   
videos.add_session('2024-03-25', 'AM',
                   'feat017_am_tuning_curve_20240325_02.mkv',
                   'feat017_am_tuning_curve_20240325b.h5', cameraParams)  
                   
videos.add_session('2024-03-25', 'naturalSounds',
                   'feat017_natural_sound_detection_20240325_01.mkv',
                   'feat017_natural_sound_detection_20240325a.h5', cameraParams) 
                   
# 2024-03-26

videos.add_session('2024-03-26', 'pureTones',
                   'feat017_am_tuning_curve_20240326_01.mkv',
                   'feat017_am_tuning_curve_20240326a.h5', cameraParams) 
                   
videos.add_session('2024-03-26', 'AM',
                   'feat017_am_tuning_curve_20240326_02.mkv',
                   'feat017_am_tuning_curve_20240326b.h5', cameraParams)  
                   
videos.add_session('2024-03-26', 'naturalSounds',
                   'feat017_natural_sound_detection_20240326_01.mkv',
                   'feat017_natural_sound_detection_20240326a.h5', cameraParams) 
                   
# 2024-03-27 

videos.add_session('2024-03-27', 'pureTones',
                   'feat017_am_tuning_curve_20240327_01.mkv',
                   'feat017_am_tuning_curve_20240327a.h5', cameraParams) 
                   
videos.add_session('2024-03-27', 'AM',
                   'feat017_am_tuning_curve_20240327_02.mkv',
                   'feat017_am_tuning_curve_20240327b.h5', cameraParams)  
                   
videos.add_session('2024-03-27', 'naturalSounds',
                   'feat017_natural_sound_detection_20240327_01.mkv',
                   'feat017_natural_sound_detection_20240327a.h5', cameraParams) 
                   
#2024-03-28

