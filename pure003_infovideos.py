'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'pure003'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2021-09-28', 'syncVisibleNoSound',
                   'pure003_20210928_syncVisibleNoSound_01.mkv',
                   'pure003_detectsound_20210928_syncVisibleNoSound_01.h5',
                   cameraParams) 
                   
videos.add_session('2021-09-28', 'syncNoSound',
                   'pure003_20210928_syncNoSound_01.mkv',
                   'pure003_detectsound_20210928_syncNoSound_01.h5',
                   cameraParams)

videos.add_session('2021-09-28', 'chord',
                   'pure003_20210928_chord_01.mkv',
                   'pure003_detectsound_20210928_chord_01.h5',
                   cameraParams)
