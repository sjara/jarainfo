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


subject = 'imag025'
sessions = []


newSession = {'subject':subject, 'date':'20260403', 'session': '000',
              'fps': 9.96, 'magnification': 1.2, 'depth': 193.17, 'angle': 42.97,
              'laserPower': 36, 'wavelength': 920, 'nFrames': 4263, 
              'sessionLabel': 'AUD_all_tuningAM', 'paradigm':'tuningAM'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '001',
              'fps': 9.96, 'magnification': 1.2, 'depth': 193.17, 'angle': 42.97,
              'laserPower': 36, 'wavelength': 920, 'nFrames': 6115, 
              'sessionLabel': 'AUD_all_tuningFreq', 'paradigm':'tuningFreq'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '002',
              'fps': 9.96, 'magnification': 1.2, 'depth': 214.2, 'angle': 42.87,
              'laserPower': 40, 'wavelength': 920, 'nFrames': 4263, 
              'sessionLabel': 'AUDp_tuningAM', 'paradigm':'tuningAM'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '003',
              'fps': 9.96, 'magnification': 1.2, 'depth': 214.2, 'angle': 42.87,
              'laserPower': 40, 'wavelength': 920, 'nFrames': 6115, 
              'sessionLabel': 'AUDp_tuningFreq', 'paradigm':'tuningFreq'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '004',
              'fps': 9.96, 'magnification': 2.0, 'depth': 139.57, 'angle': 42.87,
              'laserPower': 45, 'wavelength': 920, 'nFrames': 4263, 
              'sessionLabel': 'AUDv_tuningAM', 'paradigm':'tuningAM'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '005',
              'fps': 9.96, 'magnification': 2.0, 'depth': 139.57, 'angle': 42.87,
              'laserPower': 45, 'wavelength': 920, 'nFrames': 4263, 
              'sessionLabel': 'AUDv_tuningFreq', 'paradigm':'tuningFreq'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '006',
              'fps': 9.96, 'magnification': 1.4, 'depth': 192.32, 'angle': 42.87,
              'laserPower': 50, 'wavelength': 920, 'nFrames': 4263, 
              'sessionLabel': 'AUDp_AAF_highFreq_tuningAM', 'paradigm':'tuningAM'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '007',
              'fps': 9.96, 'magnification': 1.4, 'depth': 192.32, 'angle': 42.87,
              'laserPower': 50, 'wavelength': 920, 'nFrames': 4263, 
              'sessionLabel': 'AUDp_AAF_highFreq_tuningFreq', 'paradigm':'tuningFreq'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '008',
              'fps': 9.96, 'magnification': 1.0, 'depth': 186.21, 'angle': 42.87,
              'laserPower': 47, 'wavelength': 920, 'nFrames': 17928, 
              'sessionLabel': 'AUDp_highFreq_spont', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '009',
              'fps': 19.92, 'magnification': 1.0, 'depth': 186.21, 'angle': 42.87,
              'laserPower': 47, 'wavelength': 920, 'nFrames': 35856, 
              'sessionLabel': 'AUDp_highFreq_spont', 'paradigm':'none'}
sessions.append(newSession)
# PMT0
# PMT1

newSession = {'subject':subject, 'date':'20260417', 'session': '000',
              'fps': 9.92, 'magnification': 1.4, 'depth': 179.91, 'angle': 44.77,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 6115, 
              'sessionLabel': 'AUDp_tuningFreq_green_red_ventLat', 'paradigm':'tuningFreq'}
sessions.append(newSession)
# PMT0, 1

newSession = {'subject':subject, 'date':'20260417', 'session': '001',
              'fps': 9.92, 'magnification': 1.4, 'depth': 179.91, 'angle': 44.77,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 6115, 
              'sessionLabel': 'AUDp_tuningFreq_green_ventLat', 'paradigm':'tuningFreq'}
sessions.append(newSession)
# PMT0

newSession = {'subject':subject, 'date':'20260417', 'session': '002',
              'fps': 9.92, 'magnification': 1.4, 'depth': 235.29, 'angle': 44.77,
              'laserPower': 42, 'wavelength': 920, 'nFrames': 6115, 
              'sessionLabel': 'AUDp_tuningFreq_green_antDors', 'paradigm':'tuningFreq'}
sessions.append(newSession)
# PMT0

newSession = {'subject':subject, 'date':'20260417', 'session': '003',
              'fps': 9.92, 'magnification': 1.4, 'depth': 235.29, 'angle': 44.77,
              'laserPower': 42, 'wavelength': 920, 'nFrames': 6115, 
              'sessionLabel': 'AUDp_tuningAM_green_antDors', 'paradigm':'tuningAM'}
sessions.append(newSession)
# PMT0

newSession = {'subject':subject, 'date':'20260417', 'session': '004',
              'fps': 9.92, 'magnification': 1.4, 'depth': 235.29, 'angle': 44.77,
              'laserPower': 42, 'wavelength': 920, 'nFrames': 6115, 
              'sessionLabel': 'AUDv_AAF_tuningFreq_green', 'paradigm':'tuningFreq'}
sessions.append(newSession)
# PMT0





