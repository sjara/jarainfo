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


subject = 'imag044'
sessions = []



newSession = {'subject':subject, 'date':'20261120','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 201.25, 'angle': 42.76,
              'laserPower': 35,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF mode 3.9 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 9:46 am

newSession = {'subject':subject, 'date':'20261120','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 201.25, 'angle': 42.76,
              'laserPower': 35,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 3900 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 10:15 am

newSession = {'subject':subject, 'date':'20261120','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 201.25, 'angle': 42.76,
              'laserPower': 35,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 3900 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 10:30 am

newSession = {'subject':subject, 'date':'20261120','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 201.25, 'angle': 42.76,
              'laserPower': 35,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#F0 3900 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 10:42 am

newSession = {'subject':subject, 'date':'20261120','session': '004', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 201.25, 'angle': 42.76,
              'laserPower': 35,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 10:55 am
#8 kHz center, 6 octave range

newSession = {'subject':subject, 'date':'20261120','session': '005', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 201.25, 'angle': 42.76,
              'laserPower': 35,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'am_noise_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 11:14 am

newSession = {'subject':subject, 'date':'20261120','session': '006', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 201.25, 'angle': 42.76,
              'laserPower': 35,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fading_noise_45_75dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#45 to 75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:26 am

newSession = {'subject':subject, 'date':'20261124','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.18, 'angle': 42.77,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF mode 8 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 2:22 pm

newSession = {'subject':subject, 'date':'20261124','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.18, 'angle': 42.77,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'band_noise_67dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#67 dB SPL
#center freq 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 2:51 pm

newSession = {'subject':subject, 'date':'20261124','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.18, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 3:07 pm

newSession = {'subject':subject, 'date':'20261124','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.18, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'chord_tones_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#F0 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 3:26 pm

newSession = {'subject':subject, 'date':'20261124','session': '004', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.18, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'AAF_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 3:36 pm
#8 kHz center, 6 octave range

newSession = {'subject':subject, 'date':'20261124','session': '005', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.18, 'angle': 42.77,
              'laserPower': 33,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'am_noise_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 3:51 pm

newSession = {'subject':subject, 'date':'20261124','session': '006', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 164.18, 'angle': 42.77,
              'laserPower': 34,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fading_noise_45_75dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#45 to 75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 4:01 pm

newSession = {'subject':subject, 'date':'20261125','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF modes 4446 Hz and 9884 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 10:29 am

newSession = {'subject':subject, 'date':'20261125','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#ABORTED - wrong center freq

newSession = {'subject':subject, 'date':'20261125','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'band_noise_67dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#67 dB SPL
#center freq 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#ABORTED - wrong dB SPL

newSession = {'subject':subject, 'date':'20261125','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 4446 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:00 am

newSession = {'subject':subject, 'date':'20261125','session': '004', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 4446 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#ABORTED. sound_tuning.py crashed

newSession = {'subject':subject, 'date':'20261125','session': '005', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 4446 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:14 am

newSession = {'subject':subject, 'date':'20261125','session': '006', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'chord_tones_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#F0 4446 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 11:32 am

newSession = {'subject':subject, 'date':'20261125','session': '007', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 9884 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:42 am

newSession = {'subject':subject, 'date':'20261125','session': '008', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'noise_pair_62dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#62 dB SPL
#center freq 9884 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 11:56 am

newSession = {'subject':subject, 'date':'20261125','session': '009', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 32,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'chord_tones_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#F0 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 12:18 pm

newSession = {'subject':subject, 'date':'20261125','session': '010', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 33,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 12:28 pm

newSession = {'subject':subject, 'date':'20261125','session': '011', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 34,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'am_noise_68dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#68 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#session start at 12:42 pm

newSession = {'subject':subject, 'date':'20261125','session': '012', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 193.61, 'angle': 42.77,
              'laserPower': 34,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'fading_noise_45_75dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#45 to 75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 12:53 pm

newSession = {'subject':subject, 'date':'20261125','session': '013', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 401.23, 'angle': 42.77,
              'laserPower': 85,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF modes 
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 1:10 pm
#only 6 cells detected in BF quick check, so moved superficial for FOV2

newSession = {'subject':subject, 'date':'20261125','session': '014', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 335.04, 'angle': 42.77,
              'laserPower': 71,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'pure_tones_72dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#72 dB SPL
#BF mode 8 kHz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session start at 1:34 pm

newSession = {'subject':subject, 'date':'20261125','session': '015', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 335.04, 'angle': 42.77,
              'laserPower': 75,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A2_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0,1], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#center freq 8000 Hz
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#session start at 2:13 pm

