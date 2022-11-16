from jaratoolbox import videoinfo

subject = 'feat011'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2022-11-16

videos.add_session('2022-11-16', 'AM',
                   'feat011_am_tuning_curve_20221116_01.mkv',
                   'feat011_am_tuning_curve_20221116a.h5', cameraParams) 


videos.add_session('2022-11-16', 'pureTones',
                   'feat011_am_tuning_curve_20221116_02.mkv',
                   'feat011_am_tuning_curve_20221116b.h5', cameraParams) 

videos.add_session('2022-11-16', 'FTVOTBorders',
                   'feat011_2afc_speech_20221116_01.mkv',
                   'feat011_2afc_speech_20221116a.h5', cameraParams) 

                   
