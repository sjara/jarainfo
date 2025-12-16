from jaratoolbox import videoinfo

subject = 'arch043'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-12-15
#session with 440  trials
videos.add_session('2025-12-15', 'optoTuningAM',
                   'arch043_am_tuning_curve_20251215_01.mkv',
                   'arch043_am_tuning_curve_20251215a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-15', 'optoNaturalCategories',
                   'arch043_natural_sound_detection_20251215_02.mkv',
                   'arch043_natural_sound_detection_20251215a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-12-15', 'optoTuningFreq',
                   'arch043_am_tuning_curve_20251215_03.mkv',
                   'arch043_am_tuning_curve_20251215b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-12-15', 'optoNaturalInstances',
                   'arch043_natural_sound_detection_20251215_04.mkv',
                   'arch043_natural_sound_detection_20251215b.h5', cameraParams)
