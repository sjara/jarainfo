from jaratoolbox import videoinfo

subject = 'inpi001'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams


# 2023-02-21   
                   
videos.add_session('2023-02-21', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-21', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-21', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
                   'inpi001_oddball_sequence_20230221b', cameraParams)
                   
# 2023-02-22
                             
videos.add_session('2023-02-22', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-22', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-22', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
                   'inpi001_oddball_sequence_20230221b', cameraParams)                             
                   
# 2023-02-24
                             
videos.add_session('2023-02-24', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-24', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-24', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
                   'inpi001_oddball_sequence_20230221b', cameraParams)                             
