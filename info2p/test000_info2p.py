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
sessionLabel: short string describing the session.
brainArea: aproximate brain area, e.g., 'low_freq_A1', 'AAF_A2'.
paradigm: name of taskontrol paradigm used during the session.

NOTE: when you save the stimulus/behavior data via the taskontrol paradigm
      make sure you name the file with the format: SUBJECT_PARADIGM_DATE_SESSION.h5
      For example: test000_am_tuning_20260401_001.h5
"""


subject = 'test000'
sessions = []

# Example session
newSession = {'subject':subject, 'date':'20260101', 'session': '001',
              'fps': 15.49, 'magnification': 2.4, 'depth': 250, 'angle': 48.56,
              'laserPower': 56, 'wavelength': 920, 'nFrames': 200,
              'brainArea': 'low_freq_AAF', 'sessionLabel': 'freq_tuning',
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

'''
# Here is the info that gets saved in the .mat file by Scanbox
In [2]: data2p.info
Out[2]: 
{'frame': array([   34,    42,    60, ..., 13733, 13750, 13757],
       shape=(1002,), dtype=uint16),
 'line': array([492, 353, 230, ...,  84,  57, 430], shape=(1002,), dtype=uint16),
 'event_id': array([2, 2, 2, ..., 2, 2, 2], shape=(1002,), dtype=uint8),
 'initialDatetime': MatlabOpaque([(b'', b'MCOS', b'datetime',
                     array([3707764736, 2, 1, 1, 1,1], dtype=uint32))],
              dtype=[('s0', 'O'), ('s1', 'O'), ('s2', 'O'), ('arr', 'O')]),
 'resfreq': 7930,
 'postTriggerSamples': 5000,
 'recordsPerBuffer': 512,
 'bytesPerBuffer': 10240000,
 'channels': 2,
 'ballmotion': array([], dtype=uint8),
 'abort_bit': 0,
 'scanbox_version': 2,
 'scanmode': 1,
 'config': {'wavelength': 920,
  'frames': 13941,
  'lines': 512,
  'magnification': 1,
  'magnification_list': array(['1.0', '1.2', '1.4', '1.7', '2.0', '2.4', '2.8', '3.4', '4.0',
         '4.8', '5.7', '6.7', '8.0'], dtype='<U3'),
  'pmt0_gain': 0.777174,
  'pmt1_gain': 0,
  'knobby': {'pos': {'x': 13171.34, 'y': 129.24, 'z': -10514.45, 'a': 49.18},
   'schedule': array([[    0,     0,    10,     0,   750],
          ...
          [    0,     0,    10,     0, 37500]], dtype=uint16)}},
 'sz': array([512, 796], dtype=uint16),
 'fold_lines': 0,
 'otwave': array([], dtype=uint8),
 'otwave_um': array([], dtype=uint8),
 'otparam': array([], dtype=uint8),
 'otwavestyle': 1,
 'volscan': 0,
 'power_depth_link': 0,
 'opto2pow': array([], dtype=uint8),
 'area_line': 1,
 'calibration': array([
        <scipy.io.matlab._mio5_params.mat_struct object at 0x7e9d99824a70>,
        ...
        <scipy.io.matlab._mio5_params.mat_struct object at 0x7e9d99824ef0>],
       dtype=object),
 'objective': 'Nikon 16x/0.8w/WD3.0',
 'messages': array([], dtype=object),
 'usernotes': array([], dtype='<U1')}
'''
