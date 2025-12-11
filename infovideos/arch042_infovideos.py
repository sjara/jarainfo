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

# 2025-12-10
#session with 440  trials
videos.add_session('2025-12-10', 'optoTuningAM',
                   'arch042_am_tuning_curve_20251210_01.mkv',
                   'arch042_am_tuning_curve_20251210a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-10', 'optoNaturalCategories',
                   'arch042_natural_sound_detection_20251210_02.mkv',
                   'arch042_natural_sound_detection_20251210a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-12-10', 'optoTuningFreq',
                   'arch042_am_tuning_curve_20251210_03.mkv',
                   'arch042_am_tuning_curve_20251210b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-12-10', 'optoNaturalInstances',
                   'arch042_natural_sound_detection_20251210_04.mkv',
                   'arch042_natural_sound_detection_20251210b.h5', cameraParams)

# 2025-12-11
#session with 440  trials
videos.add_session('2025-12-11', 'optoTuningAM',
                   'arch042_am_tuning_curve_20251211_01.mkv',
                   'arch042_am_tuning_curve_20251211a.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-11', 'optoNaturalCategories',
                   'arch042_natural_sound_detection_20251211_02.mkv',
                   'arch042_natural_sound_detection_20251211a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-12-11', 'optoTuningFreq',
                   'arch042_am_tuning_curve_20251211_03.mkv',
                   'arch042_am_tuning_curve_20251211b.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-12-11', 'optoNaturalInstances',
                   'arch042_natural_sound_detection_20251211_04.mkv',
                   'arch042_natural_sound_detection_20251211b.h5', cameraParams)

#Sessins with laser outside of the brain
#session with 440  trials
videos.add_session('2025-12-11', 'optoTuningAM',
                   'arch042_am_tuning_curve_20251211_05.mkv',
                   'arch042_am_tuning_curve_20251211e.h5', cameraParams)

#session with 200 trials
videos.add_session('2025-12-11', 'optoNaturalCategories',
                   'arch042_natural_sound_detection_20251211_06.mkv',
                   'arch042_natural_sound_detection_20251211c.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2025-12-11', 'optoTuningFreq',
                   'arch042_am_tuning_curve_20251211_07.mkv',
                   'arch042_am_tuning_curve_20251211f.h5', cameraParams)

#session with 160 trials
videos.add_session('2025-12-11', 'optoNaturalInstances',
                   'arch042_natural_sound_detection_20251211_08.mkv',
                   'arch042_natural_sound_detection_20251211d.h5', cameraParams)
