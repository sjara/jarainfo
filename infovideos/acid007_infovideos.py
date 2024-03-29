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



# 2023-05-17
# DOI & Saline

videos.add_session('2023-05-17', 'prePureTones',
                   'acid007_am_tuning_curve_20230517_01pre.mkv',
                   'acid007_am_tuning_curve_20230517apre.h5', cameraParams) 

videos.add_session('2023-05-17', 'preHighFreq',
                   'acid007_oddball_sequence_20230517_01pre.mkv',
                   'acid007_oddball_sequence_20230517apre', cameraParams) 

videos.add_session('2023-05-17', 'preLowFreq',
                   'acid007_oddball_sequence_20230517_02pre.mkv',
                   'acid007_oddball_sequence_20230517bpre', cameraParams)

videos.add_session('2023-05-17', 'preFM_Down',
                   'acid007_oddball_sequence_20230517_03pre.mkv',
                   'acid007_oddball_sequence_20230517cpre', cameraParams)
                   
videos.add_session('2023-05-17', 'preFM_Up',
                   'acid007_oddball_sequence_20230517_04pre.mkv',
                   'acid007_oddball_sequence_20230517dpre', cameraParams)
# Saline

videos.add_session('2023-05-17', 'salinePureTones',
                   'acid007_am_tuning_curve_20230517_01saline.mkv',
                   'acid007_am_tuning_curve_20230517asaline.h5', cameraParams) 

videos.add_session('2023-05-17', 'salineHighFreq',
                   'acid007_oddball_sequence_20230517_01saline.mkv',
                   'acid007_oddball_sequence_20230517asaline', cameraParams) 

videos.add_session('2023-05-17', 'salineLowFreq',
                   'acid007_oddball_sequence_20230517_02saline.mkv',
                   'acid007_oddball_sequence_20230517bsaline', cameraParams)

videos.add_session('2023-05-17', 'salineFM_Down',
                   'acid007_oddball_sequence_20230517_03saline.mkv',
                   'acid007_oddball_sequence_20230517csaline', cameraParams)
                   
videos.add_session('2023-05-17', 'salineFM_Up',
                   'acid007_oddball_sequence_20230517_04saline.mkv',
                   'acid007_oddball_sequence_20230517dsaline', cameraParams)
                   
# DOI

videos.add_session('2023-05-17', 'doiPureTones',
                   'acid007_am_tuning_curve_20230517_01doi.mkv',
                   'acid007_am_tuning_curve_20230517adoi.h5', cameraParams) 

videos.add_session('2023-05-17', 'doiHighFreq',
                   'acid007_oddball_sequence_20230517_01doi.mkv',
                   'acid007_oddball_sequence_20230517adoi', cameraParams) 

videos.add_session('2023-05-17', 'doiLowFreq',
                   'acid007_oddball_sequence_20230517_02doi.mkv',
                   'acid007_oddball_sequence_20230517bdoi', cameraParams)

videos.add_session('2023-05-17', 'doiFM_Down',
                   'acid007_oddball_sequence_20230517_03doi.mkv',
                   'acid007_oddball_sequence_20230517cdoi', cameraParams)
                   
videos.add_session('2023-05-17', 'doiFM_Up',
                   'acid007_oddball_sequence_20230517_04doi.mkv',
                   'acid007_oddball_sequence_20230517ddoi', cameraParams)                   
                   
     

# 2023-05-19
# DOI & Saline

videos.add_session('2023-05-19', 'prePureTones',
                   'acid007_am_tuning_curve_20230519_01pre.mkv',
                   'acid007_am_tuning_curve_20230519apre.h5', cameraParams) 

videos.add_session('2023-05-19', 'preHighFreq',
                   'acid007_oddball_sequence_20230519_01pre.mkv',
                   'acid007_oddball_sequence_20230519apre', cameraParams) 

videos.add_session('2023-05-19', 'preLowFreq',
                   'acid007_oddball_sequence_20230519_02pre.mkv',
                   'acid007_oddball_sequence_20230519bpre', cameraParams)

videos.add_session('2023-05-19', 'preFM_Down',
                   'acid007_oddball_sequence_20230519_03pre.mkv',
                   'acid007_oddball_sequence_20230519cpre', cameraParams)
                   
videos.add_session('2023-05-19', 'preFM_Up',
                   'acid007_oddball_sequence_20230519_04pre.mkv',
                   'acid007_oddball_sequence_20230519dpre', cameraParams)
# Saline

videos.add_session('2023-05-19', 'salinePureTones',
                   'acid007_am_tuning_curve_20230519_01saline.mkv',
                   'acid007_am_tuning_curve_20230519asaline.h5', cameraParams) 

videos.add_session('2023-05-19', 'salineHighFreq',
                   'acid007_oddball_sequence_20230519_01saline.mkv',
                   'acid007_oddball_sequence_20230519asaline', cameraParams) 

videos.add_session('2023-05-19', 'salineLowFreq',
                   'acid007_oddball_sequence_20230519_02saline.mkv',
                   'acid007_oddball_sequence_20230519bsaline', cameraParams)

videos.add_session('2023-05-19', 'salineFM_Down',
                   'acid007_oddball_sequence_20230519_03saline.mkv',
                   'acid007_oddball_sequence_20230519csaline', cameraParams)
                   
videos.add_session('2023-05-19', 'salineFM_Up',
                   'acid007_oddball_sequence_20230519_04saline.mkv',
                   'acid007_oddball_sequence_20230519dsaline', cameraParams)
                   
# DOI

videos.add_session('2023-05-19', 'doiPureTones',
                   'acid007_am_tuning_curve_20230519_01doi.mkv',
                   'acid007_am_tuning_curve_20230519adoi.h5', cameraParams) 

videos.add_session('2023-05-19', 'doiHighFreq',
                   'acid007_oddball_sequence_20230519_01doi.mkv',
                   'acid007_oddball_sequence_20230519adoi', cameraParams) 

videos.add_session('2023-05-19', 'doiLowFreq',
                   'acid007_oddball_sequence_20230519_02doi.mkv',
                   'acid007_oddball_sequence_20230519bdoi', cameraParams)

videos.add_session('2023-05-19', 'doiFM_Down',
                   'acid007_oddball_sequence_20230519_03doi.mkv',
                   'acid007_oddball_sequence_20230519cdoi', cameraParams)
                   
videos.add_session('2023-05-19', 'doiFM_Up',
                   'acid007_oddball_sequence_20230519_04doi.mkv',
                   'acid007_oddball_sequence_20230519ddoi', cameraParams)                   
                   
     
# 2023-05-25
# DOI & Saline

videos.add_session('2023-05-25', 'prePureTones',
                   'acid007_am_tuning_curve_20230525_01pre.mkv',
                   'acid007_am_tuning_curve_20230525apre.h5', cameraParams) 

videos.add_session('2023-05-25', 'preHighFreq',
                   'acid007_oddball_sequence_20230525_01pre.mkv',
                   'acid007_oddball_sequence_20230525apre', cameraParams) 

videos.add_session('2023-05-25', 'preLowFreq',
                   'acid007_oddball_sequence_20230525_02pre.mkv',
                   'acid007_oddball_sequence_20230525bpre', cameraParams)

videos.add_session('2023-05-25', 'preFM_Down',
                   'acid007_oddball_sequence_20230525_03pre.mkv',
                   'acid007_oddball_sequence_20230525cpre', cameraParams)
                   
videos.add_session('2023-05-25', 'preFM_Up',
                   'acid007_oddball_sequence_20230525_04pre.mkv',
                   'acid007_oddball_sequence_20230525dpre', cameraParams)
# Saline
videos.add_session('2023-05-25', 'salineInjection',
                   'acid007_20230525_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-05-25', 'salinePureTones',
                   'acid007_am_tuning_curve_20230525_01saline.mkv',
                   'acid007_am_tuning_curve_20230525asaline.h5', cameraParams) 

videos.add_session('2023-05-25', 'salineHighFreq',
                   'acid007_oddball_sequence_20230525_01saline.mkv',
                   'acid007_oddball_sequence_20230525asaline', cameraParams) 

videos.add_session('2023-05-25', 'salineLowFreq',
                   'acid007_oddball_sequence_20230525_02saline.mkv',
                   'acid007_oddball_sequence_20230525bsaline', cameraParams)

videos.add_session('2023-05-25', 'salineFM_Down',
                   'acid007_oddball_sequence_20230525_03saline.mkv',
                   'acid007_oddball_sequence_20230525csaline', cameraParams)
                   
videos.add_session('2023-05-25', 'salineFM_Up',
                   'acid007_oddball_sequence_20230525_04saline.mkv',
                   'acid007_oddball_sequence_20230525dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-05-25', 'doiInjection',
                   'acid007_20230525_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-05-25', 'doiPureTones',
                   'acid007_am_tuning_curve_20230525_01doi.mkv',
                   'acid007_am_tuning_curve_20230525adoi.h5', cameraParams) 

videos.add_session('2023-05-25', 'doiHighFreq',
                   'acid007_oddball_sequence_20230525_01doi.mkv',
                   'acid007_oddball_sequence_20230525adoi', cameraParams) 

videos.add_session('2023-05-25', 'doiLowFreq',
                   'acid007_oddball_sequence_20230525_02doi.mkv',
                   'acid007_oddball_sequence_20230525bdoi', cameraParams)

videos.add_session('2023-05-25', 'doiFM_Down',
                   'acid007_oddball_sequence_20230525_03doi.mkv',
                   'acid007_oddball_sequence_20230525cdoi', cameraParams)
                   
videos.add_session('2023-05-25', 'doiFM_Up',
                   'acid007_oddball_sequence_20230525_04doi.mkv',
                   'acid007_oddball_sequence_20230525ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-05-25', 'doiSpontaneous',
                   'acid007_20230525_doiSpontaneous.mkv',
                   '', cameraParams)
                   
# 2023-05-31
# DOI & Saline

videos.add_session('2023-05-31', 'prePureTones',
                   'acid007_am_tuning_curve_20230531_01pre.mkv',
                   'acid007_am_tuning_curve_20230531apre.h5', cameraParams) 

videos.add_session('2023-05-31', 'preHighFreq',
                   'acid007_oddball_sequence_20230531_01pre.mkv',
                   'acid007_oddball_sequence_20230531apre', cameraParams) 

videos.add_session('2023-05-31', 'preLowFreq',
                   'acid007_oddball_sequence_20230531_02pre.mkv',
                   'acid007_oddball_sequence_20230531bpre', cameraParams)

videos.add_session('2023-05-31', 'preFM_Down',
                   'acid007_oddball_sequence_20230531_03pre.mkv',
                   'acid007_oddball_sequence_20230531cpre', cameraParams)
                   
videos.add_session('2023-05-31', 'preFM_Up',
                   'acid007_oddball_sequence_20230531_04pre.mkv',
                   'acid007_oddball_sequence_20230531dpre', cameraParams)
# Saline
videos.add_session('2023-05-31', 'salineInjection',
                   'acid007_20230531_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-05-31', 'salinePureTones',
                   'acid007_am_tuning_curve_20230531_01saline.mkv',
                   'acid007_am_tuning_curve_20230531asaline.h5', cameraParams) 

videos.add_session('2023-05-31', 'salineHighFreq',
                   'acid007_oddball_sequence_20230531_01saline.mkv',
                   'acid007_oddball_sequence_20230531asaline', cameraParams) 

videos.add_session('2023-05-31', 'salineLowFreq',
                   'acid007_oddball_sequence_20230531_02saline.mkv',
                   'acid007_oddball_sequence_20230531bsaline', cameraParams)

videos.add_session('2023-05-31', 'salineFM_Down',
                   'acid007_oddball_sequence_20230531_03saline.mkv',
                   'acid007_oddball_sequence_20230531csaline', cameraParams)
                   
videos.add_session('2023-05-31', 'salineFM_Up',
                   'acid007_oddball_sequence_20230531_04saline.mkv',
                   'acid007_oddball_sequence_20230531dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-05-31', 'doiInjection',
                   'acid007_20230531_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-05-31', 'doiPureTones',
                   'acid007_am_tuning_curve_20230531_01doi.mkv',
                   'acid007_am_tuning_curve_20230531adoi.h5', cameraParams) 

videos.add_session('2023-05-31', 'doiHighFreq',
                   'acid007_oddball_sequence_20230531_01doi.mkv',
                   'acid007_oddball_sequence_20230531adoi', cameraParams) 

videos.add_session('2023-05-31', 'doiLowFreq',
                   'acid007_oddball_sequence_20230531_02doi.mkv',
                   'acid007_oddball_sequence_20230531bdoi', cameraParams)

videos.add_session('2023-05-31', 'doiFM_Down',
                   'acid007_oddball_sequence_20230531_03doi.mkv',
                   'acid007_oddball_sequence_20230531cdoi', cameraParams)
                   
videos.add_session('2023-05-31', 'doiFM_Up',
                   'acid007_oddball_sequence_20230531_04doi.mkv',
                   'acid007_oddball_sequence_20230531ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-05-31', 'doiSpontaneous',
                   'acid007_20230531_doiSpontaneous.mkv',
                   '', cameraParams) 

# 2023-06-14
# DOI & Saline

videos.add_session('2023-06-14', 'prePureTones',
                   'acid007_am_tuning_curve_20230614_01pre.mkv',
                   'acid007_am_tuning_curve_20230614apre.h5', cameraParams) 

videos.add_session('2023-06-14', 'preHighFreq',
                   'acid007_oddball_sequence_20230614_01pre.mkv',
                   'acid007_oddball_sequence_20230614apre', cameraParams) 

videos.add_session('2023-06-14', 'preLowFreq',
                   'acid007_oddball_sequence_20230614_02pre.mkv',
                   'acid007_oddball_sequence_20230614bpre', cameraParams)

videos.add_session('2023-06-14', 'preFM_Down',
                   'acid007_oddball_sequence_20230614_03pre.mkv',
                   'acid007_oddball_sequence_20230614cpre', cameraParams)
                   
videos.add_session('2023-06-14', 'preFM_Up',
                   'acid007_oddball_sequence_20230614_04pre.mkv',
                   'acid007_oddball_sequence_20230614dpre', cameraParams)
# Saline
videos.add_session('2023-06-14', 'salineInjection',
                   'acid007_20230614_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-06-14', 'salinePureTones',
                   'acid007_am_tuning_curve_20230614_01saline.mkv',
                   'acid007_am_tuning_curve_20230614asaline.h5', cameraParams) 

videos.add_session('2023-06-14', 'salineHighFreq',
                   'acid007_oddball_sequence_20230614_01saline.mkv',
                   'acid007_oddball_sequence_20230614asaline', cameraParams) 

videos.add_session('2023-06-14', 'salineLowFreq',
                   'acid007_oddball_sequence_20230614_02saline.mkv',
                   'acid007_oddball_sequence_20230614bsaline', cameraParams)

videos.add_session('2023-06-14', 'salineFM_Down',
                   'acid007_oddball_sequence_20230614_03saline.mkv',
                   'acid007_oddball_sequence_20230614csaline', cameraParams)
                   
videos.add_session('2023-06-14', 'salineFM_Up',
                   'acid007_oddball_sequence_20230614_04saline.mkv',
                   'acid007_oddball_sequence_20230614dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-06-14', 'doiInjection',
                   'acid007_20230614_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-06-14', 'doiPureTones',
                   'acid007_am_tuning_curve_20230614_01doi.mkv',
                   'acid007_am_tuning_curve_20230614adoi.h5', cameraParams) 

videos.add_session('2023-06-14', 'doiHighFreq',
                   'acid007_oddball_sequence_20230614_01doi.mkv',
                   'acid007_oddball_sequence_20230614adoi', cameraParams) 

videos.add_session('2023-06-14', 'doiLowFreq',
                   'acid007_oddball_sequence_20230614_02doi.mkv',
                   'acid007_oddball_sequence_20230614bdoi', cameraParams)

videos.add_session('2023-06-14', 'doiFM_Down',
                   'acid007_oddball_sequence_20230614_03doi.mkv',
                   'acid007_oddball_sequence_20230614cdoi', cameraParams)
                   
videos.add_session('2023-06-14', 'doiFM_Up',
                   'acid007_oddball_sequence_20230614_04doi.mkv',
                   'acid007_oddball_sequence_20230614ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-06-14', 'doiSpontaneous',
                   'acid007_20230614_doiSpontaneous.mkv',
                   '', cameraParams)                                                                    
