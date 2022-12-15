from jaratoolbox import videoinfo

subject = 'feat011'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# 2022-12-13

videos.add_session('2022-12-13', 'pureTones',
                   'acid001_am_tuning_curve_20221213_01.mkv',
                   'acid001_am_tuning_curve_20221213a.h5', cameraParams) 

videos.add_session('2022-12-13', 'highFreq',
                   'acid001_oddball_sequence_20221213_01.mkv',
                   'acid001_oddball_sequence_20221213a', cameraParams) 

videos.add_session('2022-12-13', 'lowFreq',
                   'acid001_oddball_sequence_20221213_02.mkv',
                   'acid001_oddball_sequence_20221213b', cameraParams)

videos.add_session('2022-12-13', 'FM_Down',
                   'acid001_oddball_sequence_20221213_03.mkv',
                   'acid001_oddball_sequence_20221213c', cameraParams)
                   
videos.add_session('2022-12-13', 'FM_Up',
                   'acid001_oddball_sequence_20221213_04.mkv',
                   'acid001_oddball_sequence_20221213d', cameraParams)

#Saline

videos.add_session('2022-12-13', 'pureTones',
                   'acid001_am_tuning_curve_20221213_02.mkv',
                   'acid001_am_tuning_curve_20221213b.h5', cameraParams) 

videos.add_session('2022-12-13', 'highFreq',
                   'acid001_oddball_sequence_20221213_05.mkv',
                   'acid001_oddball_sequence_20221213e', cameraParams) 

videos.add_session('2022-12-13', 'lowFreq',
                   'acid001_oddball_sequence_20221213_06.mkv',
                   'acid001_oddball_sequence_20221213f', cameraParams)

videos.add_session('2022-12-13', 'FM_Down',
                   'acid001_oddball_sequence_20221213_07.mkv',
                   'acid001_oddball_sequence_20221213g', cameraParams)
                   
videos.add_session('2022-12-13', 'FM_Up',
                   'acid001_oddball_sequence_20221213_08.mkv',
                   'acid001_oddball_sequence_20221213h', cameraParams)  
                     

# 2022-12-14

videos.add_session('2022-12-14', 'pureTones',
                   'acid001_am_tuning_curve_20221214_01pre.mkv',
                   'acid001_am_tuning_curve_20221214apre.h5', cameraParams) 

videos.add_session('2022-12-14', 'highFreq',
                   'acid001_oddball_sequence_20221214_01pre.mkv',
                   'acid001_oddball_sequence_20221214apre', cameraParams) 

videos.add_session('2022-12-14', 'lowFreq',
                   'acid001_oddball_sequence_20221214_02pre.mkv',
                   'acid001_oddball_sequence_20221214bpre', cameraParams)

videos.add_session('2022-12-14', 'FM_Down',
                   'acid001_oddball_sequence_20221214_03pre.mkv',
                   'acid001_oddball_sequence_20221214cpre', cameraParams)
                   
videos.add_session('2022-12-14', 'FM_Up',
                   'acid001_oddball_sequence_20221214_04pre.mkv',
                   'acid001_oddball_sequence_20221214dpre', cameraParams)

#Saline

videos.add_session('2022-12-14', 'pureTones',
                   'acid001_am_tuning_curve_20221214_01post.mkv',
                   'acid001_am_tuning_curve_20221214apost.h5', cameraParams) 

videos.add_session('2022-12-14', 'highFreq',
                   'acid001_oddball_sequence_20221214_01post.mkv',
                   'acid001_oddball_sequence_20221214apost', cameraParams) 

videos.add_session('2022-12-14', 'lowFreq',
                   'acid001_oddball_sequence_20221214_02post.mkv',
                   'acid001_oddball_sequence_20221214bpost', cameraParams)

videos.add_session('2022-12-14', 'FM_Down',
                   'acid001_oddball_sequence_20221214_03post.mkv',
                   'acid001_oddball_sequence_20221214cpost', cameraParams)
                   
videos.add_session('2022-12-14', 'FM_Up',
                   'acid001_oddball_sequence_20221214_04post.mkv',
                   'acid001_oddball_sequence_20221214dpost', cameraParams)                     