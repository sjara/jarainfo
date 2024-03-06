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

# 2024-02-28

videos.add_session('2024-02-28', 'pureTones',
                   'feat014_am_tuning_curve_20240228_01.mkv',
                   'feat014_am_tuning_curve_20240228a.h5', cameraParams) 
videos.add_session('2024-02-28', 'AM',
                   'feat014_am_tuning_curve_20240228_02.mkv',
                   'feat014_am_tuning_curve_20240228b.h5', cameraParams) 

# 2024-02-29

videos.add_session('2024-02-29', 'pureTones',
                   'feat014_am_tuning_curve_20240229_01.mkv',
                   'feat014_am_tuning_curve_2024029a.h5', cameraParams) 
videos.add_session('2024-02-29', 'AM',
                   'feat014_am_tuning_curve_20240229_02.mkv',
                   'feat014_am_tuning_curve_20240229b.h5', cameraParams) 

# 2024-03-04

videos.add_session('2024-03-04', 'pureTones',
                   'feat014_am_tuning_curve_20240304_01.mkv',
                   'feat014_am_tuning_curve_20240304a.h5', cameraParams) 
videos.add_session('2024-03-04', 'AM',
                   'feat014_am_tuning_curve_20240204_02.mkv',
                   'feat014_am_tuning_curve_20240304b.h5', cameraParams) 


# 2024-03-06

videos.add_session('2024-03-06', 'pureTones',
                   'feat014_am_tuning_curve_20240306_01.mkv',
                   'feat014_am_tuning_curve_20240306a.h5', cameraParams) 
videos.add_session('2024-03-06', 'AM',
                   'feat014_am_tuning_curve_20240306_02.mkv',
                   'feat014_am_tuning_curve_20240306b.h5', cameraParams) 

# 2024-03-

videos.add_session('2024-03-xx', 'pureTones',
                   'feat014_am_tuning_curve_202403xx_01.mkv',
                   'feat014_am_tuning_curve_202403xxa.h5', cameraParams) 
videos.add_session('2024-03-xx', 'AM',
                   'feat014_am_tuning_curve_202403xx_02.mkv',
                   'feat014_am_tuning_curve_202403xxb.h5', cameraParams) 
