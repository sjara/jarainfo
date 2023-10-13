from jaratoolbox import videoinfo

subject = 'sole018'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

# Session parameters: date, sessionType, videoFile, behavFile, cameraParams

# ----------------------

# 2023-10-13

#videos.add_session('2023-08-04', 'prePureTones',
                   'acid009_am_tuning_curve_20230804_01pre.mkv',
                   'acid009_am_tuning_curve_20230804apre.h5', cameraParams)

#videos.add_session('2023-08-04', 'preHighFreq',
                   'acid009_oddball_sequence_20230804_01pre.mkv',
                   'acid009_oddball_sequence_20230804apre', cameraParams)

#videos.add_session('2023-08-04', 'preLowFreq',
                   'acid009_oddball_sequence_20230804_02pre.mkv',
                   'acid009_oddball_sequence_20230804bpre', cameraParams)

#videos.add_session('2023-08-04', 'preFM_Down',
                   'acid009_oddball_sequence_20230804_03pre.mkv',
                   'acid009_oddball_sequence_20230804cpre', cameraParams)

#videos.add_session('2023-08-04', 'preFM_Up',
                   'acid009_oddball_sequence_20230804_04pre.mkv',
                   'acid009_oddball_sequence_20230804dpre', cameraParams)
