from jaratoolbox import videoinfo

subject = 'feat018'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-06-06

videos.add_session('2024-06-06', 'pureTones',
                   'feat018_am_tuning_curve_20240606_01.mkv',
                   'feat018_am_tuning_curve_20240606a.h5', cameraParams) 
                   
                   
videos.add_session('2024-06-06', 'naturalSounds',
                   'feat018_natural_sound_detection_20240606_01.mkv',
                   'feat018_natural_sound_detection_20240606a.h5', cameraParams) 
                   
videos.add_session('2024-06-06', 'AM',
                   'feat018_am_tuning_curve_20240606_02.mkv',
                   'feat018_am_tuning_curve_20240606b.h5', cameraParams) 
                   
                   
# 2024-06-07

videos.add_session('2024-06-07', 'pureTones',
                   'feat018_am_tuning_curve_20240607_01.mkv',
                   'feat018_am_tuning_curve_20240607a.h5', cameraParams) 
                   
                   
videos.add_session('2024-06-07', 'naturalSounds',
                   'feat018_natural_sound_detection_20240607_01.mkv',
                   'feat018_natural_sound_detection_20240607a.h5', cameraParams) 
                   
videos.add_session('2024-06-07', 'AM',
                   'feat018_am_tuning_curve_20240607_02.mkv',
                   'feat018_am_tuning_curve_20240607b.h5', cameraParams) 
