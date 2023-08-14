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
                   

# EVERY SESSION AFTER HERE HAS A 1-2 SECOND MANUAL SYNC LIGHT BEFORE AND AFTER THE TRIALS.
# 2023-08-09

videos.add_session('2023-08-09', 'prePureTones',
                   'acid010_am_tuning_curve_20230809_01pre.mkv',
                   'acid010_am_tuning_curve_20230809apre.h5', cameraParams) 

videos.add_session('2023-08-09', 'preHighFreq',
                   'acid010_oddball_sequence_20230809_01pre.mkv',
                   'acid010_oddball_sequence_20230809apre', cameraParams) 

videos.add_session('2023-08-09', 'preLowFreq',
                   'acid010_oddball_sequence_20230809_02pre.mkv',
                   'acid010_oddball_sequence_20230809bpre', cameraParams)

videos.add_session('2023-08-09', 'preFM_Down',
                   'acid010_oddball_sequence_20230809_03pre.mkv',
                   'acid010_oddball_sequence_20230809cpre', cameraParams)
                   
videos.add_session('2023-08-09', 'preFM_Up',
                   'acid010_oddball_sequence_20230809_04pre.mkv',
                   'acid010_oddball_sequence_20230809dpre', cameraParams)
# Saline
videos.add_session('2023-08-09', 'salineInjection',
                   'acid010_20230809_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-08-09', 'salinePureTones',
                   'acid010_am_tuning_curve_20230809_01saline.mkv',
                   'acid010_am_tuning_curve_20230809asaline.h5', cameraParams) 

videos.add_session('2023-08-09', 'salineHighFreq',
                   'acid010_oddball_sequence_20230809_01saline.mkv',
                   'acid010_oddball_sequence_20230809asaline', cameraParams) 

videos.add_session('2023-08-09', 'salineLowFreq',
                   'acid010_oddball_sequence_20230809_02saline.mkv',
                   'acid010_oddball_sequence_20230809bsaline', cameraParams)

videos.add_session('2023-08-09', 'salineFM_Down',
                   'acid010_oddball_sequence_20230809_03saline.mkv',
                   'acid010_oddball_sequence_20230809csaline', cameraParams)
                   
videos.add_session('2023-08-09', 'salineFM_Up',
                   'acid010_oddball_sequence_20230809_04saline.mkv',
                   'acid010_oddball_sequence_20230809dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-08-09', 'doiInjection',
                   'acid010_20230809_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-08-09', 'doiPureTones',
                   'acid010_am_tuning_curve_20230809_01doi.mkv',
                   'acid010_am_tuning_curve_20230809adoi.h5', cameraParams) 

videos.add_session('2023-08-09', 'doiHighFreq',
                   'acid010_oddball_sequence_20230809_01doi.mkv',
                   'acid010_oddball_sequence_20230809adoi', cameraParams) 

videos.add_session('2023-08-09', 'doiLowFreq',
                   'acid010_oddball_sequence_20230809_02doi.mkv',
                   'acid010_oddball_sequence_20230809bdoi', cameraParams)

videos.add_session('2023-08-09', 'doiFM_Down',
                   'acid010_oddball_sequence_20230809_03doi.mkv',
                   'acid010_oddball_sequence_20230809cdoi', cameraParams)
                   
videos.add_session('2023-08-09', 'doiFM_Up',
                   'acid010_oddball_sequence_20230809_04doi.mkv',
                   'acid010_oddball_sequence_20230809ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-08-09', 'doiSpontaneous',
                   'acid010_20230809_doiSpontaneous.mkv','', cameraParams)
                   

# 2023-08-14

videos.add_session('2023-08-14', 'prePureTones',
                   'acid010_am_tuning_curve_20230814_01pre.mkv',
                   'acid010_am_tuning_curve_20230814apre.h5', cameraParams) 

videos.add_session('2023-08-14', 'preHighFreq',
                   'acid010_oddball_sequence_20230814_01pre.mkv',
                   'acid010_oddball_sequence_20230814apre', cameraParams) 

videos.add_session('2023-08-14', 'preLowFreq',
                   'acid010_oddball_sequence_20230814_02pre.mkv',
                   'acid010_oddball_sequence_20230814bpre', cameraParams)

videos.add_session('2023-08-14', 'preFM_Down',
                   'acid010_oddball_sequence_20230814_03pre.mkv',
                   'acid010_oddball_sequence_20230814cpre', cameraParams)
                   
videos.add_session('2023-08-14', 'preFM_Up',
                   'acid010_oddball_sequence_20230814_04pre.mkv',
                   'acid010_oddball_sequence_20230814dpre', cameraParams)
# Saline
videos.add_session('2023-08-14', 'salineInjection',
                   'acid010_20230814_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-08-14', 'salinePureTones',
                   'acid010_am_tuning_curve_20230814_01saline.mkv',
                   'acid010_am_tuning_curve_20230814asaline.h5', cameraParams) 

videos.add_session('2023-08-14', 'salineHighFreq',
                   'acid010_oddball_sequence_20230814_01saline.mkv',
                   'acid010_oddball_sequence_20230814asaline', cameraParams) 

videos.add_session('2023-08-14', 'salineLowFreq',
                   'acid010_oddball_sequence_20230814_02saline.mkv',
                   'acid010_oddball_sequence_20230814bsaline', cameraParams)

videos.add_session('2023-08-14', 'salineFM_Down',
                   'acid010_oddball_sequence_20230814_03saline.mkv',
                   'acid010_oddball_sequence_20230814csaline', cameraParams)
                   
videos.add_session('2023-08-14', 'salineFM_Up',
                   'acid010_oddball_sequence_20230814_04saline.mkv',
                   'acid010_oddball_sequence_20230814dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-08-14', 'doiInjection',
                   'acid010_20230814_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-08-14', 'doiPureTones',
                   'acid010_am_tuning_curve_20230814_01doi.mkv',
                   'acid010_am_tuning_curve_20230814adoi.h5', cameraParams) 

videos.add_session('2023-08-14', 'doiHighFreq',
                   'acid010_oddball_sequence_20230814_01doi.mkv',
                   'acid010_oddball_sequence_20230814adoi', cameraParams) 

videos.add_session('2023-08-14', 'doiLowFreq',
                   'acid010_oddball_sequence_20230814_02doi.mkv',
                   'acid010_oddball_sequence_20230814bdoi', cameraParams)

videos.add_session('2023-08-14', 'doiFM_Down',
                   'acid010_oddball_sequence_20230814_03doi.mkv',
                   'acid010_oddball_sequence_20230814cdoi', cameraParams)
                   
videos.add_session('2023-08-14', 'doiFM_Up',
                   'acid010_oddball_sequence_20230814_04doi.mkv',
                   'acid010_oddball_sequence_20230814ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-08-14', 'doiSpontaneous',                   'acid010_20230814_doiSpontaneous.mkv','', cameraParams)                                                                                                                                                             
