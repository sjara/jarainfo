'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'pure001'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2021-09-28', 'syncVisibleNoSound',
                   'pure001_20210928_syncVisibleNoSound_01.mkv',
                   'pure001_detectsound_20210928_syncVisibleNoSound_01.h5',
                   cameraParams) 
                   
videos.add_session('2021-09-28', 'syncNoSound',
                   'pure001_20210928_syncNoSound_01.mkv',
                   'pure001_detectsound_20210928_syncNoSound_01.h5',
                   cameraParams)

videos.add_session('2021-09-28', 'chord',
                   'pure001_20210928_chord_01.mkv',
                   'pure001_detectsound_20210928_chord_01.h5',
                   cameraParams)
                   

                                                                                          
