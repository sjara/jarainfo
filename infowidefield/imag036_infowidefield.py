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

subject = 'imag036'
signalType = 'GCaMP8m'
sessions = []


newSession = {'subject':subject, 'date':'20260625', 'time': '145038', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':4, 'depth':200, 'frequencies':[3,15.5,28], 'intensities':[70,65,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 285 trials, session 000

newSession = {'subject':subject, 'date':'20260625', 'time': '152128', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':4, 'depth':200, 'frequencies':[15.5,15.5,28], 'intensities':[55,75,85],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 285 trials, session 001

newSession = {'subject':subject, 'date':'20260625', 'time': '154054', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':4, 'depth':200, 'frequencies':[15.5,28,28], 'intensities':[60,65,70],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 285 trials, session 002

newSession = {'subject':subject, 'date':'20260701', 'time': '104245', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':2, 'depth':200, 'frequencies':[3,15.5,28], 'intensities':[70,65,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 285 trials, session 000

newSession = {'subject':subject, 'date':'20260701', 'time': '110534', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':2, 'depth':200, 'frequencies':[3,15.5,28], 'intensities':[80,75,85],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 285 trials, session 001



