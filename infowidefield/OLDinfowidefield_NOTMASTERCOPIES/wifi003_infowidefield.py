"""
Metadata for widefield imaging sessions.

See test000_infowidefield.py for explanation of parameters and example sessions.
"""

subject = 'wifi003'
signalType = 'GCaMP6f'
sessions = []

# Example session: calcium, awake
newSession = {'subject':subject, 'date':'2024-08-20', 'time': '16:14:51',
              'sessionLabel': 'calcium_test', 'signalType':signalType, 'LED':7,
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

# Example session: calcium, awake
newSession = {'subject':subject, 'date':'2024-08-20', 'time': '16:32:14',
              'sessionLabel': 'calcium_test', 'signalType':signalType, 'LED':7,
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

