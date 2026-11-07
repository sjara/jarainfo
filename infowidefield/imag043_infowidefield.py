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

subject = 'imag043'
signalType = 'GCaMP8m'
sessions = []


newSession = {'subject':subject, 'date':'20261106', 'time': '134345', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':9, 'depth':300, 'frequencies':[3,15.5,28], 'intensities':[60,55,60],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 000
#zoomed in 300 microns past where blood vessels were most clear
#used 9 LED
#test sequence before full mapping

newSession = {'subject':subject, 'date':'20261106', 'time': '140011', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[3,4.8,7.5,12,18.5,30], 'intensities':[60,55,50,45,50,60],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 150 trials, session 001
#testing a full frequency sweep

newSession = {'subject':subject, 'date':'20261106', 'time': '142353', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[3,4.8,7.5,12,18.5,30], 'intensities':[65,55,55,50,55,65],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 150 trials, session 002
#testing a full frequency sweep a second time with slightly higher intesnsities
