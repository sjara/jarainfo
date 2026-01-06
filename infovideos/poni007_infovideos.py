'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'poni007'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2025-11-03', 'optoTuningAMtone',
                   'poni007_am_tuning_curve_20251103_01-03_VP9.mkv',
                   'poni007_am_tuning_curve_20251103a.h5',
                   cameraParams) 

videos.add_session('2025-11-03', 'optoTuningFreq',
                   'poni007_am_tuning_curve_20251103_01-05_VP9.mkv',
                   'poni007_am_tuning_curve_20251103b.h5',
                   cameraParams) 

videos.add_session('2025-12-04', 'optoShamAMtone',
                   'poni007_am_tuning_curve_20251204_01_VP9.mkv',
                   'poni007_am_tuning_curve_20251204a.h5',
                   cameraParams) 

videos.add_session('2025-12-04', 'naturalSoundLoc',
                   'poni007_natural_sound_detection_20251204_01_VP9.mkv',
                   'poni007_natural_sound_detection_20251204a.h5',
                   cameraParams) 

videos.add_session('2025-12-05', 'optoShamAMtone',
                   'poni007_am_tuning_curve_20251205_01_VP9.mkv',
                   'poni007_am_tuning_curve_20251205a.h5',
                   cameraParams) 

videos.add_session('2025-12-05', 'naturalSoundLoc',
                   'poni007_natural_sound_detection_20251205_01_VP9.mkv',
                   'poni007_natural_sound_detection_20251205a.h5',
                   cameraParams) 