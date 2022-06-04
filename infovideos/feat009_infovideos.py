from jaratoolbox import videoinfo

subject = 'feat009'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2022-03-23

videos.add_session('2022-06-04', 'AM',
                   'feat009_am_tuning_curve_20220604_01.mkv',
                   'feat009_am_tuning_curve_20220604a.h5', cameraParams) 


videos.add_session('2022-06-04', 'pureTones',
                   'feat009_am_tuning_curve_20220604_02.mkv',
                   'feat009_am_tuning_curve_20220604b.h5', cameraParams) 

videos.add_session('2022-06-04', 'FTVOTBorders',
                   'feat009_2afc_speech_20220604_01.mkv',
                   'feat009_2afc_speech_20220604a.h5', cameraParams) 

