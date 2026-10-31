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

subject = 'imag041'
signalType = 'GCaMP8m'
sessions = []


newSession = {'subject':subject, 'date':'20261029', 'time': '154337', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':700, 'frequencies':[3,15.5,28], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 000
#zoomed in 700 microns past where blood vessels were most clear
#used 6 LED because 8 LED was overexposing the image

newSession = {'subject':subject, 'date':'20261029', 'time': '161251', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':700, 'frequencies':[5,12,29], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 001
#zoomed in 700 microns past where blood vessels were most clear
#used 6 LED because 8 LED was overexposing the image

newSession = {'subject':subject, 'date':'20261029', 'time': '162958', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':700, 'frequencies':[4,17,27], 'intensities':[75,70,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 002
#zoomed in 700 microns past where blood vessels were most clear
#used 6 LED because 8 LED was overexposing the image

newSession = {'subject':subject, 'date':'20261030', 'time': '155948', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':700, 'frequencies':[3,15.5,28], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 000
#zoomed in 700 microns past where blood vessels were most clear
#used 6 LED because 8 LED was overexposing the image
#ran these same settings yesterday to compare

newSession = {'subject':subject, 'date':'20261030', 'time': '155948', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':1050, 'frequencies':[3,18,28], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 001
#zoomed in 1050 microns past where blood vessels were most clear
#used 6 LED because 8 LED was overexposing the image

newSession = {'subject':subject, 'date':'20261030', 'time': '164107', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':1050, 'frequencies':[4,18,27], 'intensities':[75,70,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 002
#zoomed in 1050 microns past where blood vessels were most clear
#used 6 LED because 8 LED was overexposing the image
