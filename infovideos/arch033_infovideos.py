from jaratoolbox import videoinfo

subject = 'arch033'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-10-27
#session with 440  trials
videos.add_session('2025-10-27', 'optoTuningAM',
                   'arch033_am_tuning_curve_20251027_01.mkv',
                   'arch033_am_tuning_curve_20251027c.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-10-27', 'optoNaturalCategories',
                   'arch033_natural_sound_detection_20251027_02.mkv',
                   'arch033_natural_sound_detection_20251027a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-10-27', 'optoTuningFreq',
                   'arch033_am_tuning_curve_20251027_03.mkv',
                   'arch033_am_tuning_curve_20251027d.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-10-27', 'optoNaturalInstances',
                   'arch033_natural_sound_detection_20251027_04.mkv',
                   'arch033_natural_sound_detection_20251027b.h5', cameraParams)
