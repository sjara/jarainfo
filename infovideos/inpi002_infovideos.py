from jaratoolbox import videoinfo

subject = 'inpi002'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams


# 2023-02-21
                   
videos.add_session('2023-02-21', 'PureTones',
                   'inpi002_am_tuning_curve_20230221_01.mkv',
                   'inpi002_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-21', 'FM_Up',
                   'inpi002_oddball_sequence_20230221_01.mkv',
                   'inpi002_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-21', 'FM_Down',
                   'inpi002_oddball_sequence_20230221_02.mkv',
                   'inpi002_oddball_sequence_20230221b', cameraParams)

# 2023-02-23
                   
videos.add_session('2023-02-23', 'PureTones',
                   'inpi002_am_tuning_curve_20230221_01.mkv',
                   'inpi002_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-23', 'FM_Up',
                   'inpi002_oddball_sequence_20230221_01.mkv',
                   'inpi002_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-23', 'FM_Down',
                   'inpi002_oddball_sequence_20230221_02.mkv',
                   'inpi002_oddball_sequence_20230221b', cameraParams)
                                      

                             
