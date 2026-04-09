from jaratoolbox import videoinfo

subject = 'arch051'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

#2026-03-05
#Shanks 1 and 2. Manually selected channels 1-96 and 97-192.
#session with 440  trials
videos.add_session('2026-03-05', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260305_01.mkv',
                   'arch051_am_tuning_curve_20260305a.h5', cameraParams)

#session with 200 trials
videos.add_session('2026-03-05', 'optoNaturalCategories',
                   'arch051_natural_sound_detection_20260305_02.mkv',
                   'arch051_natural_sound_detection_20260305a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2026-03-05', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260305_03.mkv',
                   'arch051_am_tuning_curve_20260305b.h5', cameraParams)

#session with 160 trials
videos.add_session('2026-03-05', 'optoNaturalInstances',
                   'arch051_natural_sound_detection_20260305_04.mkv',
                   'arch051_natural_sound_detection_20260305b.h5', cameraParams)

#2026-03-19
#All shanks  1-96 
#session with 440  trials
videos.add_session('2026-03-19', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260319_01.mkv',
                   'arch051_am_tuning_curve_20260319a.h5', cameraParams)

#session with 200 trials
videos.add_session('2026-03-19', 'optoNaturalCategories',
                   'arch051_natural_sound_detection_20260319_02.mkv',
                   'arch051_natural_sound_detection_20260319a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2026-03-19', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260319_03.mkv',
                   'arch051_am_tuning_curve_20260319b.h5', cameraParams)

#session with 160 trials
videos.add_session('2026-03-19', 'optoNaturalInstances',
                   'arch051_natural_sound_detection_20260319_04.mkv',
                   'arch051_natural_sound_detection_20260319b.h5', cameraParams)

#All shanks  97-192.
#session with 440  trials
videos.add_session('2026-03-19', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260319_05.mkv',
                   'arch051_am_tuning_curve_20260319c.h5', cameraParams)

#session with 200 trials
videos.add_session('2026-03-19', 'optoNaturalCategories',
                   'arch051_natural_sound_detection_20260319_06.mkv',
                   'arch051_natural_sound_detection_20260319c.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2026-03-19', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260319_07.mkv',
                   'arch051_am_tuning_curve_20260319d.h5', cameraParams)

#session with 160 trials
videos.add_session('2026-03-19', 'optoNaturalInstances',
                   'arch051_natural_sound_detection_20260319_08.mkv',
                   'arch051_natural_sound_detection_20260319d.h5', cameraParams)

#Control sessions
#All shanks  1-96 
#session with 440  trials
videos.add_session('2026-03-19', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260319_09.mkv',
                   'arch051_am_tuning_curve_20260319e.h5', cameraParams)

#session with 640 trials
videos.add_session('2026-03-19', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260319_10.mkv',
                   'arch051_am_tuning_curve_20260319f.h5', cameraParams)

#All shanks   97-192
#session with 440  trials
videos.add_session('2026-03-19', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260319_11.mkv',
                   'arch051_am_tuning_curve_20260319g.h5', cameraParams)

#session with 640 trials
videos.add_session('2026-03-19', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260319_12.mkv',
                   'arch051_am_tuning_curve_20260319h.h5', cameraParams)

#2026-03-20
#All shanks  1-96 
#session with 440  trials
videos.add_session('2026-03-20', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260320_01.mkv',
                   'arch051_am_tuning_curve_20260320a.h5', cameraParams)

#session with 200 trials
videos.add_session('2026-03-20', 'optoNaturalCategories',
                   'arch051_natural_sound_detection_20260320_02.mkv',
                   'arch051_natural_sound_detection_20260320a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2026-03-20', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260320_03.mkv',
                   'arch051_am_tuning_curve_20260320b.h5', cameraParams)

#session with 160 trials
videos.add_session('2026-03-20', 'optoNaturalInstances',
                   'arch051_natural_sound_detection_20260320_04.mkv',
                   'arch051_natural_sound_detection_20260320b.h5', cameraParams)

#All shanks  97-192.
#session with 440  trials
videos.add_session('2026-03-20', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260320_05.mkv',
                   'arch051_am_tuning_curve_20260320c.h5', cameraParams)

#session with 200 trials
videos.add_session('2026-03-20', 'optoNaturalCategories',
                   'arch051_natural_sound_detection_20260320_06.mkv',
                   'arch051_natural_sound_detection_20260320c.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2026-03-20', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260320_07.mkv',
                   'arch051_am_tuning_curve_20260320d.h5', cameraParams)

#session with 160 trials
videos.add_session('2026-03-20', 'optoNaturalInstances',
                   'arch051_natural_sound_detection_20260320_08.mkv',
                   'arch051_natural_sound_detection_20260320d.h5', cameraParams)

#2026-03-26
#All shanks  1-96 
#session with 440  trials
videos.add_session('2026-03-26', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260326_01.mkv',
                   'arch051_am_tuning_curve_20260326a.h5', cameraParams)

#session with 200 trials
videos.add_session('2026-03-26', 'optoNaturalCategories',
                   'arch051_natural_sound_detection_20260326_02.mkv',
                   'arch051_natural_sound_detection_20260326a.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2026-03-26', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260326_03.mkv',
                   'arch051_am_tuning_curve_20260326b.h5', cameraParams)

#session with 160 trials
videos.add_session('2026-03-26', 'optoNaturalInstances',
                   'arch051_natural_sound_detection_20260326_04.mkv',
                   'arch051_natural_sound_detection_20260326b.h5', cameraParams)

#All shanks  97-192.
#session with 440  trials
videos.add_session('2026-03-26', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260326_05.mkv',
                   'arch051_am_tuning_curve_20260326c.h5', cameraParams)

#session with 200 trials
videos.add_session('2026-03-26', 'optoNaturalCategories',
                   'arch051_natural_sound_detection_20260326_06.mkv',
                   'arch051_natural_sound_detection_20260326c.h5', cameraParams)
        
 
#session with 640 trials
videos.add_session('2026-03-26', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260326_07.mkv',
                   'arch051_am_tuning_curve_20260326d.h5', cameraParams)

#session with 160 trials
videos.add_session('2026-03-26', 'optoNaturalInstances',
                   'arch051_natural_sound_detection_20260326_08.mkv',
                   'arch051_natural_sound_detection_20260326d.h5', cameraParams)

#Control sessions
#All shanks  1-96 
#session with 440  trials
videos.add_session('2026-03-26', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260326_09.mkv',
                   'arch051_am_tuning_curve_20260326e.h5', cameraParams)

#session with 640 trials
videos.add_session('2026-03-26', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260326_10.mkv',
                   'arch051_am_tuning_curve_20260326f.h5', cameraParams)

#All shanks   97-192
#session with 440  trials
videos.add_session('2026-03-26', 'optoTuningAM',
                   'arch051_am_tuning_curve_20260326_11.mkv',
                   'arch051_am_tuning_curve_20260326g.h5', cameraParams)

#session with 640 trials
videos.add_session('2026-03-26', 'optoTuningFreq',
                   'arch051_am_tuning_curve_20260326_12.mkv',
                   'arch051_am_tuning_curve_20260326h.h5', cameraParams)
