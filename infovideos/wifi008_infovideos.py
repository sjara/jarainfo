from jaratoolbox import videoinfo

subject = 'wifi008'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

 # 2025-05-28

videos.add_session('2025-05-28', 'pureTones',
                   'wifi008_am_tuning_curve_20250528_01.mkv',
                   'wifi008_am_tuning_curve_20250528a.h5', cameraParams) 
                   
                   
videos.add_session('2025-05-28', 'naturalSounds',
                   'wifi008_natural_sound_detection_20250528_01.mkv',
                   'wifi008_natural_sound_detection_20250528a.h5', cameraParams) 
                   
videos.add_session('2025-05-28', 'AM',
                   'wifi008_am_tuning_curve_20250528_02.mkv',
                   'wifi008_am_tuning_curve_20250528b.h5', cameraParams) 
