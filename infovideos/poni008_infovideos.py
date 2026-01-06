'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'poni008'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2025-11-17', 'optoTuningAMtone',
                   'poni008_am_tuning_curve_20251117_01-1_VP9.mkv',
                   'poni008_am_tuning_curve_20251117a.h5',
                   cameraParams) 

videos.add_session('2025-11-17', 'optoTuningFreq',
                   'poni008_am_tuning_curve_20251117_01-2_VP9.mkv',
                   'poni008_am_tuning_curve_20251117b.h5',
                   cameraParams) 

videos.add_session('2025-11-19', 'optoTuningAMtone',
                   'poni008_am_tuning_curve_20251119_01-1_VP9.mkv',
                   'poni008_am_tuning_curve_20251119a.h5',
                   cameraParams) 

videos.add_session('2025-11-19', 'optoTuningFreq',
                   'poni008_am_tuning_curve_20251119_01-2_VP9.mkv',
                   'poni008_am_tuning_curve_20251119b.h5',
                   cameraParams) 

videos.add_session('2025-11-21', 'optoTuningAMtone',
                   'poni008_am_tuning_curve_20251121_01-1_VP9.mkv',
                   'poni008_am_tuning_curve_20251121a.h5',
                   cameraParams) 

videos.add_session('2025-11-21', 'optoTuningFreq',
                   'poni008_am_tuning_curve_20251121_01-2_VP9.mkv',
                   'poni008_am_tuning_curve_20251121b.h5',
                   cameraParams) 

videos.add_session('2025-12-02', 'optoTuningAMtone',
                   'poni008_am_tuning_curve_20251202_01-1_VP9.mkv',
                   'poni008_am_tuning_curve_20251202a.h5',
                   cameraParams) 

videos.add_session('2025-12-02', 'optoTuningFreq',
                   'poni008_am_tuning_curve_20251202_01-2_VP9.mkv',
                   'poni008_am_tuning_curve_20251202b.h5',
                   cameraParams) 

videos.add_session('2025-12-05', 'optoShamAMtone',
                   'poni008_am_tuning_curve_20251205_01-1_VP9.mkv',
                   'poni008_am_tuning_curve_20251205a.h5',
                   cameraParams) 

videos.add_session('2025-12-05', 'naturalSoundLoc',
                   'poni008_natural_sound_detection_20251205_01-1_VP9.mkv',
                   'poni008_natural_sound_detection_20251205a.h5',
                   cameraParams) 


