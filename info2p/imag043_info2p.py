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


subject = 'imag043'
sessions = []



newSession = {'subject':subject, 'date':'20261110','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 32,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF modes 3641 and 6629 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 10:34 am

newSession = {'subject':subject, 'date':'20261110','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 3641 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:06 am

newSession = {'subject':subject, 'date':'20261110','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 6629 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:26 am

newSession = {'subject':subject, 'date':'20261110','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 34,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 3641 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:41 am































