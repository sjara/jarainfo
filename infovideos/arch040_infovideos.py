from jaratoolbox import videoinfo

subject = 'arch040'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-12-09
#session with 440  trials
videos.add_session('2025-12-09', 'optoTuningAM',
                   'arch040_am_tuning_curve_20251209_01.mkv',
                   'arch040_am_tuning_curve_20251209a.h5', cameraParams)

 
#session with 640 trials
videos.add_session('2025-12-09', 'optoTuningFreq',
                   'arch040_am_tuning_curve_20251209_02.mkv',
                   'arch040_am_tuning_curve_20251209b.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-09', 'optoNaturalCategories',
                   'arch040_natural_sound_detection_20251209_03.mkv',
                   'arch034_natural_sound_detection_20251209a.h5', cameraParams)
        

#session with 160 trials
videos.add_session('2025-12-09', 'optoNaturalInstances',
                   'arch040_natural_sound_detection_20251209_04.mkv',
                   'arch040_natural_sound_detection_20251209b.h5', cameraParams)


