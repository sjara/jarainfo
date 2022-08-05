'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'pure013'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2022-06-24', 'lowestfirst6chord',
                   'pure013_detectiongonogo_20220624a_lowestfirst6chord.mkv',
                   'pure013_detectiongonogo_20220624a.h5',
                   cameraParams)
                   
videos.add_session('2022-07-01', 'highestfirst6chord',
                   'pure013_detectiongonogo_20220701a_highestfirst6chord.mkv',
                   'pure013_detectiongonogo_20220701a.h5',
                   cameraParams)                   
