'''
Information about videos.
'''

from jaratoolbox import videoinfo

        
subject = 'pure013'
videos = videoinfo.Videos(subject)
cameraParams = videoinfo.cameraParams['IR_webcam_640x480_30fps_VP9']

videos.add_session('2022-06-24', 'lowestfirst6chord',
                   'pure013_detectiongonogo_20220624a_lowestfirst6chord.mkv',
                   'pure013_detectiongonogo_20220624a.h5',
                   cameraParams)
                   
videos.add_session('2022-07-01', 'highestfirst6chord',
                   'pure013_detectiongonogo_20220701a_highestfirst6chord.mkv',
                   'pure013_detectiongonogo_20220701a.h5',
                   cameraParams)                   

videos.add_session('2022-08-16', 'AMpreExtreme3rate',
                   'pure013_detectiongonogo_20220816a_AMpreExtreme3rate.mkv',
                   'pure013_detectiongonogo_20220816a.h5',
                   cameraParams)                     
                   
videos.add_session('2022-08-18', 'pureTone20sec',
                   'pure013_am_tuning_curve_20220818a_pureTone20sec.mkv',
                   'pure013_am_tuning_curve_20220818a.h5',
                   cameraParams)

videos.add_session('2022-08-19', 'AM20sec',
                   'pure013_am_tuning_curve_20220819a_AM20sec.mkv',
                   'pure013_am_tuning_curve_20220819a.h5',
                   cameraParams)  
                   
videos.add_session('2022-08-23', 'AM20secControl',
                   'pure013_am_tuning_curve_20220823a_AM20secControl.mkv',
                   'pure013_am_tuning_curve_20220823a.h5',
                   cameraParams)                                     
                  
videos.add_session('2022-08-31', 'AM4sec10off',
                   'pure013_am_tuning_curve_20220831a_AM4sec10off.mkv',
                   'pure013_am_tuning_curve_20220831a.h5',
                   cameraParams)   
                   
videos.add_session('2022-09-06', 'AM4sec10off',
                   'pure013_am_tuning_curve_20220906a_AM4sec10off.mkv',
                   'pure013_am_tuning_curve_20220906a.h5',
                   cameraParams)                                      
