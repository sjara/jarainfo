from jaratoolbox import videoinfo

subject = 'acid010'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# ----------------------

# 2023-08-07

videos.add_session('2023-08-07', 'prePureTones',
                   'acid010_am_tuning_curve_20230807_01pre.mkv',
                   'acid010_am_tuning_curve_20230807apre.h5', cameraParams) 

videos.add_session('2023-08-07', 'preHighFreq',
                   'acid010_oddball_sequence_20230807_01pre.mkv',
                   'acid010_oddball_sequence_20230807apre', cameraParams) 

videos.add_session('2023-08-07', 'preLowFreq',
                   'acid010_oddball_sequence_20230807_02pre.mkv',
                   'acid010_oddball_sequence_20230807bpre', cameraParams)

videos.add_session('2023-08-07', 'preFM_Down',
                   'acid010_oddball_sequence_20230807_03pre.mkv',
                   'acid010_oddball_sequence_20230807cpre', cameraParams)
                   
videos.add_session('2023-08-07', 'preFM_Up',
                   'acid010_oddball_sequence_20230807_04pre.mkv',
                   'acid010_oddball_sequence_20230807dpre', cameraParams)
# Saline
videos.add_session('2023-08-07', 'salineInjection',
                   'acid010_20230807_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-08-07', 'salinePureTones',
                   'acid010_am_tuning_curve_20230807_01saline.mkv',
                   'acid010_am_tuning_curve_20230807asaline.h5', cameraParams) 

videos.add_session('2023-08-07', 'salineHighFreq',
                   'acid010_oddball_sequence_20230807_01saline.mkv',
                   'acid010_oddball_sequence_20230807asaline', cameraParams) 

videos.add_session('2023-08-07', 'salineLowFreq',
                   'acid010_oddball_sequence_20230807_02saline.mkv',
                   'acid010_oddball_sequence_20230807bsaline', cameraParams)

videos.add_session('2023-08-07', 'salineFM_Down',
                   'acid010_oddball_sequence_20230807_03saline.mkv',
                   'acid010_oddball_sequence_20230807csaline', cameraParams)
                   
videos.add_session('2023-08-07', 'salineFM_Up',
                   'acid010_oddball_sequence_20230807_04saline.mkv',
                   'acid010_oddball_sequence_20230807dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-08-07', 'doiInjection',
                   'acid010_20230807_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-08-07', 'doiPureTones',
                   'acid010_am_tuning_curve_20230807_01doi.mkv',
                   'acid010_am_tuning_curve_20230807adoi.h5', cameraParams) 

videos.add_session('2023-08-07', 'doiHighFreq',
                   'acid010_oddball_sequence_20230807_01doi.mkv',
                   'acid010_oddball_sequence_20230807adoi', cameraParams) 

videos.add_session('2023-08-07', 'doiLowFreq',
                   'acid010_oddball_sequence_20230807_02doi.mkv',
                   'acid010_oddball_sequence_20230807bdoi', cameraParams)

videos.add_session('2023-08-07', 'doiFM_Down',
                   'acid010_oddball_sequence_20230807_03doi.mkv',
                   'acid010_oddball_sequence_20230807cdoi', cameraParams)
                   
videos.add_session('2023-08-07', 'doiFM_Up',
                   'acid010_oddball_sequence_20230807_04doi.mkv',
                   'acid010_oddball_sequence_20230807ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-08-07', 'doiSpontaneous',
                   'acid010_20230807_doiSpontaneous.mkv','', cameraParams)
                   
                                                                                       
