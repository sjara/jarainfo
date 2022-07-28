from jaratoolbox import videoinfo

subject = 'febe008'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9'] #CHECK THIS!

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


# 2022-07-21

videos.add_session('2022-07-21', 'AM',
                   'febe008_am_tuning_20220721_01.mkv',
                   'febe008_am_tuning_20220721a.h5', cameraParams) 

videos.add_session('2022-07-21', 'pureTones',
                   'febe008_am_tuning_20220721_02.mkv',
                   'febe008_am_tuning_20220721b.h5', cameraParams)
                   
videos.add_session('2022-07-21', 'behaviorVOT',
                   'febe008_headfixed_speech_20220721_01.mkv',
                   'febe008_headfixed_speech_20220721a.h5', cameraParams) 

# 2022-07-22

videos.add_session('2022-07-22', 'behaviorVOT',
                   'febe008_headfixed_speech_20220722_01.mkv',
                   'febe008_headfixed_speech_20220722a.h5', cameraParams) #sync light not visible until trial 34
                         
videos.add_session('2022-07-22', 'AM',
                   'febe008_am_tuning_20220722_01.mkv',
                   'febe008_am_tuning_20220722a.h5', cameraParams) 

videos.add_session('2022-07-22', 'pureTones',
                   'febe008_am_tuning_20220722_02.mkv',
                   'febe008_am_tuning_20220722b.h5', cameraParams)


# 2022-07-26

videos.add_session('2022-07-26', 'behaviorVOT',
                   'febe008_headfixed_speech_20220726_01.mkv',
                   'febe008_headfixed_speech_20220726a.h5', cameraParams)
                         
videos.add_session('2022-07-26', 'AM',
                   'febe008_am_tuning_20220726_01.mkv',
                   'febe008_am_tuning_20220726a.h5', cameraParams) 

videos.add_session('2022-07-26', 'pureTones',
                   'febe008_am_tuning_20220726_02.mkv',
                   'febe008_am_tuning_20220726b.h5', cameraParams)


# 2022-07-27

videos.add_session('2022-07-27', 'behaviorVOT',
                   'febe008_headfixed_speech_20220727_01.mkv',
                   'febe008_headfixed_speech_20220727a.h5', cameraParams)
                         
videos.add_session('2022-07-27', 'AM',
                   'febe008_am_tuning_20220727_01.mkv',
                   'febe008_am_tuning_20220727a.h5', cameraParams) 

videos.add_session('2022-07-27', 'pureTones',
                   'febe008_am_tuning_20220727_02.mkv',
                   'febe008_am_tuning_20220727b.h5', cameraParams)

# 2022-07-28

videos.add_session('2022-07-28', 'behaviorVOT',
                   'febe008_headfixed_speech_20220728_01.mkv',
                   'febe008_headfixed_speech_20220728a.h5', cameraParams)
                         
videos.add_session('2022-07-28', 'AM',
                   'febe008_am_tuning_20220728_01.mkv',
                   'febe008_am_tuning_20220728a.h5', cameraParams) 

videos.add_session('2022-07-28', 'pureTones',
                   'febe008_am_tuning_20220728_02.mkv',
                   'febe008_am_tuning_20220728b.h5', cameraParams)


