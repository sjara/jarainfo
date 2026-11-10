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

newSession = {'subject':subject, 'date':'20261103', 'time': '132719', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':1050, 'frequencies':[4,18,27], 'intensities':[75,70,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 000
#retesting last weeks final session to see how things align
#the depth evaluation in the wiki seems off, but according to that I would be at 1050 micrometers (3/4 turn large knob)

newSession = {'subject':subject, 'date':'20261103', 'time': '135829', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':5.5, 'depth':700, 'frequencies':[4,18,27], 'intensities':[75,70,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 001
#retesting last weeks final session to see how things align
#brought the depth back a bit to approximately 700 micrometers
#reduced LED brightness a bit as well

newSession = {'subject':subject, 'date':'20261103', 'time': '141118', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':700, 'frequencies':[4,18,27], 'intensities':[75,70,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 002
#retesting last weeks final session to see how things align
#went a little deeper this time, maybe around 900 micrometers
#put LED brightness back at 6 because signal was too dark

newSession = {'subject':subject, 'date':'20261103', 'time': '142645', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[4,18,27], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 003
#retesting last weeks final session to see how things align
#went a little shallower this time, maybe around 300 micrometers

newSession = {'subject':subject, 'date':'20261103', 'time': '143643', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[4,6,9,13,18,27], 'intensities':[75,72,68,68,70,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 300 trials, session 004
#testing a full range of frequencies as a proof of concept

newSession = {'subject':subject, 'date':'20261104', 'time': '141335', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[4,18,27], 'intensities':[75,70,75],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 000
#retesting last weeks final session to see how things align

newSession = {'subject':subject, 'date':'20261104', 'time': '141335', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[5,14,26], 'intensities':[75,70,80],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 001
#trying slightly different depth and frequencies to see how it affects the signal

newSession = {'subject':subject, 'date':'20261104', 'time': '145605', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[3,14,29], 'intensities':[60,60,60],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 002
#decreasing intensities to see how it affects the signal
    
newSession = {'subject':subject, 'date':'20261104', 'time': '150919', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[3,10,30], 'intensities':[60,55,65],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#5700 fr, 150 trials, session 003

newSession = {'subject':subject, 'date':'20261104', 'time': '152327', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[3,4.8,7.5,12,18.5,30], 'intensities':[60,55,50,45,50,60],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#17100 fr, 150 trials, session 004
#testing a full frequency sweep
#accidentally put in the wrong number of triggers
#don't use this session

newSession = {'subject':subject, 'date':'20261104', 'time': '154609', 'suffix':'EDV',
              'sessionLabel': 'intensitytoneTrains', 'signalType':signalType, 
              'LED':6, 'depth':300, 'frequencies':[3,4.8,7.5,12,18.5,30], 'intensities':[60,55,50,45,50,60],
              'paradigm':'widefield_mapping'}
sessions.append(newSession)
#11400 fr, 150 trials, session 005
#testing a full frequency sweep
#redid last session with proper number of triggers
