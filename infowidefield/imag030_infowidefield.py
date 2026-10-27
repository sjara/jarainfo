"""
Metadata for widefield imaging sessions.

--- SESSION PARAMETERS ---
subject: animal name.
date: in ISO format (YYYYMMDD).
time: in 24hr format (hhmmss).
suffix: experimenter initials, e.g., 'SJ'.
sessionLabel: short string that describes the session, e.g., '3_freq_mapping', '28kHz_mapping'.
signalType: imaging type, e.g, 'GCaMP6f', 'GCaMP8mSoma', 'intrinsic', 'flavoprotein', etc.
LED: LED intensity setting. A number from 0-8, matching the position of the LED knob.
depth: imaging depth from brain surface (in microns).
paradigm: name of the experimental paradigm used in the session.

-- Optional parameters --
frequencies: list of frequencies used in the session (in kHz), if applicable, e.g., [3, 32].
intensities: list of sound intensities used (in dB SPL), if applicable, e.g., [70, 80].
iso: percentage of isoflurane. Default is None for no anesthesia.
oxy: oxygen flow rate. Default is None for no anesthesia.
"""

subject = 'imag030'
signalType = 'GCaMP8m'
sessions = []


newSession = {'subject':subject, 'date':'20260501', 'time': '110958', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[3], 'intensities':[70,80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260501', 'time': '112348', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[3], 'intensities':[60,70],
              'paradigm':'am_tuning_curve'}

newSession = {'subject':subject, 'date':'20260501', 'time': '113124', 'suffix':'EDV',
              'sessionLabel': 'lowtoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[1], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260501', 'time': '114127', 'suffix':'EDV',
              'sessionLabel': 'midtoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[1], 'intensities':[60],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260501', 'time': '114805', 'suffix':'EDV',
              'sessionLabel': 'hightoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[1], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260521', 'time': '123042', 'suffix':'wf',
              'sessionLabel': 'lowtoneTrains', 'signalType':signalType, 
              'LED':4, 'depth':200, 'frequencies':[1], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260903', 'time': '162815', 'suffix':'wf',
              'sessionLabel': '3puretones', 'signalType':signalType, 
              'LED':3.5, 'depth':200, 'frequencies':[3], 'intensities':[70],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260903', 'time': '171502', 'suffix':'wf',
              'sessionLabel': '9puretones', 'signalType':signalType, 
              'LED':3.5, 'depth':200, 'frequencies':[9], 'intensities':[70],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20261026', 'time': '121033', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':8, 'depth':200, 'frequencies':[3,3,3,3], 'intensities':[75,65,55,45],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#7600 fr, 380 trials, session 000
#testing 3khz sound intensity response with 4 different intensities

newSession = {'subject':subject, 'date':'20261026', 'time': '123031', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':8, 'depth':200, 'frequencies':[10,10,10,10], 'intensities':[75,65,55,45],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#7600 fr, 380 trials, session 001
#testing 10khz sound intensity response with 4 different intensities

newSession = {'subject':subject, 'date':'20261026', 'time': '125741', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':8, 'depth':200, 'frequencies':[29,29,29,29], 'intensities':[75,65,55,45],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#7600 fr, 380 trials, session 002
#testing 29khz sound intensity response with 4 different intensities