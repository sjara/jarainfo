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


subject = 'imag029'
sessions = []


newSession = {'subject':subject, 'date':'20260227', 'session': '000',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 1000, 
              'sessionLabel': 'green_anat', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '001',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 1040, 'nFrames': 1000, 
              'sessionLabel': 'red_anat', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '002',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 980, 'nFrames': 1000, 
              'sessionLabel': 'combined_anat', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '003',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 6630, 
              'sessionLabel': 'tuningAM', 'paradigm':'tuningAM'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '004',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 9573, 
              'sessionLabel': 'tuningFreq', 'paradigm':'tuningAFreq'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '004',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 9573, 
              'sessionLabel': 'tuningFreq', 'paradigm':'tuningFreq'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '005',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 9573, 
              'sessionLabel': 'natSounds', 'paradigm':'natSounds'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '005',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 1040, 'nFrames': 10, 
              'sessionLabel': 'red_anat_zStack', 'paradigm':'natSounds'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260227', 'session': '005',
              'fps': 15.49, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 1040, 'nFrames': 250, 
              'sessionLabel': 'red_anat_zStack', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '000',
              'fps': 9.96, 'magnification': 1.0, 'depth': 200, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 2000, 
              'sessionLabel': 'green_lowMag_unidir_test', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '001',
              'fps': 9.96, 'magnification': 4.0, 'depth': 200, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 2000, 
              'sessionLabel': 'green_highMag_unidir_test', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '002',
              'fps': 19.92, 'magnification': 1.0, 'depth': 200, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 4000, 
              'sessionLabel': 'green_lowMag_bidir_test', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '003',
              'fps': 9.96, 'magnification': 1.0, 'depth': 200, 'angle': 42.93,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 4000, 
              'sessionLabel': 'green_lowMag_unidir_test', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '004',
              'fps': 19.92, 'magnification': 1.0, 'depth': 500, 'angle': 43.3,
              'laserPower': 65, 'wavelength': 920, 'nFrames': 18000, 
              'sessionLabel': 'green_L5_spont_test_long', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '005',
              'fps': 19.92, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 43, 'wavelength': 1040, 'nFrames': 4000, 
              'sessionLabel': 'red_zStack_center_single_frame', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '006',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 43, 'wavelength': 1040, 'nFrames': 2000, 
              'sessionLabel': 'red_zStack_-80_to_80_step_10.7', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '007',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 28, 'wavelength': 920, 'nFrames': 2000, 
              'sessionLabel': 'green_zStack_-80_to_80_step_10.7', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '008',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 39, 'wavelength': 920, 'nFrames': 3000, 
              'sessionLabel': 'green_zStack_center_single_frame', 'paradigm':'none'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260402', 'session': '009',
              'fps': 9.96, 'magnification': 1.0, 'depth': 500, 'angle': 42.93,
              'laserPower': 43, 'wavelength': 920, 'nFrames': 3000, 
              'sessionLabel': 'green_zStack_center_single_frame_save_PMT0_and_1', 'paradigm':'none'}
sessions.append(newSession)

