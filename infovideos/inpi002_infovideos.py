from jaratoolbox import videoinfo

subject = 'inpi002'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams


# 2023-02-21
                   
videos.add_session('2023-02-21', 'PureTones',
                   'inpi002_am_tuning_curve_20230221_01.mkv',
                   'inpi002_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-21', 'FM_Up',
                   'inpi002_oddball_sequence_20230221_01.mkv',
                   'inpi002_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-21', 'FM_Down',
                   'inpi002_oddball_sequence_20230221_02.mkv',
                   'inpi002_oddball_sequence_20230221b', cameraParams)

# 2023-02-23
                   
videos.add_session('2023-02-23', 'PureTones',
                   'inpi002_am_tuning_curve_20230221_01.mkv',
                   'inpi002_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-23', 'FM_Up',
                   'inpi002_oddball_sequence_20230221_01.mkv',
                   'inpi002_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-23', 'FM_Down',
                   'inpi002_oddball_sequence_20230221_02.mkv',
                   'inpi002_oddball_sequence_20230221b', cameraParams)
                                      
# 2023-02-27
                   
videos.add_session('2023-02-27', 'PureTones',
                   'inpi002_am_tuning_curve_20230221_01.mkv',
                   'inpi002_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-02-27', 'FM_Up',
                   'inpi002_oddball_sequence_20230221_01.mkv',
                   'inpi002_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-02-27', 'FM_Down',
                   'inpi002_oddball_sequence_20230221_02.mkv',
                   'inpi002_oddball_sequence_20230221b', cameraParams)
  
# 2023-03-02
                   
videos.add_session('2023-03-02', 'PureTones',
                   'inpi002_am_tuning_curve_20230221_01.mkv',
                   'inpi002_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-03-02', 'FM_Up',
                   'inpi002_oddball_sequence_20230221_01.mkv',
                   'inpi002_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-03-02', 'FM_Down',
                   'inpi002_oddball_sequence_20230221_02.mkv',
                   'inpi002_oddball_sequence_20230221b', cameraParams)     
                   
# 2023-03-07
                   
videos.add_session('2023-03-07', 'PureTones',
                   'inpi002_am_tuning_curve_20230221_01.mkv',
                   'inpi002_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-03-07', 'FM_Up',
                   'inpi002_oddball_sequence_20230221_01.mkv',
                   'inpi002_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-03-07', 'FM_Down',
                   'inpi002_oddball_sequence_20230221_02.mkv',
                   'inpi002_oddball_sequence_20230221b', cameraParams)        
                   
                   
# 2023-03-13
                   
videos.add_session('2023-03-13', 'PureTones',
                   'inpi002_am_tuning_curve_20230221_01.mkv',
                   'inpi002_am_tuning_curve_20230221a.h5', cameraParams)
                   
videos.add_session('2023-03-13', 'FM_Up',
                   'inpi002_oddball_sequence_20230221_01.mkv',
                   'inpi002_oddball_sequence_20230221a', cameraParams) 

videos.add_session('2023-03-13', 'FM_Down',
                   'inpi002_oddball_sequence_20230221_02.mkv',
                   'inpi002_oddball_sequence_20230221b', cameraParams)


# ----------------------
# Max's DOI Study
                  
# 2023-03-23
#Saline injection

videos.add_session('2023-03-23', 'prePureTones',
                   'inpi002_am_tuning_curve_20230323_01pre.mkv',
                   'inpi002_am_tuning_curve_20230323apre.h5', cameraParams) 

videos.add_session('2023-03-23', 'preHighFreq',
                   'inpi002_oddball_sequence_20230323_01pre.mkv',
                   'inpi002_oddball_sequence_20230323apre', cameraParams) 

videos.add_session('2023-03-23', 'preLowFreq',
                   'inpi002_oddball_sequence_20230323_02pre.mkv',
                   'inpi002_oddball_sequence_20230323bpre', cameraParams)

videos.add_session('2023-03-23', 'preFM_Down',
                   'inpi002_oddball_sequence_20230323_03pre.mkv',
                   'inpi002_oddball_sequence_20230323cpre', cameraParams)
                   
videos.add_session('2023-03-23', 'preFM_Up',
                   'inpi002_oddball_sequence_20230323_04pre.mkv',
                   'inpi002_oddball_sequence_20230323dpre', cameraParams)
# Saline

videos.add_session('2023-03-23', 'salinePureTones',
                   'inpi002_am_tuning_curve_20230323_01saline.mkv',
                   'inpi002_am_tuning_curve_20230323asaline.h5', cameraParams) 

videos.add_session('2023-03-23', 'salineHighFreq',
                   'inpi002_oddball_sequence_20230323_01saline.mkv',
                   'inpi002_oddball_sequence_20230323asaline', cameraParams) 

videos.add_session('2023-03-23', 'salineLowFreq',
                   'inpi002_oddball_sequence_20230323_02saline.mkv',
                   'inpi002_oddball_sequence_20230323bsaline', cameraParams)

videos.add_session('2023-03-23', 'salineFM_Down',
                   'inpi002_oddball_sequence_20230323_03saline.mkv',
                   'inpi002_oddball_sequence_20230323csaline', cameraParams)
                   
videos.add_session('2023-03-23', 'salineFM_Up',
                   'inpi002_oddball_sequence_20230323_04saline.mkv',
                   'inpi002_oddball_sequence_20230323dsaline', cameraParams)
                   

# 2023-03-24
#DOI injection

videos.add_session('2023-03-24', 'prePureTones',
                   'inpi002_am_tuning_curve_20230324_01pre.mkv',
                   'inpi002_am_tuning_curve_20230324apre.h5', cameraParams) 

videos.add_session('2023-03-24', 'preHighFreq',
                   'inpi002_oddball_sequence_20230324_01pre.mkv',
                   'inpi002_oddball_sequence_20230324apre', cameraParams) 

videos.add_session('2023-03-24', 'preLowFreq',
                   'inpi002_oddball_sequence_20230324_02pre.mkv',
                   'inpi002_oddball_sequence_20230324bpre', cameraParams)

videos.add_session('2023-03-24', 'preFM_Down',
                   'inpi002_oddball_sequence_20230324_03pre.mkv',
                   'inpi002_oddball_sequence_20230324cpre', cameraParams)
                   
videos.add_session('2023-03-24', 'preFM_Up',
                   'inpi002_oddball_sequence_20230324_04pre.mkv',
                   'inpi002_oddball_sequence_20230324dpre', cameraParams)                   

# DOI

videos.add_session('2023-03-24', 'doiPureTones',
                   'inpi002_am_tuning_curve_20230324_01doi.mkv',
                   'inpi002_am_tuning_curve_20230324adoi.h5', cameraParams) 

videos.add_session('2023-03-24', 'doiHighFreq',
                   'inpi002_oddball_sequence_20230324_01doi.mkv',
                   'inpi002_oddball_sequence_20230324adoi', cameraParams) 

videos.add_session('2023-03-24', 'doiLowFreq',
                   'inpi002_oddball_sequence_20230324_02doi.mkv',
                   'inpi002_oddball_sequence_20230324bdoi', cameraParams)

videos.add_session('2023-03-24', 'doiFM_Down',
                   'inpi002_oddball_sequence_20230324_03doi.mkv',
                   'inpi002_oddball_sequence_20230324cdoi', cameraParams)
                   
videos.add_session('2023-03-24', 'doiFM_Up',
                   'inpi002_oddball_sequence_20230324_04doi.mkv',
                   'inpi002_oddball_sequence_20230324ddoi', cameraParams)            
