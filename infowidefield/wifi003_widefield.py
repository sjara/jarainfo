# Metadata for widefield imaging session

# --- SESSION PARAMETERS ---
# sessionNumber = From timestamps.
# date: in ISO format (YYYY-MM-DD).
# sessionID: suffix that indentifies the session.
# sessionLabel: any string that describes the session.
# imgType: imaging type. Either 'calcium' or 'intrinsic'.
# LED: LED intensity setting. A number from 0-8, matching the position of the LED knob.
# ISO: percentage of isoflurane. Default is None for no anesthesia.
# Oxy: oxygen flow rate. Default is None for no anesthesia.

subject = 'wifi003'
sessions = []

# Example session: calcium, awake
newSession = {'subject':subject, 'date':'2024-08-20', 'time': '16:14:51',
              'sessionLabel': 'calcium_test', 'imgType':'calcium', 'LED':7,
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

# Example session: calcium, awake
newSession = {'subject':subject, 'date':'2024-08-20', 'time': '16:32:14',
              'sessionLabel': 'calcium_test', 'imgType':'calcium', 'LED':7,
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

'''
# Example session: calcium + anesthesia
newSession = {'subject':subject, 'date':'2025-04-03', 'time': '16:32:00',
              'sessionLabel': 'calcium_anesthetized', 'imgType':'calcium', 'LED':7,
              'ISO':1.5, 'Oxy':1.25,
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

# Example session: intrinsic
newSession = {'subject':subject, 'date':'2025-04-03', 'time': '16:59:00',
              'sessionLabel': 'intrinsic_anesthetized', 'imgType':'intrinsic', 'LED':0.5,
              'ISO':1.5, 'Oxy':1.25,
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
'''

