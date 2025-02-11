from jaratoolbox import videoinfo

subject = 'test164'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-02-xx

videos.add_session('2025-02-xx', 'pureTones',
                   'test164_am_tuning_curve_202502xx_01.mkv',
                   'test164_am_tuning_curve_202502xxa.h5', cameraParams) 
                   
                   
videos.add_session('2025-02-xx', 'naturalSounds',
                   'test164_natural_sound_detection_202502xx_01.mkv',
                   'test1164_natural_sound_detection_202502xxa.h5', cameraParams) 
                   
videos.add_session('2025-02-xx', 'AM',
                   'test164_am_tuning_curve_202502xx_02.mkv',
                   'test164_am_tuning_curve_202502xxb.h5', cameraParams) 
