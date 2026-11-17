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

subject = 'imag039'
signalType = 'GCaMP8m'
sessions = []


newSession = {'subject':subject, 'date':'20260716', 'time': '115004', 'suffix':'EDV',
              'sessionLabel': 'widefieldMapping', 'signalType':'signalType', 
              'LED':3, 'depth':200, 'frequencies':[3,15.5,28], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 285 trials, session 000

newSession = {'subject':subject, 'date':'20261117', 'time': '123703', 'suffix':'EDV',
              'sessionLabel': 'widefieldMapping', 'signalType':'signalType', 
              'LED':9, 'depth':300, 'frequencies':[3,15.5,28], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 000
#retesting the same frequency/intensities as the session done in July to see how the map compares

newSession = {'subject':subject, 'date':'20261117', 'time': '130145', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':9, 'depth':300, 'frequencies':[3,4.8,7.5,10,12,18.5,22.5,26,30], 'intensities':[70,60,60,55,50,60,60,65,70],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#17100 fr, 450 trials, session 001
#testing a full frequency range with 9 total frequencies

newSession = {'subject':subject, 'date':'20261117', 'time': '132501', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':9, 'depth':300, 'frequencies':[3,4.8,7.5,10,12,18.5,22.5,26,30], 'intensities':[80,70,70,65,60,70,70,75,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#17100 fr, 450 trials, session 002
#testing same frequencies as previous session but with higher intensities to see if the map changes
#either forgot to save timestamp or something else happened, but the timestamp doesn't exist


