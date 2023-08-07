from jaratoolbox import videoinfo

subject = 'acid009'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# ----------------------

# 2023-08-04

videos.add_session('2023-08-04', 'prePureTones',
                   'acid009_am_tuning_curve_20230804_01pre.mkv',
                   'acid009_am_tuning_curve_20230804apre.h5', cameraParams) 

videos.add_session('2023-08-04', 'preHighFreq',
                   'acid009_oddball_sequence_20230804_01pre.mkv',
                   'acid009_oddball_sequence_20230804apre', cameraParams) 

videos.add_session('2023-08-04', 'preLowFreq',
                   'acid009_oddball_sequence_20230804_02pre.mkv',
                   'acid009_oddball_sequence_20230804bpre', cameraParams)

videos.add_session('2023-08-04', 'preFM_Down',
                   'acid009_oddball_sequence_20230804_03pre.mkv',
                   'acid009_oddball_sequence_20230804cpre', cameraParams)
                   
videos.add_session('2023-08-04', 'preFM_Up',
                   'acid009_oddball_sequence_20230804_04pre.mkv',
                   'acid009_oddball_sequence_20230804dpre', cameraParams)
# Saline
videos.add_session('2023-08-04', 'salineInjection',
                   'acid009_20230804_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-08-04', 'salinePureTones',
                   'acid009_am_tuning_curve_20230804_01saline.mkv',
                   'acid009_am_tuning_curve_20230804asaline.h5', cameraParams) 

videos.add_session('2023-08-04', 'salineHighFreq',
                   'acid009_oddball_sequence_20230804_01saline.mkv',
                   'acid009_oddball_sequence_20230804asaline', cameraParams) 

videos.add_session('2023-08-04', 'salineLowFreq',
                   'acid009_oddball_sequence_20230804_02saline.mkv',
                   'acid009_oddball_sequence_20230804bsaline', cameraParams)

videos.add_session('2023-08-04', 'salineFM_Down',
                   'acid009_oddball_sequence_20230804_03saline.mkv',
                   'acid009_oddball_sequence_20230804csaline', cameraParams)
                   
videos.add_session('2023-08-04', 'salineFM_Up',
                   'acid009_oddball_sequence_20230804_04saline.mkv',
                   'acid009_oddball_sequence_20230804dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-08-04', 'doiInjection',
                   'acid009_20230804_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-08-04', 'doiPureTones',
                   'acid009_am_tuning_curve_20230804_01doi.mkv',
                   'acid009_am_tuning_curve_20230804adoi.h5', cameraParams) 

videos.add_session('2023-08-04', 'doiHighFreq',
                   'acid009_oddball_sequence_20230804_01doi.mkv',
                   'acid009_oddball_sequence_20230804adoi', cameraParams) 

videos.add_session('2023-08-04', 'doiLowFreq',
                   'acid009_oddball_sequence_20230804_02doi.mkv',
                   'acid009_oddball_sequence_20230804bdoi', cameraParams)

videos.add_session('2023-08-04', 'doiFM_Down',
                   'acid009_oddball_sequence_20230804_03doi.mkv',
                   'acid009_oddball_sequence_20230804cdoi', cameraParams)
                   
videos.add_session('2023-08-04', 'doiFM_Up',
                   'acid009_oddball_sequence_20230804_04doi.mkv',
                   'acid009_oddball_sequence_20230804ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-08-04', 'doiSpontaneous',
                   'acid009_20230804_doiSpontaneous.mkv','', cameraParams)
                   
                                                                                       
