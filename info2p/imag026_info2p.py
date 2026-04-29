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


subject = 'imag026'
sessions = []


newSession = {'subject':subject, 'date':'20260403', 'session': '000',
              'fps': 15.49, 'magnification': 1.7, 'depth': 195.31, 'angle': 43.3,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 6630,
              'brainArea': 'A1', 'sessionLabel': 'tuningAM',
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '001',
              'fps': 15.49, 'magnification': 1.7, 'depth': 195.31, 'angle': 43.3,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 9573,
              'brainArea': 'A1', 'sessionLabel': 'tuningFreq', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '002',
              'fps': 15.49, 'magnification': 1.7, 'depth': 140.09, 'angle': 43.3,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 6630, 
              'brainArea': 'AUDv', 'sessionLabel': 'tuningAM', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '003',
              'fps': 15.49, 'magnification': 1.7, 'depth': 140.09, 'angle': 43.3,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 9573,
              'brainArea': 'AUDv', 'sessionLabel': 'tuningFreq', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '004',
              'fps': 15.49, 'magnification': 1.0, 'depth': 140.09, 'angle': 43.3,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 9573, 
              'brainArea': 'A1_AUDv', 'sessionLabel': 'spont',
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '005',
              'fps': 15.49, 'magnification': 1.7, 'depth': 145.2, 'angle': 43.3,
              'laserPower': 59, 'wavelength': 920, 'nFrames': 6630,
              'brainArea': 'AAF', 'sessionLabel': 'tuningAM', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260403', 'session': '006',
              'fps': 15.49, 'magnification': 1.7, 'depth': 145.2, 'angle': 43.3,
              'laserPower': 59, 'wavelength': 920, 'nFrames': 6630,
              'brainArea': 'AAF', 'sessionLabel': 'tuningFreq', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)



