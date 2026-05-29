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


subject = 'imag030'
sessions = []

newSession = {'subject':subject, 'date':'20260507', 'session': '000',
              'fps': 9.96, 'magnification': 1.0, 'depth': 610, 'angle': 43.39,
              'laserPower': 30, 'wavelength': 920, 'nFrames': 10000,
              'brainArea': 'A1', 'sessionLabel': 'spont', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260529', 'session': '000',
              'fps': 9.96, 'magnification': 2.8, 'depth': 206.55, 'angle': 40.18,
              'laserPower': 48, 'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A2', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260529', 'session': '001',
              'fps': 9.96, 'magnification': 2.8, 'depth': 206.55, 'angle': 40.18,
              'laserPower': 48, 'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A2', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260529', 'session': '002',
              'fps': 9.96, 'magnification': 2.8, 'depth': 206.55, 'angle': 40.18,
              'laserPower': 48, 'wavelength': 920, 'nFrames': 16000,
              'brainArea': 'A2', 'sessionLabel': 'natSounds', 
              'pmt': [0,1], 'paradigm':'natural_sound_detection'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260529', 'session': '003',
              'fps': 9.96, 'magnification': 2.4, 'depth': 311.47, 'angle': 40.32,
              'laserPower': 57, 'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260529', 'session': '004',
              'fps': 9.96, 'magnification': 2.4, 'depth': 311.47, 'angle': 40.32,
              'laserPower': 57, 'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260529', 'session': '005',
              'fps': 9.96, 'magnification': 2.4, 'depth': 311.47, 'angle': 40.32,
              'laserPower': 57, 'wavelength': 920, 'nFrames': 16000,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'natSounds', 
              'pmt': [0,1], 'paradigm':'natural_sound_detection'}
sessions.append(newSession)





