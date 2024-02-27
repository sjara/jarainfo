from jaratoolbox import videoinfo

subject = 'feat014'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-02-22

videos.add_session('2024-02-22', 'pureTones',
                   'feat014_am_tuning_curve_20240222_01.mkv',
                   'feat014_am_tuning_curve_20240222a.h5', cameraParams) 

videos.add_session('2024-02-22', 'AM',
                   'feat014_am_tuning_curve_20240222_02.mkv',
                   'feat014_am_tuning_curve_20240222b.h5', cameraParams) 

# 2024-02-

videos.add_session('2024-02-xx', 'pureTones',
                   'feat014_am_tuning_curve_202402xx_01.mkv',
                   'feat014_am_tuning_curve_202402xxa.h5', cameraParams) 
videos.add_session('2024-02-26', 'AM',
                   'feat014_am_tuning_curve_202402xx_02.mkv',
                   'feat014_am_tuning_curve_202402xxb.h5', cameraParams) 

# 2024-02-

videos.add_session('2024-02-xx', 'pureTones',
                   'feat014_am_tuning_curve_202402xx_01.mkv',
                   'feat014_am_tuning_curve_20240xxa.h5', cameraParams) 
videos.add_session('2024-02-xx', 'AM',
                   'feat014_am_tuning_curve_202402xx_02.mkv',
                   'feat014_am_tuning_curve_202402xxb.h5', cameraParams) 


