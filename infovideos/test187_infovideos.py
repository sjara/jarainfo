from jaratoolbox import videoinfo

subject = 'test187'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

 # 2025-10-07
#This is the session with 140 trials
videos.add_session('2025-10-07', 'optoTuningFreq',
                   'test187_am_tuning_curve_20251007_01.mkv',
                   'test187_am_tuning_curve_20251007a.h5', cameraParams) 
                   
                   
#videos.add_session('2025-05-28', 'naturalSounds',
#                   'wifi008_natural_sound_detection_20250528_01.mkv',
#                   'wifi008_natural_sound_detection_20250528.h5', cameraParams)

#session with 320 trials
videos.add_session('2025-10-07', 'optoTuningFreq',
                   'test187_am_tuning_curve_20251007_03.mkv',
                   'test187_am_tuning_curve_20251007c.h5', cameraParams)

#session with 220 trials
videos.add_session('2025-10-07', 'optoTuningAM',
                   'test187_am_tuning_curve_20251007_04.mkv',
                   'test187_am_tuning_curve_20251007d.h5', cameraParams) 
