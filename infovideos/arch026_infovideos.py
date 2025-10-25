from jaratoolbox import videoinfo

subject = 'arch026'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-10-24
#session with 400  trials
videos.add_session('2025-10-24', 'optoTuningAM',
                   'arch026_am_tuning_curve_20251024_01.mkv',
                   'arch026_am_tuning_curve_20251024c.h5', cameraParams)

#session with 440  trials
videos.add_session('2025-10-24', 'optoTuningAM',
                   'arch026_am_tuning_curve_20251024_02.mkv',
                   'arch026_am_tuning_curve_20251024d.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-10-24', 'optoNaturalCategories',
                   'arch026_natural_sound_detection_20251024_03.mkv',
                   'arch026_natural_sound_detection_20251024a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-10-24', 'optoTuningFreq',
                   'arch026_am_tuning_curve_20251024_04.mkv',
                   'arch026_am_tuning_curve_20251024e.h5', cameraParams)

#session with 160 trials - No ephys
#videos.add_session('2025-10-24', 'optoNaturalInstances',
#                   'arch026_natural_sound_detection_20251024_05.mkv',
#                   'arch026_natural_sound_detection_20251024b.h5', cameraParams)

#session with 160 trials - No ephys
videos.add_session('2025-10-24', 'optoNaturalInstances',
                   'arch026_natural_sound_detection_20251024_06.mkv',
                   'arch026_natural_sound_detection_20251024c.h5', cameraParams)
