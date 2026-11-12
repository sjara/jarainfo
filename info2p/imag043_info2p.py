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

newSession = {'subject':subject, 'date':'20261110','session': '004', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 34,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 6629 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:55 am

newSession = {'subject':subject, 'date':'20261110','session': '005', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 35,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#70 dB SPL
#center freq 3641 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 12:10 pm

newSession = {'subject':subject, 'date':'20261110','session': '006', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 35,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#70 dB SPL
#F0 6629 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 12:26 pm

newSession = {'subject':subject, 'date':'20261110','session': '007', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 35,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 12:41 pm

newSession = {'subject':subject, 'date':'20261110','session': '008', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 37,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'am_noise_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 12:55 pm

newSession = {'subject':subject, 'date':'20261110','session': '009', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 167.65, 'angle': 42.26,
              'laserPower': 37,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fading_noise_45_75dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#45 to 75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 1:09 pm

#removed gel, cleaned objective and window, and reapplied gel

newSession = {'subject':subject, 'date':'20261110','session': '010', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 188.55, 'angle': 42.26,
              'laserPower': 35,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones_71_4dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#71.4 dB SPL
#BF mode 
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 1:32 pm

#too high freq and too few cells in FOV1, so moved a bit anterior and ventral to FOV2

newSession = {'subject':subject, 'date':'20261110','session': '011', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 144.32, 'angle': 42.26,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF mode 8260 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 2:11 pm

newSession = {'subject':subject, 'date':'20261110','session': '012', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 144.32, 'angle': 42.26,
              'laserPower': 33,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 8094 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 2:39 pm

newSession = {'subject':subject, 'date':'20261110','session': '013', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 144.32, 'angle': 42.26,
              'laserPower': 33,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 8094 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 2:54 pm

newSession = {'subject':subject, 'date':'20261110','session': '014', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 144.32, 'angle': 42.26,
              'laserPower': 33,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#70 dB SPL
#F0 8094 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 3:09 pm

newSession = {'subject':subject, 'date':'20261110','session': '015', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 144.32, 'angle': 42.26,
              'laserPower': 33,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 3:24 pm

newSession = {'subject':subject, 'date':'20261110','session': '016', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 144.32, 'angle': 42.26,
              'laserPower': 34,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'am_noise_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 3:39 pm

newSession = {'subject':subject, 'date':'20261110','session': '017', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 144.32, 'angle': 42.26,
              'laserPower': 34,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'fading_noise_45_75dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#45 to 75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 3:50 pm

newSession = {'subject':subject, 'date':'20261112','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 406, 'angle': 42.25,
              'laserPower': 48,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF mode 9884 chords, 12740 noise pair and band noise
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 10:47 am

newSession = {'subject':subject, 'date':'20261112','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 406, 'angle': 42.25,
              'laserPower': 48,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 12740 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 

newSession = {'subject':subject, 'date':'20261112','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 406, 'angle': 42.25,
              'laserPower': 54,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 12740 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:39 am

#added gel but did not touch or move prep or objective, so FOV is unchanged

newSession = {'subject':subject, 'date':'20261112','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 406, 'angle': 42.25,
              'laserPower': 54,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#F0 9884 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 11:54 am

newSession = {'subject':subject, 'date':'20261110','session': '004', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 406, 'angle': 42.26,
              'laserPower': 54,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 12:07 pm

newSession = {'subject':subject, 'date':'20261112','session': '005', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 406, 'angle': 42.25,
              'laserPower': 54,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'am_noise_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 12:19 pm

newSession = {'subject':subject, 'date':'20261112','session': '006', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 406, 'angle': 42.25,
              'laserPower': 54,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fading_noise_45_75dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#45 to 75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 12:33 pm

newSession = {'subject':subject, 'date':'20261112','session': '007', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 340.64, 'angle': 42.25,
              'laserPower': 61,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF mode not enough cells
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 12:58 pm
#only 8 responsive cells, so decided to move to nearby area w/ more cells - toward mid freq AAF, slighly less deep

newSession = {'subject':subject, 'date':'20261112','session': '008', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 264.76, 'angle': 42.25,
              'laserPower': 50,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF mode 8000 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 1:28 pm

newSession = {'subject':subject, 'date':'20261112','session': '009', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 264.76, 'angle': 42.25,
              'laserPower': 50,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 1:53 pm

newSession = {'subject':subject, 'date':'20261112','session': '010', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 406, 'angle': 42.25,
              'laserPower': 51,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 2:09 pm









