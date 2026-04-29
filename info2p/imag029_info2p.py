"""
Metadata for two-photon imaging session

Each new session should include the following paramters:
subject: in standard jaralab format.
date: YYYYMMDD
session: 3-digit number incremented by Scanbox (as string)
fps: frame rate shown in Scanbox.
magnification: shown in Scanbox.
depth: in microns w.r.t. brain surface (calculated from knobby numbers)
angle: actual objective angle set (even if later it was zeroed).
laserPower: percentage shown by Scanbox.
wavelength: laser wavelength.
nFrames: total number of frames collected.
sessionLabel: arbitrary name for the type of session you recorded.
paradigm: name of taskontrol paradigm used during the session.

NOTE: when you save the stimulus/behavior data via the taskontrol paradigm
      make sure you name the file with the format: SUBJECT_PARADIGM_DATE_SESSION.h5
      For example: test000_am_tuning_20260401_001.h5
"""


subject = 'imag029'
sessions = []

newSession = {'subject':subject, 'date':'20260219', 'session': '000',
              'fps': 15.49, 'magnification': 1.0, 'depth': 610, 'angle': 43.39,
              'laserPower': 67, 'wavelength': 920, 'nFrames': 10000,
              'brainArea': 'A1', 'sessionLabel': 'spont', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260219', 'session': '001',
              'fps': 15.49, 'magnification': 1.0, 'depth': 610, 'angle': 43.39,
              'laserPower': 38, 'wavelength': 920, 'nFrames': 10000,
              'brainArea': 'A1', 'sessionLabel': 'spont', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260219', 'session': '002',
              'fps': 15.49, 'magnification': 1.0, 'depth': 610, 'angle': 43.39,
              'laserPower': 70, 'wavelength': 1040, 'nFrames': 2000,
              'brainArea': 'A1', 'sessionLabel': 'tdt_anat', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260219', 'session': '003',
              'fps': 15.49, 'magnification': 1.0, 'depth': 610, 'angle': 43.39,
              'laserPower': 38, 'wavelength': 920, 'nFrames': 7320,
              'brainArea': 'A1', 'sessionLabel': 'aborted_tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260219', 'session': '004',
              'fps': 15.49, 'magnification': 1.0, 'depth': 610, 'angle': 43.39,
              'laserPower': 65, 'wavelength': 1040, 'nFrames': 7320,
              'brainArea': 'A1', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '000',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 37.89,
              'laserPower': 49, 'wavelength': 920, 'nFrames': 6630,
              'brainArea': 'A1', 'sessionLabel': 'tuningAM', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '001',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 37.89,
              'laserPower': 49, 'wavelength': 920, 'nFrames': 9573,
              'brainArea': 'A1', 'sessionLabel': 'tuningFreq', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '002',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 37.89,
              'laserPower': 49, 'wavelength': 920, 'nFrames': 25235,
              'brainArea': 'A1', 'sessionLabel': 'naturalSounds', 
              'pmt': [0], 'paradigm':'natural_sound_detection'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '003',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 37.89,
              'laserPower': 49, 'wavelength': 920, 'nFrames': 9573,
              'brainArea': 'A1', 'sessionLabel': 'tuningFreqTrain', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '004',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 37.89,
              'laserPower': 67, 'wavelength': 920, 'nFrames': 1000,
              'brainArea': 'A1', 'sessionLabel': 'tdtAnat', 
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '005',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 37.89,
              'laserPower': 67, 'wavelength': 1040, 'nFrames': 1000,
              'brainArea': 'A1', 'sessionLabel': 'tdtAnat_zStack', 
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '000',
              'fps': 9.96, 'magnification': 1.0, 'depth': 375, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 1000,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'GCamp8m_anat', 
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '001',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 1040, 'nFrames': 1000,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'tdt_anat', 
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '002',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 980, 'nFrames': 1000,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'GCaMP8m_tdt_anat', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '003',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 6630,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'tuningAM', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '004',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 9573,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '005',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 9573,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'natSounds', 
              'pmt': [0], 'paradigm':'natural_sound_detection'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '006',                                                              ',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 1040, 'nFrames': 10,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'tdt_anat_zStack', 
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '007',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 1040, 'nFrames': 250,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'tdt_anat_zStack', 
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '000',
              'fps': 9.96, 'magnification': 1.0, 'depth': 200, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 2000,
              'brainArea': 'A1', 'sessionLabel': 'spont', 
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '001',
              'fps': 9.96, 'magnification': 4.0, 'depth': 200, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 2000,
              'brainArea': 'A1', 'sessionLabel': 'spont', 
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '002',
              'fps': 19.92, 'magnification': 1.0, 'depth': 200, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 4000,
              'brainArea': 'A1', 'sessionLabel': 'spont', 
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '003',
              'fps': 9.96, 'magnification': 1.0, 'depth': 200, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 4000,
              'brainArea': 'A1', 'sessionLabel': 'spont', 
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '004',
              'fps': 19.92, 'magnification': 1.0, 'depth': 500, 'angle': 43.3,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 18000,
              'brainArea': 'A1','sessionLabel': 'spont', 
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '005',
              'fps': 19.92, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 43, 'wavelength': 1040, 'nFrames': 4000,
              'brainArea': 'A1', 'sessionLabel': 'tdt_anat_zStack', 
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '006',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 43, 'wavelength': 1040, 'nFrames': 2000,
              'brainArea': 'A1', 'sessionLabel': 'tdt_anat_zStack',
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '007',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 28, 'wavelength': 920, 'nFrames': 2000,
              'brainArea': 'A1', 'sessionLabel': 'GCaMP8m_anat_zStack',
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '008',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 39, 'wavelength': 920, 'nFrames': 3000,
              'brainArea': 'A1', 'sessionLabel': 'GCaMP8m_anat', 
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '009',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 3000,
              'brainArea': 'A1', 'sessionLabel': 'GCaMP8m_tdt_anat', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260417', 'session': '000',
              'fps': 9.96, 'magnification': 1.0, 'depth': 146, 'angle': 42.73,
              'laserPower': 34, 'wavelength': 920, 'nFrames': 3000,
              'brainArea': 'A1_lowFreq','sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260424', 'session': '000',
              'fps': 19.96, 'magnification': 1.0, 'depth': 171.02, 'angle': 41.53,
              'laserPower': 25, 'wavelength': 920, 'nFrames': 12230,
              'brainArea': 'A1_medFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260424', 'session': '001',
              'fps': 9.96, 'magnification': 1.0, 'depth': 171.02, 'angle': 41.53,
              'laserPower': 25, 'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_medFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260424', 'session': '002',
              'fps': 9.96, 'magnification': 1.0, 'depth': 171.02, 'angle': 41.53,
              'laserPower': 25, 'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_medFreq', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260424', 'session': '003',
              'fps': 9.96, 'magnification': 1.0, 'depth': 171.02, 'angle': 41.53,
              'laserPower': 38, 'wavelength': 920, 'nFrames': 500,
              'brainArea': 'A1_medFreq', 'sessionLabel': 'tdt_anat', 
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260424', 'session': '004',
              'fps': 9.96, 'magnification': 1.0, 'depth': 502.74, 'angle': 41.53,
              'laserPower': 60, 'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_medFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260424', 'session': '005',
              'fps': 9.96, 'magnification': 1.0, 'depth': 502.74, 'angle': 41.53,
              'laserPower': 60, 'wavelength': 920, 'nFrames': 8526,
              'brainArea': 'A1_medFreq', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260424', 'session': '006',
              'fps': 9.96, 'magnification': 2.4, 'depth': 466.55, 'angle': 41.53,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 8526,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260424', 'session': '007',
              'fps': 9.96, 'magnification': 2.4, 'depth': 466.55, 'angle': 41.53,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)


newSession = {'subject':subject, 'date':'20260424', 'session': '008',
              'fps': 9.96, 'magnification': 2.4, 'depth': 438.81, 'angle': 41.53,
              'laserPower': 64, 'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AUDd', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)


