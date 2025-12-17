from jaratoolbox import videoinfo

subject = 'arch040'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

#The natural sound category does not have a recorded video in exp0.
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


#session with 160 trials
videos.add_session('2025-12-09', 'optoNaturalInstances',
                   'arch040_natural_sound_detection_20251209_04.mkv',
                   'arch040_natural_sound_detection_20251209b.h5', cameraParams)

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-12-14
#session with 440  trials
videos.add_session('2025-12-14', 'optoTuningAM',
                   'arch040_am_tuning_curve_20251214_01.mkv',
                   'arch040_am_tuning_curve_20251214a.h5', cameraParams)

 
#session with 640 trials
videos.add_session('2025-12-14', 'optoTuningFreq',
                   'arch040_am_tuning_curve_20251214_02.mkv',
                   'arch040_am_tuning_curve_20251214b.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-14', 'optoNaturalCategories',
                   'arch040_natural_sound_detection_20251214_03.mkv',
                   'arch040_natural_sound_detection_20251214a.h5', cameraParams)
        

#session with 160 trials
videos.add_session('2025-12-14', 'optoNaturalInstances',
                   'arch040_natural_sound_detection_20251214_04.mkv',
                   'arch040_natural_sound_detection_20251214b.h5', cameraParams)


#These recordings are with the laser shining outside of the brain.
#session with 440  trials
videos.add_session('2025-12-14', 'optoTuningAM',
                   'arch040_am_tuning_curve_20251214_05.mkv',
                   'arch040_am_tuning_curve_20251214c.h5', cameraParams)

 
#session with 640 trials
videos.add_session('2025-12-14', 'optoTuningFreq',
                   'arch040_am_tuning_curve_20251214_06.mkv',
                   'arch040_am_tuning_curve_20251214d.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-14', 'optoNaturalCategories',
                   'arch040_natural_sound_detection_20251214_07.mkv',
                   'arch040_natural_sound_detection_20251214c.h5', cameraParams)
        

#session with 160 trials
videos.add_session('2025-12-14', 'optoNaturalInstances',
                   'arch040_natural_sound_detection_20251214_08.mkv',
                   'arch040_natural_sound_detection_20251214d.h5', cameraParams)


# 2025-12-16
#session with 440  trials
videos.add_session('2025-12-16', 'optoTuningAM',
                   'arch040_am_tuning_curve_20251216_01.mkv',
                   'arch040_am_tuning_curve_20251216a.h5', cameraParams)

 
#session with 640 trials
videos.add_session('2025-12-16', 'optoTuningFreq',
                   'arch040_am_tuning_curve_20251216_02.mkv',
                   'arch040_am_tuning_curve_20251216b.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-16', 'optoNaturalCategories',
                   'arch040_natural_sound_detection_20251216_03.mkv',
                   'arch040_natural_sound_detection_20251216a.h5', cameraParams)
        

#session with 160 trials
videos.add_session('2025-12-16', 'optoNaturalInstances',
                   'arch040_natural_sound_detection_20251216_04.mkv',
                   'arch040_natural_sound_detection_20251216b.h5', cameraParams)

#These recordings are with the laser shining outside of the brain.
#session with 440  trials
videos.add_session('2025-12-16', 'optoTuningAM',
                   'arch040_am_tuning_curve_20251216_05.mkv',
                   'arch040_am_tuning_curve_20251216c.h5', cameraParams)

 
#session with 640 trials
videos.add_session('2025-12-16', 'optoTuningFreq',
                   'arch040_am_tuning_curve_20251216_06.mkv',
                   'arch040_am_tuning_curve_20251216d.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-16', 'optoNaturalCategories',
                   'arch040_natural_sound_detection_20251216_07.mkv',
                   'arch040_natural_sound_detection_20251216c.h5', cameraParams)
        

#session with 160 trials
videos.add_session('2025-12-16', 'optoNaturalInstances',
                   'arch040_natural_sound_detection_20251216_08.mkv',
                   'arch040_natural_sound_detection_20251216d.h5', cameraParams)
