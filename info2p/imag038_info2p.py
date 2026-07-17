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


subject = 'imag038'
sessions = []

newSession = {'subject':subject, 'date':'20260716', 'session': '000',
              'fps': 9.96, 'magnification': 2.0, 'depth': 138.08, 'angle': 42.57,
              'laserPower': 45, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_medFreq', 'sessionLabel': 'AMfading', 
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260716', 'session': '001',
              'fps': 9.96, 'magnification': 3.4, 'depth': 215.85, 'angle': 42.57,
              'laserPower': 54, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_medFreq', 'sessionLabel': 'AMfading', 
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260716', 'session': '002',
              'fps': 9.96, 'magnification': 2.0, 'depth': 152.36, 'angle': 42.57,
              'laserPower': 52, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A2_medFreq', 'sessionLabel': 'AMfading', 
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260716', 'session': '003',
              'fps': 9.96, 'magnification': 2.0, 'depth': 151.66, 'angle': 42.57,
              'laserPower': 47, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'AMfading', 
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260716', 'session': '004',
              'fps': 9.96, 'magnification': 2.0, 'depth': 151.66, 'angle': 42.57,
              'laserPower': 47, 'wavelength': 920, 'nFrames': 16000,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'natSounds', 
              'pmt': [0,1], 'paradigm':'natural_sound_detection'}
sessions.append(newSession)
#200 trials

newSession = {'subject':subject, 'date':'20260716', 'session': '005',
              'fps': 9.96, 'magnification': 2.0, 'depth': 151.66, 'angle': 42.57,
              'laserPower': 47, 'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260716', 'session': '006',
              'fps': 9.96, 'magnification': 2.0, 'depth': 151.66, 'angle': 42.57,
              'laserPower': 47, 'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials






