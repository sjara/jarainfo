from jaratoolbox import videoinfo

subject = 'arch024'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2025-04-10

videos.add_session('2025-04-10', 'optoTuningAM',
                   'arch024_am_tuning_curve_20250410_01.mkv',
                   'arch024_am_tuning_curve_20250410a.h5', cameraParams) 
                   
                
                
videos.add_session('2025-04-10', 'optoNaturalCategories',
                   'arch024_natural_sound_detection_20250410_01.mkv',
                   'arch024_natural_sound_detection_20250410a.h5', cameraParams) 
                  
videos.add_session('2025-04-10', 'optoTuningFreq',
                   'arch024_am_tuning_curve_20250410_02.mkv',
                   'arch024_am_tuning_curve_20250410b.h5', cameraParams) 
                   
                  
videos.add_session('2025-04-10', 'optoNaturalInstances',
                   'arch024_natural_sound_detection_20250410_02.mkv',
                   'arch024_natural_sound_detection_20250410b.h5', cameraParams) 
                   
                   
videos.add_session('2025-04-10', 'optoTuningAM',
                   'arch024_am_tuning_curve_20250410_03.mkv',
                   'arch024_am_tuning_curve_20250410c.h5', cameraParams) 
                    
                   
videos.add_session('2025-04-10', 'optoNaturalCategories',
                   'arch024_natural_sound_detection_20250410_03.mkv',
                   'arch024_natural_sound_detection_20250410c.h5', cameraParams) 
                    
videos.add_session('2025-04-10', 'optoTuningFreq',
                   'arch024_am_tuning_curve_20250410_04.mkv',
                   'arch024_am_tuning_curve_20250410d.h5', cameraParams) 
                   
                   
videos.add_session('2025-04-10', 'optoNaturalInstances',
                   'arch024_natural_sound_detection_20250410_04.mkv',
                   'arch024_natural_sound_detection_20250410d.h5', cameraParams) 

#===================================================================
#2025-04-11
