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

newSession = {'subject':subject, 'date':'20260730','session': '000',
              'fps': 9.96, 'magnification': 2.0, 'depth': 181.06,'angle': 42.02,
              'laserPower': 26, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '001',
              'fps': 9.96, 'magnification': 2.0, 'depth': 181.06, 'angle': 42.00,
              'laserPower': 26,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '002',
              'fps': 9.96, 'magnification': 2.0, 'depth': 181.06, 'angle':42.00,
              'laserPower': 26,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '003',
              'fps': 9.96, 'magnification': 2.0, 'depth': 415.51,'angle': 42.02,
              'laserPower': 70, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '004',
              'fps': 9.96, 'magnification': 2.0, 'depth': 415.51, 'angle': 42.00,
              'laserPower': 70,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '005',
              'fps': 9.96, 'magnification': 2.0, 'depth': 415.51, 'angle':42.00,
              'laserPower': 70,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '006',
              'fps': 9.96, 'magnification': 2.0, 'depth': 119.25,'angle': 42.02,
              'laserPower': 26, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '007',
              'fps': 9.96, 'magnification': 2.0, 'depth': 119.25, 'angle': 42.00,
              'laserPower': 26,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '008',
              'fps': 9.96, 'magnification': 2.0, 'depth': 119.25, 'angle':42.00,
              'laserPower': 26,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '009',
              'fps': 9.96, 'magnification': 2.0, 'depth': 429.39,'angle': 42.02,
              'laserPower': 81, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '010',
              'fps': 9.96, 'magnification': 2.0, 'depth': 429.39, 'angle': 42.00,
              'laserPower': 81,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '011',
              'fps': 9.96, 'magnification': 2.0, 'depth': 429.39, 'angle': 42.00,
              'laserPower': 81,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '012',
              'fps': 9.96, 'magnification': 2.0, 'depth': 155.85,'angle': 42.02,
              'laserPower': 23, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '013',
              'fps': 9.96, 'magnification': 2.0, 'depth': 155.85, 'angle': 42.02,
              'laserPower': 23,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '014',
              'fps': 9.96, 'magnification': 2.0, 'depth': 155.85, 'angle': 42.02,
              'laserPower': 23,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '015',
              'fps': 9.96, 'magnification': 2.0, 'depth': 475.76,'angle': 42.02,
              'laserPower': 73, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '016',
              'fps': 9.96, 'magnification': 2.0, 'depth': 475.76, 'angle': 42.02,
              'laserPower': 73,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '017',
              'fps': 9.96, 'magnification': 2.0, 'depth': 475.76, 'angle': 42.02,
              'laserPower': 73,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A2_highFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '018',
              'fps': 9.96, 'magnification': 2.0, 'depth': 162.17,'angle': 42.02,
              'laserPower': 27, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '019',
              'fps': 9.96, 'magnification': 2.0, 'depth': 162.17, 'angle': 42.02,
              'laserPower': 27,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '020',
              'fps': 9.96, 'magnification': 2.0, 'depth': 162.17, 'angle': 42.02,
              'laserPower': 29,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '021',
              'fps': 9.96, 'magnification': 2.0, 'depth': 448.29,'angle': 42.02,
              'laserPower': 78, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '022',
              'fps': 9.96, 'magnification': 2.0, 'depth': 448.29, 'angle': 42.02,
              'laserPower': 79,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '023',
              'fps': 9.96, 'magnification': 2.0, 'depth': 448.29, 'angle': 42.02,
              'laserPower': 79,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '024',
              'fps': 9.96, 'magnification': 2.0, 'depth': 170.44,'angle': 42.02,
              'laserPower': 29, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '025',
              'fps': 9.96, 'magnification': 2.0, 'depth': 170.44, 'angle': 42.02,
              'laserPower': 29,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '026',
              'fps': 9.96, 'magnification': 2.0, 'depth': 170.44, 'angle': 42.02,
              'laserPower': 29,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260730','session': '027',
              'fps': 9.96, 'magnification': 2.0, 'depth': 430.89,'angle': 42.02,
              'laserPower': 73, 'wavelength': 920, 'nFrames': 5500,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'AMfading',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '028',
              'fps': 9.96, 'magnification': 2.0, 'depth': 430.89, 'angle': 42.02,
              'laserPower': 73,'wavelength': 920, 'nFrames': 6115,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningFreq',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260730','session': '029',
              'fps': 9.96, 'magnification': 2.0, 'depth': 430.89, 'angle': 42.02,
              'laserPower': 73,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'tuningAM',
              'pmt': [0,1], 'paradigm':'am_tuning'}
sessions.append(newSession)
#220 trials

newSession = {'subject':subject, 'date':'20260910','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 171.75, 'angle': 42.02,
              'laserPower': 24,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260910','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 171.75, 'angle': 42.02,
              'laserPower': 24,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260910','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 171.75, 'angle': 42.02,
              'laserPower': 24,'wavelength': 920, 'nFrames': 7080,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#300 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7080
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260910','session': '003', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 147.77, 'angle': 42.02,
              'laserPower': 29,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260910','session': '004', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 147.77, 'angle': 42.02,
              'laserPower': 29,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials

newSession = {'subject':subject, 'date':'20260910','session': '005', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 147.77, 'angle': 42.02,
              'laserPower': 29,'wavelength': 920, 'nFrames': 7080,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'fm_sounds',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#300 trials

newSession = {'subject':subject, 'date':'20260910','session': '006', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 223.66, 'angle': 42.02,
              'laserPower': 28,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials

newSession = {'subject':subject, 'date':'20260910','session': '007', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 223.66, 'angle': 42.02,
              'laserPower': 31,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials

newSession = {'subject':subject, 'date':'20260910','session': '008', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 223.66, 'angle': 42.02,
              'laserPower': 32,'wavelength': 920, 'nFrames': 7080,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#300 trials
#note: prep moved down around half way through so actual new depth was around 300 micrometers

newSession = {'subject':subject, 'date':'20260910','session': '009', 'FOV#':4,
              'fps': 9.96, 'magnification': 2.0, 'depth': 223.66, 'angle': 42.02,
              'laserPower': 29,'wavelength': 920, 'nFrames': 7080,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#300 trials
#redo of 008 but at correct depth of 223.66 micrometers, matching 006 and 008.

newSession = {'subject':subject, 'date':'20260910','session': '010', 'FOV#':5,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.19, 'angle': 42.02,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7080,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#accidentally only ran 7080 fr, but all sound trials still finished nonetheless.

newSession = {'subject':subject, 'date':'20260910','session': '011', 'FOV#':5,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.19, 'angle': 42.02,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials

newSession = {'subject':subject, 'date':'20260910','session': '012', 'FOV#':5,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.19, 'angle': 42.02,
              'laserPower': 31,'wavelength': 920, 'nFrames': 7080,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'fm_sounds',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#300 trials

newSession = {'subject':subject, 'date':'20260924','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 150.55, 'angle': 41.91,
              'laserPower': 25,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 150.55, 'angle': 41.91,
              'laserPower': 25,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 150.55, 'angle': 41.91,
              'laserPower': 25,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20260924','session': '003', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 114.34, 'angle': 41.91,
              'laserPower': 26,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '004', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 114.34, 'angle': 41.91,
              'laserPower': 26,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '005', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 114.34, 'angle': 41.91,
              'laserPower': 26,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20260924','session': '006', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 154.38, 'angle': 41.91,
              'laserPower': 26,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '007', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 154.38, 'angle': 41.91,
              'laserPower': 26,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '008', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 154.38, 'angle': 41.91,
              'laserPower': 26,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20260924','session': '009', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 159.89, 'angle': 41.91,
              'laserPower': 29,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '010', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 159.89, 'angle': 41.91,
              'laserPower': 26,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '011', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 159.89, 'angle': 41.91,
              'laserPower': 26,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20260924','session': '012', 'FOV#':4,
              'fps': 9.96, 'magnification': 2.0, 'depth': 183.32, 'angle': 41.91,
              'laserPower': 29,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '013', 'FOV#':4,
              'fps': 9.96, 'magnification': 2.0, 'depth': 183.32, 'angle': 41.91,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '014', 'FOV#':4,
              'fps': 9.96, 'magnification': 2.0, 'depth': 183.32, 'angle': 41.91,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20260924','session': '015', 'FOV#':5,
              'fps': 9.96, 'magnification': 2.0, 'depth': 161.38, 'angle': 42.2,
              'laserPower': 26,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '016', 'FOV#':5,
              'fps': 9.96, 'magnification': 2.0, 'depth': 161.38, 'angle': 42.2,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '017', 'FOV#':5,
              'fps': 9.96, 'magnification': 2.0, 'depth': 161.38, 'angle': 42.2,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20260924','session': '018', 'FOV#':6,
              'fps': 9.96, 'magnification': 2.0, 'depth': 153.72, 'angle': 42.2,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '019', 'FOV#':6,
              'fps': 9.96, 'magnification': 2.0, 'depth': 153.72, 'angle': 42.2,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '020', 'FOV#':6,
              'fps': 9.96, 'magnification': 2.0, 'depth': 153.72, 'angle': 42.2,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_highFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20260924','session': '021', 'FOV#':7,
              'fps': 9.96, 'magnification': 2.0, 'depth': 161.47, 'angle': 42.2,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '022', 'FOV#':7,
              'fps': 9.96, 'magnification': 2.0, 'depth': 161.47, 'angle': 42.2,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '023', 'FOV#':7,
              'fps': 9.96, 'magnification': 2.0, 'depth': 161.47, 'angle': 42.2,
              'laserPower': 31,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20260924','session': '024', 'FOV#':8,
              'fps': 9.96, 'magnification': 2.0, 'depth': 129.45, 'angle': 42.2,
              'laserPower': 32,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20260924','session': '025', 'FOV#':8,
              'fps': 9.96, 'magnification': 2.0, 'depth': 129.45, 'angle': 42.2,
              'laserPower': 32,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=4kHz

newSession = {'subject':subject, 'date':'20260924','session': '026', 'FOV#':8,
              'fps': 9.96, 'magnification': 2.0, 'depth': 129.45, 'angle': 42.2,
              'laserPower': 32,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#new sound tuning paradigm w/ chords, fm sounds
#chord Fo=6.5kHz

newSession = {'subject':subject, 'date':'20261029','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.37, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_73dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#73 dB SPL
#BF mode 5.43 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#session start at 10:50 am

newSession = {'subject':subject, 'date':'20261029','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.37, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'band_noise_65dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#65 dB SPL
#center freq 5.43 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:25 am

newSession = {'subject':subject, 'date':'20261029','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.37, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'noise_pair_60dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:45 am
#some "fading" observed, added gel around objective but did not move prep or objective.

newSession = {'subject':subject, 'date':'20261029','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.37, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 12:01 pm

newSession = {'subject':subject, 'date':'20261029','session': '004', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.37, 'angle': 42.19,
              'laserPower': 33,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#8 kHz center, 6 oct range, 1-64 kHz
#session start at 12:16 pm

newSession = {'subject':subject, 'date':'20261029','session': '005', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.37, 'angle': 42.19,
              'laserPower': 33,'wavelength': 920, 'nFrames': 4263,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'am_noise_65dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#220 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=4263
#session start at 12:31 pm
#run with only 4 rates between 4-32 Hz mistakenly. will rerun with 11 rates 4-128 Hz

newSession = {'subject':subject, 'date':'20261029','session': '006', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.37, 'angle': 42.19,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7500,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fading_noise_45_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45-68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7500
#session start at 12:41 pm

newSession = {'subject':subject, 'date':'20261029','session': '007', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.37, 'angle': 42.19,
              'laserPower': 33,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'am_noise_65dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#220 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 12:55 pm
#use this session as replacement of session 005, FOV0, which was run with too few AM levels and too small an AM range.

newSession = {'subject':subject, 'date':'20261029','session': '008', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.49, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones_73dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#73 dB SPL
#BF mode 8.09 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 1:16 pm

newSession = {'subject':subject, 'date':'20261029','session': '009', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.49, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'band_noise_65dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#65 dB SPL
#center freq 8.09 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 1:51 pm

newSession = {'subject':subject, 'date':'20261029','session': '010', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.49, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'noise_pair_60dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#center freq 8.09 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 2:05 pm

newSession = {'subject':subject, 'date':'20261029','session': '011', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.49, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#Fo 8.09 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 2:20 pm

newSession = {'subject':subject, 'date':'20261029','session': '012', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.49, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 2:38 pm

newSession = {'subject':subject, 'date':'20261029','session': '013', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.49, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'am_noise_65dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 2:52 pm

newSession = {'subject':subject, 'date':'20261029','session': '014', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 131.49, 'angle': 42.19,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'fading_noise_45_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45-68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 3:02 pm

newSession = {'subject':subject, 'date':'20261029','session': '015', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 431.38, 'angle': 42.19,
              'laserPower': 76,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones_73dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#73 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 3:23 pm
#2p/behav alignment fail from opening sound_tuning.py after 2p imaging started. This created a fake event.
















































