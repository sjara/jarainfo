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
                   
     
