from jaratoolbox import videoinfo

subject = 'test152'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-12-xx

videos.add_session('2024-12-xx', 'pureTones',
                   'test152_am_tuning_curve_202412xx_01.mkv',
                   'test152_am_tuning_curve_202412xxa.h5', cameraParams) 
                   
                   
videos.add_session('2024-12-xx', 'naturalSounds',
                   'test152_natural_sound_detection_202412xx_01.mkv',
                   'test152_natural_sound_detection_202412xxa.h5', cameraParams) 
                   
videos.add_session('2024-12-xx', 'AM',
                   'test152_am_tuning_curve_202412xx_02.mkv',
                   'test152_am_tuning_curve_202412xxb.h5', cameraParams) 
