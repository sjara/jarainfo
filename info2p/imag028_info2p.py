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


subject = 'imag028'
sessions = []

newSession = {'subject':subject, 'date':'20260220', 'session': '000',
              'fps': 15.49, 'magnification': 1.0, 'depth': 450, 'angle': 35.37,
              'laserPower': 90, 'wavelength': 920, 'nFrames': 1000,
              'brainArea': 'A1', 'sessionLabel': 'spont', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '001',
              'fps': 15.49, 'magnification': 1.0, 'depth': 450, 'angle': 35.37,
              'laserPower': 90, 'wavelength': 1040, 'nFrames': 1000,
              'brainArea': 'A1', 'sessionLabel': 'tdt_anat', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '002',
              'fps': 15.49, 'magnification': 1.0, 'depth': 450, 'angle': 35.37,
              'laserPower': 90, 'wavelength': 920, 'nFrames': 6630,
              'brainArea': 'A1', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '003',
              'fps': 15.49, 'magnification': 1.0, 'depth': 450, 'angle': 35.37,
              'laserPower': 90, 'wavelength': 920, 'nFrames': 9573,
              'brainArea': 'A1', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '004',
              'fps': 15.49, 'magnification': 1.0, 'depth': 450, 'angle': 35.37,
              'laserPower': 90, 'wavelength': 1040, 'nFrames': 23235,
              'brainArea': 'A1', 'sessionLabel': 'naturalSounds', 
              'pmt': [0,1], 'paradigm':'natural_sound_detection'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260220', 'session': '005',
              'fps': 15.49, 'magnification': 1.0, 'depth': 325, 'angle': 35.37,
              'laserPower': 90, 'wavelength': 1040, 'nFrames': 1000,
              'brainArea': 'A1', 'sessionLabel': 'tdt_anat_zStack', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '000',
              'fps': 15.49, 'magnification': 1.0, 'depth': 250, 'angle': 35.37,
              'laserPower': 33, 'wavelength': 1040, 'nFrames': 1000,
              'brainArea': 'A1', 'sessionLabel': 'tdt_anat', 
              'pmt': [1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '001',
              'fps': 15.49, 'magnification': 1.0, 'depth': 250, 'angle': 35.37,
              'laserPower': 54, 'wavelength': 980, 'nFrames': 1000,
              'brainArea': 'A1', 'sessionLabel': 'GCaMP8m_tdt_anat', 
              'pmt': [0,1], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '002',
              'fps': 15.49, 'magnification': 1.0, 'depth': 250, 'angle': 35.37,
              'laserPower': 60, 'wavelength': 920, 'nFrames': 1000,
              'brainArea': 'A1', 'sessionLabel': 'GCaMP8m_anat', 
              'pmt': [0], 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '003',
              'fps': 15.49, 'magnification': 1.0, 'depth': 250, 'angle': 35.37,
              'laserPower': 60, 'wavelength': 920, 'nFrames': 6630,
              'brainArea': 'A1', 'sessionLabel': 'tuningAM', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '004',
              'fps': 15.49, 'magnification': 1.0, 'depth': 250, 'angle': 35.37,
              'laserPower': 60, 'wavelength': 920, 'nFrames': 9573,
              'brainArea': 'A1', 'sessionLabel': 'tuningFreq', 
              'pmt': [0], 'paradigm':'am_tuning'}
sessions.append(newSession)

