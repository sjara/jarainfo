from jaratoolbox import videoinfo

subject = 'acid007'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# ----------------------

# 2023-03-23
#Saline injection

videos.add_session('2023-03-23', 'prePureTones',
                   'acid007_am_tuning_curve_20230323_01pre.mkv',
                   'acid007_am_tuning_curve_20230323apre.h5', cameraParams) 

videos.add_session('2023-03-23', 'preHighFreq',
                   'acid007_oddball_sequence_20230323_01pre.mkv',
                   'acid007_oddball_sequence_20230323apre', cameraParams) 

videos.add_session('2023-03-23', 'preLowFreq',
                   'acid007_oddball_sequence_20230323_02pre.mkv',
                   'acid007_oddball_sequence_20230323bpre', cameraParams)

videos.add_session('2023-03-23', 'preFM_Down',
                   'acid007_oddball_sequence_20230323_03pre.mkv',
                   'acid007_oddball_sequence_20230323cpre', cameraParams)
                   
videos.add_session('2023-03-23', 'preFM_Up',
                   'acid007_oddball_sequence_20230323_04pre.mkv',
                   'acid007_oddball_sequence_20230323dpre', cameraParams)
# Saline

videos.add_session('2023-03-23', 'salinePureTones',
                   'acid007_am_tuning_curve_20230323_01saline.mkv',
                   'acid007_am_tuning_curve_20230323asaline.h5', cameraParams) 

videos.add_session('2023-03-23', 'salineHighFreq',
                   'acid007_oddball_sequence_20230323_01saline.mkv',
                   'acid007_oddball_sequence_20230323asaline', cameraParams) 

videos.add_session('2023-03-23', 'salineLowFreq',
                   'acid007_oddball_sequence_20230323_02saline.mkv',
                   'acid007_oddball_sequence_20230323bsaline', cameraParams)

videos.add_session('2023-03-23', 'salineFM_Down',
                   'acid007_oddball_sequence_20230323_03saline.mkv',
                   'acid007_oddball_sequence_20230323csaline', cameraParams)
                   
videos.add_session('2023-03-23', 'salineFM_Up',
                   'acid007_oddball_sequence_20230323_04saline.mkv',
                   'acid007_oddball_sequence_20230323dsaline', cameraParams)
                   

# 2023-03-24
#DOI injection

videos.add_session('2023-03-24', 'prePureTones',
                   'acid007_am_tuning_curve_20230324_01pre.mkv',
                   'acid007_am_tuning_curve_20230324apre.h5', cameraParams) 

videos.add_session('2023-03-24', 'preHighFreq',
                   'acid007_oddball_sequence_20230324_01pre.mkv',
                   'acid007_oddball_sequence_20230324apre', cameraParams) 

videos.add_session('2023-03-24', 'preLowFreq',
                   'acid007_oddball_sequence_20230324_02pre.mkv',
                   'acid007_oddball_sequence_20230324bpre', cameraParams)

videos.add_session('2023-03-24', 'preFM_Down',
                   'acid007_oddball_sequence_20230324_03pre.mkv',
                   'acid007_oddball_sequence_20230324cpre', cameraParams)
                   
videos.add_session('2023-03-24', 'preFM_Up',
                   'acid007_oddball_sequence_20230324_04pre.mkv',
                   'acid007_oddball_sequence_20230324dpre', cameraParams)                   

# DOI

videos.add_session('2023-03-24', 'doiPureTones',
                   'acid007_am_tuning_curve_20230324_01doi.mkv',
                   'acid007_am_tuning_curve_20230324adoi.h5', cameraParams) 

videos.add_session('2023-03-24', 'doiHighFreq',
                   'acid007_oddball_sequence_20230324_01doi.mkv',
                   'acid007_oddball_sequence_20230324adoi', cameraParams) 

videos.add_session('2023-03-24', 'doiLowFreq',
                   'acid007_oddball_sequence_20230324_02doi.mkv',
                   'acid007_oddball_sequence_20230324bdoi', cameraParams)

videos.add_session('2023-03-24', 'doiFM_Down',
                   'acid007_oddball_sequence_20230324_03doi.mkv',
                   'acid007_oddball_sequence_20230324cdoi', cameraParams)
                   
videos.add_session('2023-03-24', 'doiFM_Up',
                   'acid007_oddball_sequence_20230324_04doi.mkv',
                   'acid007_oddball_sequence_20230324ddoi', cameraParams)
                      
