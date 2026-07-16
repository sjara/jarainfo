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

subject = 'imag038'
signalType = 'GCaMP8m'
sessions = []


newSession = {'subject':subject, 'date':'20260716', 'time': '111231', 'suffix':'EDV',
              'sessionLabel': 'widefieldMapping', 'signalType':toneTrains, 
              'LED':3, 'depth':200, 'frequencies':[3,15.5,28], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 285 trials, session 000




