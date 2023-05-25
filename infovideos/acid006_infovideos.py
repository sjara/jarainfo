from jaratoolbox import videoinfo

subject = 'acid006'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams
               
# 2023-03-22
# DOI & Saline

videos.add_session('2023-03-22', 'prePureTones',
                   'acid006_am_tuning_curve_20230322_01pre.mkv',
                   'acid006_am_tuning_curve_20230322apre.h5', cameraParams) 

videos.add_session('2023-03-22', 'preHighFreq',
                   'acid006_oddball_sequence_20230322_01pre.mkv',
                   'acid006_oddball_sequence_20230322apre', cameraParams) 

videos.add_session('2023-03-22', 'preLowFreq',
                   'acid006_oddball_sequence_20230322_02pre.mkv',
                   'acid006_oddball_sequence_20230322bpre', cameraParams)

videos.add_session('2023-03-22', 'preFM_Down',
                   'acid006_oddball_sequence_20230322_03pre.mkv',
                   'acid006_oddball_sequence_20230322cpre', cameraParams)
                   
videos.add_session('2023-03-22', 'preFM_Up',
                   'acid006_oddball_sequence_20230322_04pre.mkv',
                   'acid006_oddball_sequence_20230322dpre', cameraParams)
# Saline

videos.add_session('2023-03-22', 'salinePureTones',
                   'acid006_am_tuning_curve_20230322_01saline.mkv',
                   'acid006_am_tuning_curve_20230322asaline.h5', cameraParams) 

videos.add_session('2023-03-22', 'salineHighFreq',
                   'acid006_oddball_sequence_20230322_01saline.mkv',
                   'acid006_oddball_sequence_20230322asaline', cameraParams) 

videos.add_session('2023-03-22', 'salineLowFreq',
                   'acid006_oddball_sequence_20230322_02saline.mkv',
                   'acid006_oddball_sequence_20230322bsaline', cameraParams)

videos.add_session('2023-03-22', 'salineFM_Down',
                   'acid006_oddball_sequence_20230322_03saline.mkv',
                   'acid006_oddball_sequence_20230322csaline', cameraParams)
                   
videos.add_session('2023-03-22', 'salineFM_Up',
                   'acid006_oddball_sequence_20230322_04saline.mkv',
                   'acid006_oddball_sequence_20230322dsaline', cameraParams)
                   
# DOI

videos.add_session('2023-03-22', 'doiPureTones',
                   'acid006_am_tuning_curve_20230322_01doi.mkv',
                   'acid006_am_tuning_curve_20230322adoi.h5', cameraParams) 

videos.add_session('2023-03-22', 'doiHighFreq',
                   'acid006_oddball_sequence_20230322_01doi.mkv',
                   'acid006_oddball_sequence_20230322adoi', cameraParams) 

videos.add_session('2023-03-22', 'doiLowFreq',
                   'acid006_oddball_sequence_20230322_02doi.mkv',
                   'acid006_oddball_sequence_20230322bdoi', cameraParams)

videos.add_session('2023-03-22', 'doiFM_Down',
                   'acid006_oddball_sequence_20230322_03doi.mkv',
                   'acid006_oddball_sequence_20230322cdoi', cameraParams)
                   
videos.add_session('2023-03-22', 'doiFM_Up',
                   'acid006_oddball_sequence_20230322_04doi.mkv',
                   'acid006_oddball_sequence_20230322ddoi', cameraParams)                   
                   


# 2023-05-11
# DOI & Saline

videos.add_session('2023-05-11', 'prePureTones',
                   'acid006_am_tuning_curve_20230511_01pre.mkv',
                   'acid006_am_tuning_curve_20230511apre.h5', cameraParams) 

videos.add_session('2023-05-11', 'preHighFreq',
                   'acid006_oddball_sequence_20230511_01pre.mkv',
                   'acid006_oddball_sequence_20230511apre', cameraParams) 

videos.add_session('2023-05-11', 'preLowFreq',
                   'acid006_oddball_sequence_20230511_02pre.mkv',
                   'acid006_oddball_sequence_20230511bpre', cameraParams)

videos.add_session('2023-05-11', 'preFM_Down',
                   'acid006_oddball_sequence_20230511_03pre.mkv',
                   'acid006_oddball_sequence_20230511cpre', cameraParams)
                   
videos.add_session('2023-05-11', 'preFM_Up',
                   'acid006_oddball_sequence_20230511_04pre.mkv',
                   'acid006_oddball_sequence_20230511dpre', cameraParams)
# Saline

videos.add_session('2023-05-11', 'salinePureTones',
                   'acid006_am_tuning_curve_20230511_01saline.mkv',
                   'acid006_am_tuning_curve_20230511asaline.h5', cameraParams) 

videos.add_session('2023-05-11', 'salineHighFreq',
                   'acid006_oddball_sequence_20230511_01saline.mkv',
                   'acid006_oddball_sequence_20230511asaline', cameraParams) 

videos.add_session('2023-05-11', 'salineLowFreq',
                   'acid006_oddball_sequence_20230511_02saline.mkv',
                   'acid006_oddball_sequence_20230511bsaline', cameraParams)

videos.add_session('2023-05-11', 'salineFM_Down',
                   'acid006_oddball_sequence_20230511_03saline.mkv',
                   'acid006_oddball_sequence_20230511csaline', cameraParams)
                   
videos.add_session('2023-05-11', 'salineFM_Up',
                   'acid006_oddball_sequence_20230511_04saline.mkv',
                   'acid006_oddball_sequence_20230511dsaline', cameraParams)
                   
# DOI

videos.add_session('2023-05-11', 'doiPureTones',
                   'acid006_am_tuning_curve_20230511_01doi.mkv',
                   'acid006_am_tuning_curve_20230511adoi.h5', cameraParams) 

videos.add_session('2023-05-11', 'doiHighFreq',
                   'acid006_oddball_sequence_20230511_01doi.mkv',
                   'acid006_oddball_sequence_20230511adoi', cameraParams) 

videos.add_session('2023-05-11', 'doiLowFreq',
                   'acid006_oddball_sequence_20230511_02doi.mkv',
                   'acid006_oddball_sequence_20230511bdoi', cameraParams)

videos.add_session('2023-05-11', 'doiFM_Down',
                   'acid006_oddball_sequence_20230511_03doi.mkv',
                   'acid006_oddball_sequence_20230511cdoi', cameraParams)
                   
videos.add_session('2023-05-11', 'doiFM_Up',
                   'acid006_oddball_sequence_20230511_04doi.mkv',
                   'acid006_oddball_sequence_20230511ddoi', cameraParams)                   
                   


# 2023-05-18
# DOI & Saline

videos.add_session('2023-05-18', 'prePureTones',
                   'acid006_am_tuning_curve_20230518_01pre.mkv',
                   'acid006_am_tuning_curve_20230518apre.h5', cameraParams) 

videos.add_session('2023-05-18', 'preHighFreq',
                   'acid006_oddball_sequence_20230518_01pre.mkv',
                   'acid006_oddball_sequence_20230518apre', cameraParams) 

videos.add_session('2023-05-18', 'preLowFreq',
                   'acid006_oddball_sequence_20230518_02pre.mkv',
                   'acid006_oddball_sequence_20230518bpre', cameraParams)

videos.add_session('2023-05-18', 'preFM_Down',
                   'acid006_oddball_sequence_20230518_03pre.mkv',
                   'acid006_oddball_sequence_20230518cpre', cameraParams)
                   
videos.add_session('2023-05-18', 'preFM_Up',
                   'acid006_oddball_sequence_20230518_04pre.mkv',
                   'acid006_oddball_sequence_20230518dpre', cameraParams)
# Saline

videos.add_session('2023-05-18', 'salinePureTones',
                   'acid006_am_tuning_curve_20230518_01saline.mkv',
                   'acid006_am_tuning_curve_20230518asaline.h5', cameraParams) 

videos.add_session('2023-05-18', 'salineHighFreq',
                   'acid006_oddball_sequence_20230518_01saline.mkv',
                   'acid006_oddball_sequence_20230518asaline', cameraParams) 

videos.add_session('2023-05-18', 'salineLowFreq',
                   'acid006_oddball_sequence_20230518_02saline.mkv',
                   'acid006_oddball_sequence_20230518bsaline', cameraParams)

videos.add_session('2023-05-18', 'salineFM_Down',
                   'acid006_oddball_sequence_20230518_03saline.mkv',
                   'acid006_oddball_sequence_20230518csaline', cameraParams)
                   
videos.add_session('2023-05-18', 'salineFM_Up',
                   'acid006_oddball_sequence_20230518_04saline.mkv',
                   'acid006_oddball_sequence_20230518dsaline', cameraParams)
                   
# DOI

videos.add_session('2023-05-18', 'doiPureTones',
                   'acid006_am_tuning_curve_20230518_01doi.mkv',
                   'acid006_am_tuning_curve_20230518adoi.h5', cameraParams) 

videos.add_session('2023-05-18', 'doiHighFreq',
                   'acid006_oddball_sequence_20230518_01doi.mkv',
                   'acid006_oddball_sequence_20230518adoi', cameraParams) 

videos.add_session('2023-05-18', 'doiLowFreq',
                   'acid006_oddball_sequence_20230518_02doi.mkv',
                   'acid006_oddball_sequence_20230518bdoi', cameraParams)

videos.add_session('2023-05-18', 'doiFM_Down',
                   'acid006_oddball_sequence_20230518_03doi.mkv',
                   'acid006_oddball_sequence_20230518cdoi', cameraParams)
                   
videos.add_session('2023-05-18', 'doiFM_Up',
                   'acid006_oddball_sequence_20230518_04doi.mkv',
                   'acid006_oddball_sequence_20230518ddoi', cameraParams)                   


# 2023-05-25
# DOI & Saline

videos.add_session('2023-05-25', 'prePureTones',
                   'acid006_am_tuning_curve_20230525_01pre.mkv',
                   'acid006_am_tuning_curve_20230525apre.h5', cameraParams) 

videos.add_session('2023-05-25', 'preHighFreq',
                   'acid006_oddball_sequence_20230525_01pre.mkv',
                   'acid006_oddball_sequence_20230525apre', cameraParams) 

videos.add_session('2023-05-25', 'preLowFreq',
                   'acid006_oddball_sequence_20230525_02pre.mkv',
                   'acid006_oddball_sequence_20230525bpre', cameraParams)

videos.add_session('2023-05-25', 'preFM_Down',
                   'acid006_oddball_sequence_20230525_03pre.mkv',
                   'acid006_oddball_sequence_20230525cpre', cameraParams)
                   
videos.add_session('2023-05-25', 'preFM_Up',
                   'acid006_oddball_sequence_20230525_04pre.mkv',
                   'acid006_oddball_sequence_20230525dpre', cameraParams)
# Saline

videos.add_session('2023-05-25', 'salinePureTones',
                   'acid006_am_tuning_curve_20230525_01saline.mkv',
                   'acid006_am_tuning_curve_20230525asaline.h5', cameraParams) 

videos.add_session('2023-05-25', 'salineHighFreq',
                   'acid006_oddball_sequence_20230525_01saline.mkv',
                   'acid006_oddball_sequence_20230525asaline', cameraParams) 

videos.add_session('2023-05-25', 'salineLowFreq',
                   'acid006_oddball_sequence_20230525_02saline.mkv',
                   'acid006_oddball_sequence_20230525bsaline', cameraParams)

videos.add_session('2023-05-25', 'salineFM_Down',
                   'acid006_oddball_sequence_20230525_03saline.mkv',
                   'acid006_oddball_sequence_20230525csaline', cameraParams)
                   
videos.add_session('2023-05-25', 'salineFM_Up',
                   'acid006_oddball_sequence_20230525_04saline.mkv',
                   'acid006_oddball_sequence_20230525dsaline', cameraParams)
                   
# DOI

videos.add_session('2023-05-25', 'doiPureTones',
                   'acid006_am_tuning_curve_20230525_01doi.mkv',
                   'acid006_am_tuning_curve_20230525adoi.h5', cameraParams) 

videos.add_session('2023-05-25', 'doiHighFreq',
                   'acid006_oddball_sequence_20230525_01doi.mkv',
                   'acid006_oddball_sequence_20230525adoi', cameraParams) 

videos.add_session('2023-05-25', 'doiLowFreq',
                   'acid006_oddball_sequence_20230525_02doi.mkv',
                   'acid006_oddball_sequence_20230525bdoi', cameraParams)

videos.add_session('2023-05-25', 'doiFM_Down',
                   'acid006_oddball_sequence_20230525_03doi.mkv',
                   'acid006_oddball_sequence_20230525cdoi', cameraParams)
                   
videos.add_session('2023-05-25', 'doiFM_Up',
                   'acid006_oddball_sequence_20230525_04doi.mkv',
                   'acid006_oddball_sequence_20230525ddoi', cameraParams)
                   
videos.add_session('2023-05-25', 'doiSpontaneous',
                   'acid006_doiSpontaneous.mkv',
                   '', cameraParams)                                                
