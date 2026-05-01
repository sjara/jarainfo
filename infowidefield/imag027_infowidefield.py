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

subject = 'imag027'
signalType = 'GCaMP8m'
sessions = []

## Information for 2026- 0220, 0224, 0227 need to be added
# 20260220: 
# 

######
# 20260306: W9F: Attempting to get good mapping for this animal.
#####

# Tested speaker
# Took blood vessels photo
# Down "0.5", screenshot. Remember that this is the mouse where dorsal part is sunken in, such that ACtx is higher.

# Low poles at 70 dB and 4/8?
newSession = {'subject':subject, 'date':'20260306', 'time': '151831', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[3], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Not great, but they are kinda there
# This mouse's brain moves a LOT.
# Try max LED
newSession = {'subject':subject, 'date':'20260306', 'time': '152439', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[3], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Still quite low-contrast. My 4/8 may look better for less background.

# 4/8, 80 dB low poles?
newSession = {'subject':subject, 'date':'20260306', 'time': '153215', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[3], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Ok, looks great! Has the extra dorsal spot because it's 80, but yknow...

# 28 kHz at these settings?
newSession = {'subject':subject, 'date':'20260306', 'time': '153756', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Started stim a litte late
# 98% recorded ***
# Something reaaaaally weird happened here

# Try again
newSession = {'subject':subject, 'date':'20260306', 'time': '153756', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Ok, something there!

# 32 kHz?
newSession = {'subject':subject, 'date':'20260306', 'time': '155058', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Definitely visible.

# Mapping at 80 dB and 4/8, 3800*3 = 11400 triggers
newSession = {'subject':subject, 'date':'20260306', 'time': '155638', 'suffix':'WG',
              'sessionLabel': '3freq_to32', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[3, 9, 32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%
# Checked and saw some 3, 32 spots, but not as clear for the ~9.

# Try all combos (22800 triggers)
newSession = {'subject':subject, 'date':'20260306', 'time': '161449', 'suffix':'WG',
              'sessionLabel': 'intensities', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[3, 9, 32], 'intensities':[70, 80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%
# Miscalculated the time that it'd finish, so the stimulus file went a bit long. 
# Didn't look great.

# Grab another 80 dB-only mapping
newSession = {'subject':subject, 'date':'20260306', 'time': '164608', 'suffix':'WG',
              'sessionLabel': '3freq_to32', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[3, 9, 32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%.





