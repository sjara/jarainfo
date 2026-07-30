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


from requests import session


subject = 'imag039'
sessions = []

newSession = {'subject':subject, 'date':'20260717', 'session': '000',
              'fps': 9.96, 'magnification': 2.0, 'depth': 147.92, 'angle': 42.34,
              'laserPower': 27, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'AMfading', 
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '001',
              'fps': 9.96, 'magnification': 2.0, 'depth': 159.8, 'angle': 42.34,
              'laserPower': 27, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'AMfading', 
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '002',
              'fps': 9.96, 'magnification': 2.0, 'depth': 159.8, 'angle': 42.34,
              'laserPower': 27, 'wavelength': 920, 'nFrames': 6615,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '003',
              'fps': 9.96, 'magnification': 2.0, 'depth': 159.8, 'angle': 42.34,
              'laserPower': 27, 'wavelength': 920, 'nFrames': 6615,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '004',
              'fps': 9.96, 'magnification': 2.0, 'depth': 159.8, 'angle': 42.34,
              'laserPower': 27, 'wavelength': 920, 'nFrames': 6615,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'natSounds', 
              'pmt': [0,1], 'paradigm':'natural_sound_detection'}
sessions.append(newSession)
#200 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '005',
              'fps': 9.96, 'magnification': 2.0, 'depth': 455.53, 'angle': 42.34,
              'laserPower': 88, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'AMfading', 
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '006',
              'fps': 9.96, 'magnification': 2.0, 'depth': 455.53, 'angle': 42.34,
              'laserPower': 88, 'wavelength': 920, 'nFrames': 6615,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'tuningFreq', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '007',
              'fps': 9.96, 'magnification': 2.0, 'depth': 455.53, 'angle': 42.34,
              'laserPower': 90, 'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'tuningAM', 
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '008',
              'fps': 9.96, 'magnification': 2.0, 'depth': 455.53, 'angle': 42.34,
              'laserPower': 90, 'wavelength': 920, 'nFrames': 16000,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'natSounds', 
              'pmt': [0,1], 'paradigm':'natural_sound_detection'}
sessions.append(newSession)
#200 trials

newSession = {'subject':subject, 'date':'20260717', 'session': '009',
              'fps': 9.96, 'magnification': 1.0, 'depth': 184.35, 'angle': 42.34,
              'laserPower': 37, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'AMfading', 
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '000',
              'fps': 9.96, 'magnification': 2.0, 'depth': 200.4,'angle': 42.00,
              'laserPower': 31, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '001',
              'fps': 9.96, 'magnification': 2.0, 'depth': 200.4,'angle': 42.00,
              'laserPower': 31, 'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '002',
              'fps': 9.96, 'magnification': 2.0, 'depth': 200.4,'angle': 42.00,
              'laserPower': 31, 'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260729','session': '003',
              'fps': 9.96, 'magnification': 2.0, 'depth': 439.97,'angle': 42.00,
              'laserPower': 85,'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '004',
              'fps': 9.96, 'magnification': 2.0, 'depth': 439.97, 'angle': 42.00,
              'laserPower': 85,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '005',
              'fps': 9.96, 'magnification': 2.0, 'depth': 439.97, 'angle': 42.00,
              'laserPower': 85,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260729','session': '006',
              'fps': 9.96, 'magnification': 2.0, 'depth': 350.25, 'angle': 42.00,
              'laserPower': 57,'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '007',
              'fps': 9.96, 'magnification': 2.0, 'depth': 350.25, 'angle': 42.00,
              'laserPower': 57,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '008',
              'fps': 9.96, 'magnification': 2.0, 'depth': 350.25, 'angle':42.00,
              'laserPower': 57,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260729','session': '009',
              'fps': 9.96, 'magnification': 2.0, 'depth': 178.85, 'angle': 42.00,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '010',
              'fps': 9.96, 'magnification': 2.0, 'depth': 178.85, 'angle': 42.00,
              'laserPower': 30,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '011',
              'fps': 9.96, 'magnification': 2.0, 'depth': 178.85, 'angle':42.00,
              'laserPower': 30,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260729','session': '012',
              'fps': 9.96, 'magnification': 2.0, 'depth': 443.29, 'angle': 42.00,
              'laserPower': 78,'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '013',
              'fps': 9.96, 'magnification': 2.0, 'depth': 443.29, 'angle': 42.00,
              'laserPower': 78,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '014',
              'fps': 9.96, 'magnification': 2.0, 'depth': 443.29, 'angle':42.00,
              'laserPower': 78,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260729','session': '015',
              'fps': 9.96, 'magnification': 2.0, 'depth': 179.82, 'angle': 42.00,
              'laserPower': 26,'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '016',
              'fps': 9.96, 'magnification': 2.0, 'depth': 179.82, 'angle': 42.00,
              'laserPower': 26,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '017',
              'fps': 9.96, 'magnification': 2.0, 'depth': 179.82, 'angle':42.00,
              'laserPower': 26,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260729','session': '018',
              'fps': 9.96, 'magnification': 2.0, 'depth': 438.59, 'angle': 42.00,
              'laserPower': 81,'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '019',
              'fps': 9.96, 'magnification': 2.0, 'depth': 438.59, 'angle': 42.00,
              'laserPower': 81,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '020',
              'fps': 9.96, 'magnification': 2.0, 'depth': 438.59, 'angle':42.00,
              'laserPower': 81,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260729','session': '021',
              'fps': 9.96, 'magnification': 2.0, 'depth': 181.05, 'angle': 42.00,
              'laserPower': 28,'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '022',
              'fps': 9.96, 'magnification': 2.0, 'depth': 181.05, 'angle': 42.00,
              'laserPower': 28,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '023',
              'fps': 9.96, 'magnification': 2.0, 'depth': 181.05, 'angle':42.00,
              'laserPower': 28,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260729','session': '024',
              'fps': 9.96, 'magnification': 2.0, 'depth': 434.68, 'angle': 42.00,
              'laserPower': 81,'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '025',
              'fps': 9.96, 'magnification': 2.0, 'depth': 434.68, 'angle': 42.00,
              'laserPower': 81,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260729','session': '026',
              'fps': 9.96, 'magnification': 2.0, 'depth': 434.68, 'angle':42.00,
              'laserPower': 81,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials



















