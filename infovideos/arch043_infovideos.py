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

# 2025-12-18
#session with 440  trials
videos.add_session('2025-12-18', 'optoTuningAM',
                   'arch043_am_tuning_curve_20251218_01.mkv',
                   'arch043_am_tuning_curve_20251218a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-18', 'optoNaturalCategories',
                   'arch043_natural_sound_detection_20251218_02.mkv',
                   'arch043_natural_sound_detection_20251218a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-12-18', 'optoTuningFreq',
                   'arch043_am_tuning_curve_20251218_03.mkv',
                   'arch043_am_tuning_curve_20251218b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-12-18', 'optoNaturalInstances',
                   'arch043_natural_sound_detection_20251218_04.mkv',
                   'arch043_natural_sound_detection_20251218b.h5', cameraParams)

#Sessions with no laser going in the brain
#session with 440  trials
videos.add_session('2025-12-18', 'optoTuningAM',
                   'arch043_am_tuning_curve_20251218_05.mkv',
                   'arch043_am_tuning_curve_20251218g.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-18', 'optoNaturalCategories',
                   'arch043_natural_sound_detection_20251218_06.mkv',
                   'arch043_natural_sound_detection_20251218c.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-12-18', 'optoTuningFreq',
                   'arch043_am_tuning_curve_20251218_07.mkv',
                   'arch043_am_tuning_curve_20251218h.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-12-18', 'optoNaturalInstances',
                   'arch043_natural_sound_detection_20251218_08.mkv',
                   'arch043_natural_sound_detection_20251218d.h5', cameraParams)

# 2025-12-19
#session with 440  trials
videos.add_session('2025-12-19', 'optoTuningAM',
                   'arch043_am_tuning_curve_20251219_01.mkv',
                   'arch043_am_tuning_curve_20251219a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-19', 'optoNaturalCategories',
                   'arch043_natural_sound_detection_20251219_02.mkv',
                   'arch043_natural_sound_detection_20251219a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-12-19', 'optoTuningFreq',
                   'arch043_am_tuning_curve_20251219_03.mkv',
                   'arch043_am_tuning_curve_20251219b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-12-19', 'optoNaturalInstances',
                   'arch043_natural_sound_detection_20251219_04.mkv',
                   'arch043_natural_sound_detection_20251219b.h5', cameraParams)
