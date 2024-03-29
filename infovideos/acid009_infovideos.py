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

                   
# EVERY SESSION AFTER HERE HAS A 1-2 SECOND MANUAL SYNC LIGHT BEFORE AND AFTER THE TRIALS.
# 2023-08-08

videos.add_session('2023-08-08', 'prePureTones',
                   'acid009_am_tuning_curve_20230808_01pre.mkv',
                   'acid009_am_tuning_curve_20230808apre.h5', cameraParams) 

videos.add_session('2023-08-08', 'preHighFreq',
                   'acid009_oddball_sequence_20230808_01pre.mkv',
                   'acid009_oddball_sequence_20230808apre', cameraParams) 

videos.add_session('2023-08-08', 'preLowFreq',
                   'acid009_oddball_sequence_20230808_02pre.mkv',
                   'acid009_oddball_sequence_20230808bpre', cameraParams)

videos.add_session('2023-08-08', 'preFM_Down',
                   'acid009_oddball_sequence_20230808_03pre.mkv',
                   'acid009_oddball_sequence_20230808cpre', cameraParams)
                   
videos.add_session('2023-08-08', 'preFM_Up',
                   'acid009_oddball_sequence_20230808_04pre.mkv',
                   'acid009_oddball_sequence_20230808dpre', cameraParams)
# Saline
videos.add_session('2023-08-08', 'salineInjection',
                   'acid009_20230808_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-08-08', 'salinePureTones',
                   'acid009_am_tuning_curve_20230808_01saline.mkv',
                   'acid009_am_tuning_curve_20230808asaline.h5', cameraParams) 

videos.add_session('2023-08-08', 'salineHighFreq',
                   'acid009_oddball_sequence_20230808_01saline.mkv',
                   'acid009_oddball_sequence_20230808asaline', cameraParams) 

videos.add_session('2023-08-08', 'salineLowFreq',
                   'acid009_oddball_sequence_20230808_02saline.mkv',
                   'acid009_oddball_sequence_20230808bsaline', cameraParams)

videos.add_session('2023-08-08', 'salineFM_Down',
                   'acid009_oddball_sequence_20230808_03saline.mkv',
                   'acid009_oddball_sequence_20230808csaline', cameraParams)
                   
videos.add_session('2023-08-08', 'salineFM_Up',
                   'acid009_oddball_sequence_20230808_04saline.mkv',
                   'acid009_oddball_sequence_20230808dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-08-08', 'doiInjection',
                   'acid009_20230808_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-08-08', 'doiPureTones',
                   'acid009_am_tuning_curve_20230808_01doi.mkv',
                   'acid009_am_tuning_curve_20230808adoi.h5', cameraParams) 

videos.add_session('2023-08-08', 'doiHighFreq',
                   'acid009_oddball_sequence_20230808_01doi.mkv',
                   'acid009_oddball_sequence_20230808adoi', cameraParams) 

videos.add_session('2023-08-08', 'doiLowFreq',
                   'acid009_oddball_sequence_20230808_02doi.mkv',
                   'acid009_oddball_sequence_20230808bdoi', cameraParams)

videos.add_session('2023-08-08', 'doiFM_Down',
                   'acid009_oddball_sequence_20230808_03doi.mkv',
                   'acid009_oddball_sequence_20230808cdoi', cameraParams)
                   
videos.add_session('2023-08-08', 'doiFM_Up',
                   'acid009_oddball_sequence_20230808_04doi.mkv',
                   'acid009_oddball_sequence_20230808ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-08-08', 'doiSpontaneous',
                   'acid009_20230808_doiSpontaneous.mkv','', cameraParams)


# 2023-08-10

videos.add_session('2023-08-10', 'prePureTones',
                   'acid009_am_tuning_curve_20230810_01pre.mkv',
                   'acid009_am_tuning_curve_20230810apre.h5', cameraParams) 

videos.add_session('2023-08-10', 'preHighFreq',
                   'acid009_oddball_sequence_20230810_01pre.mkv',
                   'acid009_oddball_sequence_20230810apre', cameraParams) 

videos.add_session('2023-08-10', 'preLowFreq',
                   'acid009_oddball_sequence_20230810_02pre.mkv',
                   'acid009_oddball_sequence_20230810bpre', cameraParams)

videos.add_session('2023-08-10', 'preFM_Down',
                   'acid009_oddball_sequence_20230810_03pre.mkv',
                   'acid009_oddball_sequence_20230810cpre', cameraParams)
                   
videos.add_session('2023-08-10', 'preFM_Up',
                   'acid009_oddball_sequence_20230810_04pre.mkv',
                   'acid009_oddball_sequence_20230810dpre', cameraParams)
# Saline
videos.add_session('2023-08-10', 'salineInjection',
                   'acid009_20230810_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-08-10', 'salinePureTones',
                   'acid009_am_tuning_curve_20230810_01saline.mkv',
                   'acid009_am_tuning_curve_20230810asaline.h5', cameraParams) 

videos.add_session('2023-08-10', 'salineHighFreq',
                   'acid009_oddball_sequence_20230810_01saline.mkv',
                   'acid009_oddball_sequence_20230810asaline', cameraParams) 

videos.add_session('2023-08-10', 'salineLowFreq',
                   'acid009_oddball_sequence_20230810_02saline.mkv',
                   'acid009_oddball_sequence_20230810bsaline', cameraParams)

videos.add_session('2023-08-10', 'salineFM_Down',
                   'acid009_oddball_sequence_20230810_03saline.mkv',
                   'acid009_oddball_sequence_20230810csaline', cameraParams)
                   
videos.add_session('2023-08-10', 'salineFM_Up',
                   'acid009_oddball_sequence_20230810_04saline.mkv',
                   'acid009_oddball_sequence_20230810dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-08-10', 'doiInjection',
                   'acid009_20230810_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-08-10', 'doiPureTones',
                   'acid009_am_tuning_curve_20230810_01doi.mkv',
                   'acid009_am_tuning_curve_20230810adoi.h5', cameraParams) 

videos.add_session('2023-08-10', 'doiHighFreq',
                   'acid009_oddball_sequence_20230810_01doi.mkv',
                   'acid009_oddball_sequence_20230810adoi', cameraParams) 

videos.add_session('2023-08-10', 'doiLowFreq',
                   'acid009_oddball_sequence_20230810_02doi.mkv',
                   'acid009_oddball_sequence_20230810bdoi', cameraParams)

videos.add_session('2023-08-10', 'doiFM_Down',
                   'acid009_oddball_sequence_20230810_03doi.mkv',
                   'acid009_oddball_sequence_20230810cdoi', cameraParams)
                   
videos.add_session('2023-08-10', 'doiFM_Up',
                   'acid009_oddball_sequence_20230810_04doi.mkv',
                   'acid009_oddball_sequence_20230810ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-08-10', 'doiSpontaneous',
                   'acid009_20230810_doiSpontaneous.mkv','', cameraParams)
                                                                                   
   
                                                                                   
# 2023-08-14

videos.add_session('2023-08-14', 'prePureTones',
                   'acid009_am_tuning_curve_20230814_01pre.mkv',
                   'acid009_am_tuning_curve_20230814apre.h5', cameraParams) 

videos.add_session('2023-08-14', 'preHighFreq',
                   'acid009_oddball_sequence_20230814_01pre.mkv',
                   'acid009_oddball_sequence_20230814apre', cameraParams) 

videos.add_session('2023-08-14', 'preLowFreq',
                   'acid009_oddball_sequence_20230814_02pre.mkv',
                   'acid009_oddball_sequence_20230814bpre', cameraParams)

videos.add_session('2023-08-14', 'preFM_Down',
                   'acid009_oddball_sequence_20230814_03pre.mkv',
                   'acid009_oddball_sequence_20230814cpre', cameraParams)
                   
videos.add_session('2023-08-14', 'preFM_Up',
                   'acid009_oddball_sequence_20230814_04pre.mkv',
                   'acid009_oddball_sequence_20230814dpre', cameraParams)
# Saline
videos.add_session('2023-08-14', 'salineInjection',
                   'acid009_20230814_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-08-14', 'salinePureTones',
                   'acid009_am_tuning_curve_20230814_01saline.mkv',
                   'acid009_am_tuning_curve_20230814asaline.h5', cameraParams) 

videos.add_session('2023-08-14', 'salineHighFreq',
                   'acid009_oddball_sequence_20230814_01saline.mkv',
                   'acid009_oddball_sequence_20230814asaline', cameraParams) 

videos.add_session('2023-08-14', 'salineLowFreq',
                   'acid009_oddball_sequence_20230814_02saline.mkv',
                   'acid009_oddball_sequence_20230814bsaline', cameraParams)

videos.add_session('2023-08-14', 'salineFM_Down',
                   'acid009_oddball_sequence_20230814_03saline.mkv',
                   'acid009_oddball_sequence_20230814csaline', cameraParams)
                   
videos.add_session('2023-08-14', 'salineFM_Up',
                   'acid009_oddball_sequence_20230814_04saline.mkv',
                   'acid009_oddball_sequence_20230814dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-08-14', 'doiInjection',
                   'acid009_20230814_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-08-14', 'doiPureTones',
                   'acid009_am_tuning_curve_20230814_01doi.mkv',
                   'acid009_am_tuning_curve_20230814adoi.h5', cameraParams) 

videos.add_session('2023-08-14', 'doiHighFreq',
                   'acid009_oddball_sequence_20230814_01doi.mkv',
                   'acid009_oddball_sequence_20230814adoi', cameraParams) 

videos.add_session('2023-08-14', 'doiLowFreq',
                   'acid009_oddball_sequence_20230814_02doi.mkv',
                   'acid009_oddball_sequence_20230814bdoi', cameraParams)

videos.add_session('2023-08-14', 'doiFM_Down',
                   'acid009_oddball_sequence_20230814_03doi.mkv',
                   'acid009_oddball_sequence_20230814cdoi', cameraParams)
                   
videos.add_session('2023-08-14', 'doiFM_Up',
                   'acid009_oddball_sequence_20230814_04doi.mkv',
                   'acid009_oddball_sequence_20230814ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-08-14', 'doiSpontaneous',
                   'acid009_20230814_doiSpontaneous.mkv','', cameraParams)
                                                                          
                                                                          
                                                                          
# 2023-08-16

videos.add_session('2023-08-16', 'prePureTones',
                   'acid009_am_tuning_curve_20230816_01pre.mkv',
                   'acid009_am_tuning_curve_20230816apre.h5', cameraParams) 

videos.add_session('2023-08-16', 'preHighFreq',
                   'acid009_oddball_sequence_20230816_01pre.mkv',
                   'acid009_oddball_sequence_20230816apre', cameraParams) 

videos.add_session('2023-08-16', 'preLowFreq',
                   'acid009_oddball_sequence_20230816_02pre.mkv',
                   'acid009_oddball_sequence_20230816bpre', cameraParams)

videos.add_session('2023-08-16', 'preFM_Down',
                   'acid009_oddball_sequence_20230816_03pre.mkv',
                   'acid009_oddball_sequence_20230816cpre', cameraParams)
                   
videos.add_session('2023-08-16', 'preFM_Up',
                   'acid009_oddball_sequence_20230816_04pre.mkv',
                   'acid009_oddball_sequence_20230816dpre', cameraParams)
# Saline
videos.add_session('2023-08-16', 'salineInjection',
                   'acid009_20230816_salineInjection.mkv',
                   '', cameraParams)
                     

videos.add_session('2023-08-16', 'salinePureTones',
                   'acid009_am_tuning_curve_20230816_01saline.mkv',
                   'acid009_am_tuning_curve_20230816asaline.h5', cameraParams) 

videos.add_session('2023-08-16', 'salineHighFreq',
                   'acid009_oddball_sequence_20230816_01saline.mkv',
                   'acid009_oddball_sequence_20230816asaline', cameraParams) 

videos.add_session('2023-08-16', 'salineLowFreq',
                   'acid009_oddball_sequence_20230816_02saline.mkv',
                   'acid009_oddball_sequence_20230816bsaline', cameraParams)

videos.add_session('2023-08-16', 'salineFM_Down',
                   'acid009_oddball_sequence_20230816_03saline.mkv',
                   'acid009_oddball_sequence_20230816csaline', cameraParams)
                   
videos.add_session('2023-08-16', 'salineFM_Up',
                   'acid009_oddball_sequence_20230816_04saline.mkv',
                   'acid009_oddball_sequence_20230816dsaline', cameraParams)
                   
# DOI
videos.add_session('2023-08-16', 'doiInjection',
                   'acid009_20230816_doiInjection.mkv',
                   '', cameraParams)
                        

videos.add_session('2023-08-16', 'doiPureTones',
                   'acid009_am_tuning_curve_20230816_01doi.mkv',
                   'acid009_am_tuning_curve_20230816adoi.h5', cameraParams) 

videos.add_session('2023-08-16', 'doiHighFreq',
                   'acid009_oddball_sequence_20230816_01doi.mkv',
                   'acid009_oddball_sequence_20230816adoi', cameraParams) 

videos.add_session('2023-08-16', 'doiLowFreq',
                   'acid009_oddball_sequence_20230816_02doi.mkv',
                   'acid009_oddball_sequence_20230816bdoi', cameraParams)

videos.add_session('2023-08-16', 'doiFM_Down',
                   'acid009_oddball_sequence_20230816_03doi.mkv',
                   'acid009_oddball_sequence_20230816cdoi', cameraParams)
                   
videos.add_session('2023-08-16', 'doiFM_Up',
                   'acid009_oddball_sequence_20230816_04doi.mkv',
                   'acid009_oddball_sequence_20230816ddoi', cameraParams)                   

#DOI Spontaneous                   
videos.add_session('2023-08-16', 'doiSpontaneous',
                   'acid009_20230816_doiSpontaneous.mkv','', cameraParams)                                                                                                                                                                                                           
