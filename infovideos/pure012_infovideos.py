'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'pure012'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2022-06-23', 'lowestfirst3chord',
                   'pure012_detectiongonogo_20220623a_lowestfirst3chord.mkv',
                   'pure012_detectiongonogo_20220623a.h5',
                   cameraParams) 
                   
videos.add_session('2022-06-24', 'lowestfirst6chord',
                   'pure012_detectiongonogo_20220624a_lowestfirst6chord.mkv',
                   'pure012_detectiongonogo_20220624a.h5',
                   cameraParams) 
                   
videos.add_session('2022-06-28', 'highestfirst6chord',
                   'pure012_detectiongonogo_20220628a_highestfirst6chord.mkv',
                   'pure012_detectiongonogo_20220628a.h5',
                   cameraParams) 
                   
videos.add_session('2022-07-01', 'random6chord',
                   'pure012_am_tuning_curve_20220701a_random6chord.mkv',
                   'pure012_am_tuning_curve_20220701a.h5',
                   cameraParams) 
