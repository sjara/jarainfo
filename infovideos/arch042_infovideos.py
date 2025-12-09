from jaratoolbox import videoinfo

subject = 'arch042'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-12-08
#session with 440  trials
videos.add_session('2025-12-08', 'optoTuningAM',
                   'arch042_am_tuning_curve_20251208_01.mkv',
                   'arch042_am_tuning_curve_20251208a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-08', 'optoNaturalCategories',
                   'arch042_natural_sound_detection_20251208_02.mkv',
                   'arch042_natural_sound_detection_20251208a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-12-08', 'optoTuningFreq',
                   'arch042_am_tuning_curve_20251208_03.mkv',
                   'arch042_am_tuning_curve_20251208b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-12-08', 'optoNaturalInstances',
                   'arch042_natural_sound_detection_20251208_04.mkv',
                   'arch042_natural_sound_detection_20251208b.h5', cameraParams)

