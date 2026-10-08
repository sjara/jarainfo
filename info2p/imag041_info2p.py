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


subject = 'imag041'
sessions = []

newSession = {'subject':subject, 'date':'20261008','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 175.87, 'angle': 44.10,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 175.87, 'angle': 44.10,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 175.87, 'angle': 44.10,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 175.87, 'angle': 44.10,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '004', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 112.86, 'angle': 44.10,
              'laserPower': 38,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '005', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 112.86, 'angle': 44.10,
              'laserPower': 38,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '006', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 112.86, 'angle': 44.10,
              'laserPower': 38,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '007', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 112.86, 'angle': 44.10,
              'laserPower': 38,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '008', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '009', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '010', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '011', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '012', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '013', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '014', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 46,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '015', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 55,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '016', 'FOV#':4,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 36,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

























