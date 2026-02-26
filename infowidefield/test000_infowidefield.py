"""
Metadata for widefield imaging sessions.

--- SESSION PARAMETERS ---
subject: animal name.
date: in ISO format (YYYY-MM-DD).
time: in 24hr format (HH:MM:SS).
sessionLabel: short string that describes the session, e.g., '3_freq_mapping', '28kHz_mapping'.
signalType: imaging type, e.g, 'GCaMP6f', 'GCaMP8mSoma', 'intrinsic', 'flavoprotein', etc.
LED: LED intensity setting. A number from 0-8, matching the position of the LED knob.
paradigm: name of the experimental paradigm used in the session.

-- Optional parameters --
frequencies: list of frequencies used in the session (in kHz), if applicable, e.g., [3, 32].
intensities: list of sound intensities used in the session (in dB SPL), if applicable, e.g., [70, 80].
iso: percentage of isoflurane. Default is None for no anesthesia.
oxy: oxygen flow rate. Default is None for no anesthesia.
"""

subject = 'test000'
signalType = 'GCaMP8m'
sessions = []

# Example session: calcium, awake
newSession = {'subject':subject, 'date':'2024-08-20', 'time': '16:14:51',
              'sessionLabel': 'calcium_test', 'signalType':signalType, 'LED':7,
              'frequencies':[3, 9.8, 32], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

# Example session: calcium, awake
newSession = {'subject':subject, 'date':'2024-08-20', 'time': '16:32:14',
              'sessionLabel': 'calcium_test', 'signalType':signalType, 'LED':7,
              'frequencies':[32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

'''
# Example session: calcium + anesthesia
newSession = {'subject':subject, 'date':'2025-04-03', 'time': '16:32:00',
              'sessionLabel': 'calcium_anesthetized', 'signalType':signalType, 'LED':7,
              'iso':1.5, 'oxy':1.25,
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

# Example session: intrinsic
newSession = {'subject':subject, 'date':'2025-04-03', 'time': '16:59:00',
              'sessionLabel': 'intrinsic_anesthetized', 'signalType':'intrinsic', 'LED':0.5,
              'iso':1.5, 'oxy':1.25,
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
'''

