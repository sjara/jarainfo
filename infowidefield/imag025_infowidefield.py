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

subject = 'imag025'
signalType = 'GCaMP8m'
sessions = []

# Template:
#newSession = {'subject':subject, 'date':'', 'time': '', 'suffix':'WG',
#              'sessionLabel': '', 'signalType':signalType, 
#              'LED':, 'depth':, 'frequencies':[], 'intensities':[],
#              'paradigm':'am_tuning_curve'}
#sessions.append(newSession)

########################
# Need to add info from 20260217 and 20260219 
########################

########################
# 20260305: W9R: Attempting to map. Will try 70 dB first, but suspect that I need 80 dB.
########################

# Tested speaker
# Took blood vessels photo
# Down "0.5" (took screenshot)

# Look for low poles at 70 dB, 4/8 first
newSession = {'subject':subject, 'date':'20260305', 'time': '120505', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED'4:, 'depth':127, 'frequencies':[3], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Nothing in figure...??

# low poles at 70, max LED?
newSession = {'subject':subject, 'date':'20260305', 'time': '121122', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[3], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Phew, the low poles show up now. A1 and AAF are great, A2 may be hard to seperate from background -- may be worth trying to reduce LED 

# high poles at 70, max LED. 32 kHz first, then could try 28 if not.
newSession = {'subject':subject, 'date':'20260305', 'time': '121823', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[32], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 95%***
# Looks like nothing but I don't trust it with the 95%... Again:
newSession = {'subject':subject, 'date':'20260305', 'time': '122435', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[32], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Got distracted writing an email, so the stimulus file went longer than needed. 
# Nothing in figure.

# 28 kHz at 70?
newSession = {'subject':subject, 'date':'20260305', 'time': '123131', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[28], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Nothing good in figure.

# Ok, up to 80 dB. 32 first
newSession = {'subject':subject, 'date':'20260305', 'time': '125139', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Nothing good.

# 28 kHz, 80 dB
newSession = {'subject':subject, 'date':'20260305', 'time': '130916', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Kiiiinda something dorsal, but it's hard to say.

# 20 kHz?
newSession = {'subject':subject, 'date':'20260305', 'time': '131548', 'suffix':'WG',
              'sessionLabel': '20kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[20], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. I can see signal! Lots of vessels lit up, though -- maybe I should focus a little deeper?

# Refocused from vessels down "0.5," screenshot. It does look deeper.
# Let's try 28 kHz one more time
newSession = {'subject':subject, 'date':'20260305', 'time': '132337', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 97%*** Maybe because I was looking through a folder?
# Nothing good but I don't trust the 97%... again:
newSession = {'subject':subject, 'date':'20260305', 'time': '133015', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Nothing good.

# Reconfirm 20:
newSession = {'subject':subject, 'date':'20260305', 'time': '133532', 'suffix':'WG',
              'sessionLabel': '20kHz_mapping', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[20], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
# Went to 99%. Really vessely.

# I'm running out of time, so I'm going to grab a fast (3800 triggers total) mapping to 20 even though I doubt it'll be great...
newSession = {'subject':subject, 'date':'20260305', 'time': '134212', 'suffix':'WG',
              'sessionLabel': '3freq_to20', 'signalType':signalType, 
              'LED'8:, 'depth':127, 'frequencies':[3, 999, 20], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
# Figure out what the middle freq should be written as here****
# Went to 100%.


