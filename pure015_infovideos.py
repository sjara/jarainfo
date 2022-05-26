'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'pure015'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']


videos.add_session('2022-05-17', 'twoChordsPreExtremes',
                   'pure015_20220517_twoChordsPreExtremes_204_xconfig1.mkv',
                   'pure015_detectiongonogo_20220517_twoChordsPreExtremes_204_xconfig1.h5',
                   cameraParams)

videos.add_session('2022-05-17', 'twoChordsPreExtremes',
                   'pure015_20220517_twoChordsPreExtremes_205_xconfig1.mkv',
                   'pure015_detectiongonogo_20220517_twoChordsPreExtremes_205_xconfig1.h5',
                   cameraParams)

videos.add_session('2022-05-18', 'twoChordsPreExtremes',
                   'pure015_20220518_twoChordsPreExtremes_206_xconfig1.mkv',
                   'pure015_detectiongonogo_20220518_twoChordsPreExtremes_206_xconfig1.h5',
                   cameraParams)

videos.add_session('2022-05-18', 'twoChordsPreExtremes',
                   'pure015_20220518_twoChordsPreExtremes_207_xconfig1.mkv',
                   'pure015_detectiongonogo_20220518_twoChordsPreExtremes_207_xconfig1.h5',
                   cameraParams)

videos.add_session('2022-05-18', 'twoChordsPreExtremes',
                   'pure015_20220518_twoChordsPreExtremes_208_xconfig1.mkv',
                   'pure015_detectiongonogo_20220518_twoChordsPreExtremes_208_xconfig1.h5',
                   cameraParams)

videos.add_session('2022-05-19', 'twoChordsPreExtremes',
                   'pure015_20220519_twoChordsPreExtremes_209_xconfig1.mkv',
                   'pure015_detectiongonogo_20220519_twoChordsPreExtremes_209_xconfig1.h5',
                   cameraParams)

videos.add_session('2022-05-25', 'twoChordsPreExtremes',
                   'pure015_20220525_twoChordsPreExtremes_210_xconfig1.mkv',
                   'pure015_detectiongonogo_20220525_twoChordsPreExtremes_210_xconfig1.h5',
                   cameraParams)                   

