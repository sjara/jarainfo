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

subject = 'imag031'
signalType = 'GCaMP8m'
sessions = []


newSession = {'subject':subject, 'date':'20260501', 'time': '093044', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[3], 'intensities':[70,80],
              'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260501', 'time': '100142', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[3], 'intensities':[60,70],
              'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260501', 'time': '100910', 'suffix':'EDV',
              'sessionLabel': 'lowtoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[1], 'intensities':[70],
              'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260501', 'time': '101726', 'suffix':'EDV',
              'sessionLabel': 'midtoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[1], 'intensities':[60],
              'paradigm':'am_tuning'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260501', 'time': '102353', 'suffix':'EDV',
              'sessionLabel': 'hightoneTrains', 'signalType':signalType, 
              'LED':5, 'depth':200, 'frequencies':[1], 'intensities':[70],
              'paradigm':'am_tuning'}
sessions.append(newSession)


