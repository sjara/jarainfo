from jaratoolbox import videoinfo

subject = 'arch032'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-10-16 bank 1-96
#session with 440  trials
videos.add_session('2025-10-16', 'optoTuningAM',
                   'arch032_am_tuning_curve_20251016_01.mkv',
                   'arch032_am_tuning_curve_20251016a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-10-16', 'optoNaturalCategories',
                   'arch032_natural_sound_detection_20251016_02.mkv',
                   'arch032_natural_sound_detection_20251016a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-10-16', 'optoTuningFreq',
                   'arch032_am_tuning_curve_20251016_03.mkv',
                   'arch032_am_tuning_curve_20251016b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-10-16', 'optoNaturalInstances',
                   'arch032_natural_sound_detection_20251016_04.mkv',
                   'arch032_natural_sound_detection_20251016b.h5', cameraParams)

# 2025-10-16 bank 97-192
#session with 440  trials
videos.add_session('2025-10-16', 'optoTuningAM',
                   'arch032_am_tuning_curve_20251016_05.mkv',
                   'arch032_am_tuning_curve_20251016c.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-10-16', 'optoNaturalCategories',
                   'arch032_natural_sound_detection_20251016_06.mkv',
                   'arch032_natural_sound_detection_20251016c.h5', cameraParams)

#session with 640 trials
videos.add_session('2025-10-16', 'optoTuningFreq',
                   'arch032_am_tuning_curve_20251016_07.mkv',
                   'arch032_am_tuning_curve_20251016d.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-10-16', 'optoNaturalInstances',
                   'arch032_natural_sound_detection_20251016_08.mkv',
                   'arch032_natural_sound_detection_20251016d.h5', cameraParams)

# -------------------------------------------------

# 2025-10-17 bank 1-96
#session with 440  trials
videos.add_session('2025-10-17', 'optoTuningAM',
                   'arch032_am_tuning_curve_20251017_01.mkv',
                   'arch032_am_tuning_curve_20251017a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-10-17', 'optoNaturalCategoriesnaturalSound',
                   'arch032_natural_sound_detection_20251017_02.mkv',
                   'arch032_natural_sound_detection_20251017a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-10-17', 'optoTuningFreq',
                   'arch032_am_tuning_curve_20251017_03.mkv',
                   'arch032_am_tuning_curve_20251017b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-10-17', 'optoNaturalInstances',
                   'arch032_natural_sound_detection_20251017_04.mkv',
                   'arch032_natural_sound_detection_20251017b.h5', cameraParams)
