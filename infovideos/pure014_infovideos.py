'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'pure014'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']


videos.add_session('2022-07-25', 'detectSound',
                   'pure014_detectsound_20220725_01.mkv',
                   'pure014_detectsound_20220725a.h5',
                   cameraParams) 

videos.add_session('2022-07-26', 'detectSound',
                   'pure014_detectsound_20220726_01.mkv',
                   'pure014_detectsound_20220726a.h5',
                   cameraParams) 

videos.add_session('2022-07-27', 'detectSound',
                   'pure014_detectsound_20220727_01.mkv',
                   'pure014_detectsound_20220727a.h5',
                   cameraParams) 


