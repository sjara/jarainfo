from jaratoolbox import videoinfo

subject = 'feat016'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-03-21

videos.add_session('2024-03-21', 'pureTones',
                   'feat016_am_tuning_curve_20240321_01.mkv',
                   'feat016_am_tuning_curve_20240321a.h5', cameraParams) 
videos.add_session('2024-03-21', 'AM',
                   'feat016_am_tuning_curve_20240321_02.mkv',
                   'feat016_am_tuning_curve_20240321b.h5', cameraParams) 
videos.add_session('2024-03-21', 'naturalSound',
                   'feat016_natural_sound_detection_20240321_01.mkv',
                   'feat016_natural_sound_detection_20240321a.h5', cameraParams) 


# 2024-03-

videos.add_session('2024-03-xx', 'pureTones',
                   'feat016_am_tuning_curve_202403xx_01.mkv',
                   'feat016_am_tuning_curve_202403xxa.h5', cameraParams) 
videos.add_session('2024-03-xx', 'AM',
                   'feat016_am_tuning_curve_202403xx_02.mkv',
                   'feat016_am_tuning_curve_202403xxb.h5', cameraParams) 
videos.add_session('2024-03-xx', 'naturalSound',
                   'feat016_natural_sound_detection_202403xx_01.mkv',
                   'feat016_natural_sound_detection_202403xxa.h5', cameraParams) 
                   
                   
