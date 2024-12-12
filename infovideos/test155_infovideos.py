from jaratoolbox import videoinfo

subject = 'test155'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2024-12-05

videos.add_session('2024-12-05', "AM",
                   'test155_am_tuning_curve_20241205_01',
                   'test155_am_tuning_curve_20241205a.h5', cameraParams) 
               
videos.add_session('2024-12-05', "AM",
                   'test155_am_tuning_curve_20241205_02',
                   'test155_am_tuning_curve_20241205b.h5', cameraParams) 
                   
