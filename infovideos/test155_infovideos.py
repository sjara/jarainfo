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
#fgbedsjgfb
videos.add_session('2024-12-20', "AM",
                   'test155_am_tuning_curve_20241220_03',
                   'test155_am_tuning_curve_20241205a.h5', cameraParams)
#This session 239 trials were recorded. And 3 videos were recorded. First video had 239 trials. Second video was 2 trails that is 2 secs, and third video 1 second by mistake. Then, I recorded 1 session from scratch. 220 trails taht is the next recording. 
videos.add_session('2024-12-20', "AM",
                   'test155_am_tuning_curve_20241220_06',
                   'test155_am_tuning_curve_20241220b.h5', cameraParams)   
#Today I recorded 6 sessions, four of which was nice. In one of the sessions i forgot to save the sound data, and in one the count increased to 224 trails, so had to take fresh recordings, but have the video data for all of them.           
videos.add_session('2024-12-26', "AM",
                   'test155_am_tuning_curve_20241226_07',
                   'test155_am_tuning_curve_20241226a.h5', cameraParams)
#Video is present but sound data file is not,as i did not save it, so naming it waste videos.add_session('2024-12-26', "AM",
#                   'test155_am_tuning_curve_20241226_08',
 #                  'test155_am_tuning_curve_20241226-waste.h5', cameraParams)
#Then recorded 224 trials, so naming it invalid
videos.add_session('2024-12-26', "AM",
                   'test155_am_tuning_curve_20241226_09',
                   'test155_am_tuning_curve_20241226x.h5', cameraParams)
videos.add_session('2024-12-26', "AM",
                   'test155_am_tuning_curve_20241226_10',
                   'test155_am_tuning_curve_20241226b.h5', cameraParams)
videos.add_session('2024-12-26', "AM",
                   'test155_am_tuning_curve_20241226_11',
                   'test155_am_tuning_curve_20241226c.h5', cameraParams)
videos.add_session('2024-12-26', "AM",
                   'test155_am_tuning_curve_20241226_12',
                   'test155_am_tuning_curve_20241226d.h5', cameraParams)
# Summary- On 26th Dec, I took 6 sessions recording from 4500um. The first recording was good. Second recording was video recorded and ephy too, but I did not save the sound data. The third recording, all was saved but for 224 triails. Fourth, fifth and sixth recordings were good.
