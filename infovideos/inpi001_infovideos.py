from jaratoolbox import videoinfo

subject = 'inpi001'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams


# 2023-02-21   
                   
videos.add_session('2023-02-21', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-21', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-21', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
                   'inpi001_oddball_sequence_20230221b', cameraParams)
                   
# 2023-02-22
                             
videos.add_session('2023-02-22', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-22', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-22', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
                   'inpi001_oddball_sequence_20230221b', cameraParams)                             
                   
# 2023-02-24
                             
videos.add_session('2023-02-24', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-24', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-24', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
<<<<<<< HEAD
                   'inpi001_oddball_sequence_20230221b', cameraParams)   
                   
# 2023-02-28
                             
videos.add_session('2023-02-28', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-28', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-28', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
                   'inpi001_oddball_sequence_20230221b', cameraParams)         
                   
# 2023-03-07
                             
videos.add_session('2023-03-07', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-03-07', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-03-07', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
                   'inpi001_oddball_sequence_20230221b', cameraParams)    
                   
# 2023-03-13
                             
videos.add_session('2023-03-13', 'PureTones',
                   'inpi001_am_tuning_curve_20230221_01.mkv',
                   'inpi001_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-03-13', 'FM_Up',
                   'inpi001_oddball_sequence_20230221_01.mkv',
                   'inpi001_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-03-13', 'FM_Down',
                   'inpi001_oddball_sequence_20230221_02.mkv',
                   'inpi001_oddball_sequence_20230221b', cameraParams)                                               
=======
                   'inpi001_oddball_sequence_20230221b', cameraParams)
                   

#------------
# Max's DOI Study                  
# 2023-03-22
# DOI & Saline

videos.add_session('2023-03-22', 'prePureTones',
                   'inpi001_am_tuning_curve_20230322_01pre.mkv',
                   'inpi001_am_tuning_curve_20230322apre.h5', cameraParams) 

videos.add_session('2023-03-22', 'preHighFreq',
                   'inpi001_oddball_sequence_20230322_01pre.mkv',
                   'inpi001_oddball_sequence_20230322apre', cameraParams) 

videos.add_session('2023-03-22', 'preLowFreq',
                   'inpi001_oddball_sequence_20230322_02pre.mkv',
                   'inpi001_oddball_sequence_20230322bpre', cameraParams)

videos.add_session('2023-03-22', 'preFM_Down',
                   'inpi001_oddball_sequence_20230322_03pre.mkv',
                   'inpi001_oddball_sequence_20230322cpre', cameraParams)
                   
videos.add_session('2023-03-22', 'preFM_Up',
                   'inpi001_oddball_sequence_20230322_04pre.mkv',
                   'inpi001_oddball_sequence_20230322dpre', cameraParams)
# Saline

videos.add_session('2023-03-22', 'salinePureTones',
                   'inpi001_am_tuning_curve_20230322_01saline.mkv',
                   'inpi001_am_tuning_curve_20230322asaline.h5', cameraParams) 

videos.add_session('2023-03-22', 'salineHighFreq',
                   'inpi001_oddball_sequence_20230322_01saline.mkv',
                   'inpi001_oddball_sequence_20230322asaline', cameraParams) 

videos.add_session('2023-03-22', 'salineLowFreq',
                   'inpi001_oddball_sequence_20230322_02saline.mkv',
                   'inpi001_oddball_sequence_20230322bsaline', cameraParams)

videos.add_session('2023-03-22', 'salineFM_Down',
                   'inpi001_oddball_sequence_20230322_03saline.mkv',
                   'inpi001_oddball_sequence_20230322csaline', cameraParams)
                   
videos.add_session('2023-03-22', 'salineFM_Up',
                   'inpi001_oddball_sequence_20230322_04saline.mkv',
                   'inpi001_oddball_sequence_20230322dsaline', cameraParams)
                   
# DOI

videos.add_session('2023-03-22', 'doiPureTones',
                   'inpi001_am_tuning_curve_20230322_01doi.mkv',
                   'inpi001_am_tuning_curve_20230322adoi.h5', cameraParams) 

videos.add_session('2023-03-22', 'doiHighFreq',
                   'inpi001_oddball_sequence_20230322_01doi.mkv',
                   'inpi001_oddball_sequence_20230322adoi', cameraParams) 

videos.add_session('2023-03-22', 'doiLowFreq',
                   'inpi001_oddball_sequence_20230322_02doi.mkv',
                   'inpi001_oddball_sequence_20230322bdoi', cameraParams)

videos.add_session('2023-03-22', 'doiFM_Down',
                   'inpi001_oddball_sequence_20230322_03doi.mkv',
                   'inpi001_oddball_sequence_20230322cdoi', cameraParams)
                   
videos.add_session('2023-03-22', 'doiFM_Up',
                   'inpi001_oddball_sequence_20230322_04doi.mkv',
                   'inpi001_oddball_sequence_20230322ddoi', cameraParams)                   
                   
                                                
>>>>>>> 267481925f58abea05bb798da81cba4fdd4356ac
