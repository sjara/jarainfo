from jaratoolbox import videoinfo

subject = 'feat015'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-02-23

videos.add_session('2024-02-23', 'pureTones',
                   'feat015_am_tuning_curve_20240223_01.mkv',
                   'feat015_am_tuning_curve_20240223a.h5', cameraParams) 
                   
videos.add_session('2024-02-23', 'AM',
                   'feat015_am_tuning_curve_20240223_02.mkv',
                   'feat015_am_tuning_curve_20240223b.h5', cameraParams)   
                   
#2024-02-27

videos.add_session('2024-02-27', 'pureTones',
                   'feat015_am_tuning_curve_20240227_01.mkv',
                   'feat015_am_tuning_curve_20240227a.h5', cameraParams) 
                   
videos.add_session('2024-02-27', 'AM',
                   'feat015_am_tuning_curve_20240227_02.mkv',
                   'feat015_am_tuning_curve_20240227b.h5', cameraParams) 
                   
 #2024-02-28

videos.add_session('2024-02-28', 'pureTones',
                   'feat015_am_tuning_curve_20240228_01.mkv',
                   'feat015_am_tuning_curve_20240228a.h5', cameraParams) 
                   
videos.add_session('2024-02-28', 'AM',
                   'feat015_am_tuning_curve_20240228_02.mkv',
                   'feat015_am_tuning_curve_20240228b.h5', cameraParams)  
                   
#2024-03-01

videos.add_session('2024-03-01', 'pureTones',
                   'feat015_am_tuning_curve_20240301_01.mkv',
                   'feat015_am_tuning_curve_20240301a.h5', cameraParams) 
                   
videos.add_session('2024-03-01', 'AM',
                   'feat015_am_tuning_curve_20240301_02.mkv',
                   'feat015_am_tuning_curve_20240301b.h5', cameraParams)  
                   
#2024-03-06

videos.add_session('2024-03-06', 'pureTones',
                   'feat015_am_tuning_curve_20240306_01.mkv',
                   'feat015_am_tuning_curve_20240306a.h5', cameraParams) 
                   
videos.add_session('2024-03-06', 'AM',
                   'feat015_am_tuning_curve_20240306_02.mkv',
                   'feat015_am_tuning_curve_20240306b.h5', cameraParams)  
                   
#2024-03-20

# Night mode flickered in and out. Covered one of the lights, 3 originally were uncovered and this appeared to fix the issue.
# Left speaker was not working - we switched out the cable from the right side to the left and this fixed the issue. NOTE: the behavior file will report that the sound was presented to the right side but it was presented LEFT.

videos.add_session('2024-03-20', 'pureTones',
                   'feat015_am_tuning_curve_20240320_01.mkv',
                   'feat015_am_tuning_curve_20240320a.h5', cameraParams) 
                   
videos.add_session('2024-03-20', 'AM',
                   'feat015_am_tuning_curve_20240320_02.mkv',
                   'feat015_am_tuning_curve_20240320b.h5', cameraParams)   
                   
videos.add_session('2024-03-20', 'naturalSounds',
                   'feat015_natural_sound_detection_20240320_01.mkv',
                   'feat015_natural_sound_detection_20240320a.h5', cameraParams) 
                   
#2024-03-21

# Night mode flickered in and out - pressing the sensor cover seemed to fix


videos.add_session('2024-03-21', 'pureTones',
                   'feat015_am_tuning_curve_20240321_01.mkv',
                   'feat015_am_tuning_curve_20240321a.h5', cameraParams) 
                   
videos.add_session('2024-03-21', 'AM',
                   'feat015_am_tuning_curve_20240321_02.mkv',
                   'feat015_am_tuning_curve_20240321b.h5', cameraParams)   
                   
videos.add_session('2024-03-21', 'naturalSounds',
                   'feat015_natural_sound_detection_20240321_01.mkv',
                   'feat015_natural_sound_detection_20240321a.h5', cameraParams)                                                           
