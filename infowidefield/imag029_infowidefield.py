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

subject = 'imag029'
signalType = 'GCaMP8m'
sessions = []

#### ADD 20260220 (low poles)


######
# 20260308: W9U: Attempting to map.
#####

# Tested speakers
# Took blood vessels photo
# Down "0.5", screenshot

# Confirm 70 dB, 4/8 low poles:
newSession = {'subject':subject, 'date':'20260308', 'time': '192913', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[3], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Bright -- but weirdly just two "A1" spots, without the A2 and AAF that I saw before.??

# Want to replicate, maybe with higher LED to try to get the dimmer spots?
newSession = {'subject':subject, 'date':'20260308', 'time': '193707', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[3], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Very similar

# Let's try the 32 kHz
newSession = {'subject':subject, 'date':'20260308', 'time': '194504', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[32], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Nothing good in figure.

# 28 kHz?
newSession = {'subject':subject, 'date':'20260308', 'time': '194958', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[28], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Also nothing.

# 32 kHz, 80 dB, max
newSession = {'subject':subject, 'date':'20260308', 'time': '195524', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Absolutely nothing.

# 28 kHz, 80 dB, max
newSession = {'subject':subject, 'date':'20260308', 'time': '200019', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Ok, yes, response!

# Mapping at max LED, both intensities, up to 28
# 3800*3*2 = 22800 triggers
newSession = {'subject':subject, 'date':'20260308', 'time': '200618', 'suffix':'WG',
              'sessionLabel': 'intensity', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[3, 9, 28], 'intensities':[70, 80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. 

# Grab one at just 80 and one at just 70, in case that's useful
# 70 
# 2800*3 = 11400 triggers
newSession = {'subject':subject, 'date':'20260308', 'time': '200618', 'suffix':'WG',
              'sessionLabel': '3freq_to28', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[3, 9, 28], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. 

# 80
newSession = {'subject':subject, 'date':'20260308', 'time': '204040', 'suffix':'WG',
              'sessionLabel': '3freq_to28', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[3, 9, 28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%.


