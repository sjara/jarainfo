from jaratoolbox import videoinfo

subject = 'feat019'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-06-12

videos.add_session('2024-06-12', 'pureTones',
                   'feat019_am_tuning_curve_20240612_01.mkv',
                   'feat019_am_tuning_curve_20240612a.h5', cameraParams) 
videos.add_session('2024-06-12', 'naturalSound',
                   'feat019_natural_sound_detection_20240612_01.mkv',
                   'feat019_natural_sound_detection_20240612a.h5', cameraParams) 
videos.add_session('2024-06-12', 'AM',
                   'feat019_am_tuning_curve_20240612_02.mkv',
                   'feat019_am_tuning_curve_20240612b.h5', cameraParams) 


# 2024-06-13

videos.add_session('2024-06-13', 'pureTones',
                   'feat019_am_tuning_curve_20240613_01.mkv',
                   'feat019_am_tuning_curve_20240613a.h5', cameraParams) 
videos.add_session('2024-06-13', 'naturalSound',
                   'feat019_natural_sound_detection_20240613_01.mkv',
                   'feat019_natural_sound_detection_20240613a.h5', cameraParams) 
videos.add_session('2024-06-13', 'AM',
                   'feat019_am_tuning_curve_20240613_02.mkv',
                   'feat019_am_tuning_curve_20240613b.h5', cameraParams) 

# 2024-06-14

videos.add_session('2024-06-14', 'pureTones',
                   'feat019_am_tuning_curve_20240614_01.mkv',
                   'feat019_am_tuning_curve_20240614a.h5', cameraParams) 
videos.add_session('2024-06-14', 'naturalSound',
                   'feat019_natural_sound_detection_20240614_01.mkv',
                   'feat019_natural_sound_detection_20240614a.h5', cameraParams) 
videos.add_session('2024-06-14', 'AM',
                   'feat019_am_tuning_curve_20240614_02.mkv',
                   'feat019_am_tuning_curve_20240614b.h5', cameraParams) 


# 2024-06-17

videos.add_session('2024-06-17', 'pureTones',
                   'feat019_am_tuning_curve_20240617_01.mkv',
                   'feat019_am_tuning_curve_20240617a.h5', cameraParams) 
videos.add_session('2024-06-17', 'naturalSound',
                   'feat019_natural_sound_detection_20240617_01.mkv',
                   'feat019_natural_sound_detection_20240617a.h5', cameraParams) 
videos.add_session('2024-06-17', 'AM',
                   'feat019_am_tuning_curve_20240617_02.mkv',
                   'feat019_am_tuning_curve_20240617b.h5', cameraParams) 
                   
                   
# 2024-06-xx

#videos.add_session('2024-06-xx', 'pureTones',
#                   'feat019_am_tuning_curve_202406xx_01.mkv',
#                   'feat019_am_tuning_curve_202406xxa.h5', cameraParams) 
#videos.add_session('2024-06-xx', 'naturalSound',
#                   'feat019_natural_sound_detection_202406xx_01.mkv',
#                   'feat019_natural_sound_detection_202406xxa.h5', cameraParams) 
#videos.add_session('2024-06-xx', 'AM',
#                   'feat019_am_tuning_curve_202406xx_02.mkv',
#                   'feat019_am_tuning_curve_202406xxb.h5', cameraParams) 



