'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'poni005'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2025-11-06', 'optoTuningAMtone',
                   'poni005_am_tuning_curve_20251106_01-01_VP9.mkv',
                   'poni005_am_tuning_curve_20251106a.h5',
                   cameraParams) 

videos.add_session('2025-11-06', 'optoTuningFreq',
                   'poni005_am_tuning_curve_20251106_01-02_VP9.mkv',
                   'poni005_am_tuning_curve_20251106b.h5',
                   cameraParams) 

videos.add_session('2025-11-07', 'optoTuningAMtone',
                   'poni005_am_tuning_curve_20251107_01-01_VP9.mkv',
                   'poni005_am_tuning_curve_20251107a.h5',
                   cameraParams) 

videos.add_session('2025-11-07', 'optoTuningFreq',
                   'poni005_am_tuning_curve_20251107_01-02_VP9.mkv',
                   'poni005_am_tuning_curve_20251107b.h5',
                   cameraParams) 

videos.add_session('2025-11-12', 'optoTuningAMtone',
                   'poni005_am_tuning_curve_20251112_01-01_VP9.mkv',
                   'poni005_am_tuning_curve_20251112a.h5',
                   cameraParams) 

videos.add_session('2025-11-12', 'optoTuningFreq',
                   'poni005_am_tuning_curve_20251112_01-02_VP9.mkv',
                   'poni005_am_tuning_curve_20251112b.h5',
                   cameraParams) 


videos.add_session('2025-12-03', 'optoShamAMtone',
                   'poni005_am_tuning_curve_20251203_01_VP9.mkv',
                   'poni005_am_tuning_curve_20251203a.h5',
                   cameraParams) 

videos.add_session('2025-12-03', 'naturalSoundLoc',
                   'poni005_natural_sound_detection_20251203_01_VP9.mkv',
                   'poni005_natural_sound_detection_20251203a.h5',
                   cameraParams) 