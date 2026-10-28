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
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_45dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 175.87, 'angle': 44.10,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_55dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 175.87, 'angle': 44.10,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_65dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 175.87, 'angle': 44.10,
              'laserPower': 33,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '004', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 112.86, 'angle': 44.10,
              'laserPower': 38,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_45dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '005', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 112.86, 'angle': 44.10,
              'laserPower': 38,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_55dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '006', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 112.86, 'angle': 44.10,
              'laserPower': 38,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_65dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '007', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 112.86, 'angle': 44.10,
              'laserPower': 38,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '008', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_45dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '009', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_55dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '010', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_65dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '011', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '012', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_45dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '013', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 43,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_55dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '014', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 46,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_65dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

#image was getting dim, so added ultrasound gel to column without removing objective. image was improved.

newSession = {'subject':subject, 'date':'20261008','session': '015', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 55,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261008','session': '016', 'FOV#':4,
              'fps': 9.96, 'magnification': 2.0, 'depth': 160.55, 'angle': 44.10,
              'laserPower': 36,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261015','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.88, 'angle': 44.08,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_45dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#behavior not SAVED! did not complete behavior! FAIL!
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds

newSession = {'subject':subject, 'date':'20261015','session': '001', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.88, 'angle': 44.08,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_55dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#start at around 10:20 am. plan to put new gel in around 12:30 pm (every two hours is good)

newSession = {'subject':subject, 'date':'20261015','session': '002', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.88, 'angle': 44.08,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_45dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#redo of 000, which failed
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#pyscanbox failed after save, had to be restarted. abort button was still live at fail/hang.

newSession = {'subject':subject, 'date':'20261015','session': '003', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.88, 'angle': 44.08,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_65dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#quadrature and position streaming accidentaly off

newSession = {'subject':subject, 'date':'20261015','session': '004', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.88, 'angle': 44.08,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds
#quadrature and position streaming back on

newSession = {'subject':subject, 'date':'20261015','session': '005', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.88, 'angle': 44.08,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds_frange_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#4kHz center freq

newSession = {'subject':subject, 'date':'20261015','session': '006', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.88, 'angle': 44.08,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'band_noise_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#300 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#4kHz center freq

newSession = {'subject':subject, 'date':'20261015','session': '007', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.88, 'angle': 44.08,
              'laserPower': 35,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'noise_pair_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#4kHz center freq
#replaced gel after this recording at around 12:50 pm

newSession = {'subject':subject, 'date':'20261015','session': '008', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 138.4, 'angle': 44.09,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'pure_tones_65dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#4kHz center freq

newSession = {'subject':subject, 'date':'20261015','session': '009', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 138.4, 'angle': 44.09,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'fm_sounds_frange_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#6kHz center freq

newSession = {'subject':subject, 'date':'20261015','session': '010', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 138.4, 'angle': 44.09,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'band_noise_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#6kHz center freq

newSession = {'subject':subject, 'date':'20261015','session': '011', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 138.4, 'angle': 44.09,
              'laserPower': 32,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_midFreq', 'sessionLabel': 'noise_pair_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#6kHz center freq

newSession = {'subject':subject, 'date':'20261015','session': '012', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 143.43, 'angle': 44.09,
              'laserPower': 28,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_45dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#45 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair

newSession = {'subject':subject, 'date':'20261015','session': '013', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 143.43, 'angle': 44.09,
              'laserPower': 28,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_55dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#55 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair

newSession = {'subject':subject, 'date':'20261015','session': '014', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 143.43, 'angle': 44.09,
              'laserPower': 28,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_65dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#65 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair

newSession = {'subject':subject, 'date':'20261015','session': '015', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 143.43, 'angle': 44.09,
              'laserPower': 28,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair

newSession = {'subject':subject, 'date':'20261015','session': '016', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 143.43, 'angle': 44.09,
              'laserPower': 28,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'fm_sounds_frange_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#8kHz center freq

newSession = {'subject':subject, 'date':'20261015','session': '017', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 143.43, 'angle': 44.09,
              'laserPower': 28,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'band_noise_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#8kHz center freq

newSession = {'subject':subject, 'date':'20261015','session': '018', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 143.43, 'angle': 44.09,
              'laserPower': 28,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'noise_pair_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#8kHz center freq

newSession = {'subject':subject, 'date':'20261022','session': '000', 'FOV#':0,
              'fps': 9.96, 'magnification': 2.0, 'depth': 162.31, 'angle': 44.1,
              'laserPower': 26,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_70dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session time around 11:05 am, duration 12min38s

newSession = {'subject':subject, 'date':'20261022','session': '001', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 165.62, 'angle': 44.1,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session duration 12min38s

newSession = {'subject':subject, 'date':'20261022','session': '002', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 165.62, 'angle': 44.1,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'pure_tones_70dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session duration 12min38s

newSession = {'subject':subject, 'date':'20261022','session': '003', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 165.62, 'angle': 44.1,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#8kHz center freq

newSession = {'subject':subject, 'date':'20261022','session': '004', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 165.62, 'angle': 44.1,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#8kHz center freq

newSession = {'subject':subject, 'date':'20261022','session': '005', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 165.62, 'angle': 44.1,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'noise_pair_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#8kHz center freq

newSession = {'subject':subject, 'date':'20261022','session': '006', 'FOV#':1,
              'fps': 9.96, 'magnification': 2.0, 'depth': 165.62, 'angle': 44.1,
              'laserPower': 30,'wavelength': 920, 'nFrames': 5900,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'chord_tones_70dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#250 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=5900
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#8kHz F0, 5 possible middle, irrational

newSession = {'subject':subject, 'date':'20261022','session': '007', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.79, 'angle': 44.11,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session duration 12min38s

newSession = {'subject':subject, 'date':'20261022','session': '008', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.79, 'angle': 44.11,
              'laserPower': 30,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_lowFreq', 'sessionLabel': 'fm_sounds_frange_70dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#8kHz center freq

newSession = {'subject':subject, 'date':'20261022','session': '009', 'FOV#':2,
              'fps': 9.96, 'magnification': 2.0, 'depth': 135.79, 'angle': 44.11,
              'laserPower': 30,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_70dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session time around 2:19pm, duration 12min38s

newSession = {'subject':subject, 'date':'20261022','session': '010', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 147.94, 'angle': 44.11,
              'laserPower': 31,'wavelength': 920, 'nFrames': 7550,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'pure_tones_75dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#320 trials
#75 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=7550
#session time around 2:48pm, duration 12min38s

newSession = {'subject':subject, 'date':'20261022','session': '011', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 147.94, 'angle': 44.1,
              'laserPower': 31,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'band_noise_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#20kHz center freq
#Aborted, was running at 60 dB SPL, but should have been 70 dB SPL. Repeated at 70 dB SPL in next session.

newSession = {'subject':subject, 'date':'20261022','session': '012', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 147.94, 'angle': 44.1,
              'laserPower': 31,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'band_noise_70dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#70 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#20kHz center freq

newSession = {'subject':subject, 'date':'20261022','session': '013', 'FOV#':3,
              'fps': 9.96, 'magnification': 2.0, 'depth': 147.94, 'angle': 44.1,
              'laserPower': 31,'wavelength': 920, 'nFrames': 8260,
              'brainArea': 'A1_highFreq', 'sessionLabel': 'noise_pair_60dB',
              'pmt': [0], 'paradigm':'sound_tuning'}
sessions.append(newSession)
#350 trials
#60 dB SPL
#total frames = scan rate * #trials * (stim_dur + isi_mean)*1.128=8260
#new sound tuning paradigm w/ chords, fm sounds (dur and range), band noise, fading noise, and noise pair
#20kHz center freq
#session time around 3:26 pm









