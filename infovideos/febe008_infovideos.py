from jaratoolbox import videoinfo

subject = 'febe008'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_1280x1024_30fps_VP9'] #CHECK THIS!

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2022-07-20

videos.add_session('2022-07-20', 'behaviorVOT',
                   'febe008_headfixed_speech_20220720_01.mkv',
                   'febe008_headfixed_speech_20220720a.h5', cameraParams) 
                         
videos.add_session('2022-07-20', 'AM',
                   'febe008_am_tuning_20220720_01.mkv',
                   'febe008_am_tuning_20220720a.h5', cameraParams) 

videos.add_session('2022-07-20', 'pureTones',
                   'febe008_am_tuning_20220720_02.mkv',
                   'febe008_am_tuning_20220720b.h5', cameraParams) 


