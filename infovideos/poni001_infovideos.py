'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'poni001'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2025-11-03', 'optoTuningAMtone',
                   'poni001_am_tuning_curve_20251103_01-03_VP9.mkv',
                   'poni001_am_tuning_curve_20251103a.h5',
                   cameraParams) 

videos.add_session('2025-11-03', 'optoTuningFreq',
                   'poni001_am_tuning_curve_20251103_01-05_VP9.mkv',
                   'poni001_am_tuning_curve_20251103b.h5',
                   cameraParams) 

videos.add_session('2025-11-07', 'optoTuningAMtone',
                   'poni001_am_tuning_curve_20251107_01-01_VP9.mkv',
                   'poni001_am_tuning_curve_20251107a.h5',
                   cameraParams)

videos.add_session('2025-11-07', 'optoTuningFreq',
                   'poni001_am_tuning_curve_20251107_01-02_VP9.mkv',
                   'poni001_am_tuning_curve_20251107b.h5',
                   cameraParams)

videos.add_session('2025-11-12', 'optoTuningAMtone',
                   'poni001_am_tuning_curve_20251112_01-01_VP9.mkv',
                   'poni001_am_tuning_curve_20251112a.h5',
                   cameraParams)

videos.add_session('2025-11-12', 'optoTuningFreq',
                   'poni001_am_tuning_curve_20251112_01-02_VP9.mkv',
                   'poni001_am_tuning_curve_20251112b.h5',
                   cameraParams)

videos.add_session('2025-12-03', 'optoShamAMtone',
                   'poni001_am_tuning_curve_20251203_01-01_VP9.mkv',
                   'poni001_am_tuning_curve_20251203a.h5',
                   cameraParams)

videos.add_session('2025-12-16', 'naturalSoundLoc',
                   'poni001_natural_sound_detection_20251216_01-01_VP9.mkv',
                   'poni001_natural_sound_detection_20251216a.h5',
                   cameraParams)


