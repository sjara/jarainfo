from jaratoolbox import videoinfo

subject = 'arch034'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-11-10
#session with 440  trials
videos.add_session('2025-11-10', 'optoTuningAM',
                   'arch034_am_tuning_curve_20251110_01.mkv',
                   'arch034_am_tuning_curve_20251110a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-11-10', 'optoNaturalCategories',
                   'arch034_natural_sound_detection_20251110_02.mkv',
                   'arch034_natural_sound_detection_20251110a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-11-10', 'optoTuningFreq',
                   'arch034_am_tuning_curve_20251110_03.mkv',
                   'arch034_am_tuning_curve_20251110b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-11-10', 'optoNaturalInstances',
                   'arch034_natural_sound_detection_20251110_04.mkv',
                   'arch034_natural_sound_detection_20251110b.h5', cameraParams)

# 2025-11-12
#session with 461  trials
videos.add_session('2025-11-12', 'optoTuningAM',
                   'arch034_am_tuning_curve_20251112_01.mkv',
                   'arch034_am_tuning_curve_20251112a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-11-12', 'optoNaturalCategories',
                   'arch034_natural_sound_detection_20251112_02.mkv',
                   'arch034_natural_sound_detection_20251112a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-11-12', 'optoTuningFreq',
                   'arch034_am_tuning_curve_20251112_03.mkv',
                   'arch034_am_tuning_curve_20251112b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-11-12', 'optoNaturalInstances',
                   'arch034_natural_sound_detection_20251112_04.mkv',
                   'arch034_natural_sound_detection_20251112b.h5', cameraParams)
