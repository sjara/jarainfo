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

subject = 'imag026'
signalType = 'GCaMP8m'
sessions = []

## Information for 2026- 0217 and 0224 need to be added
# 20260217: W7T: First sessions, got low poles
# 20260224: W8T: After centering LED on ACtx, 70 dB was sufficient to see good 32 kHz responses

######
# 20260303: W9T: Attempting to get good mapping for this animal.
#####
# Since I saw good 3 kHz and 32 kHz responses on W8T, I'm hoping to get a three-freq map at 70 dB today
# Checked speakers. Went down 0.5 rotation.

# Checking low poles
newSession = {'subject':subject, 'date':'20260303', 'time': '102212', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[3], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Slightly blurrier than on W8T, but low poles definitely visible in figure.

# Now high poles
newSession = {'subject':subject, 'date':'20260303', 'time': '104042', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[32], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Nothing in figure.

# Refocused, then went back down 0.5 rotation. Tried again.
newSession = {'subject':subject, 'date':'20260303', 'time': '105027', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[32], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Still nothing.

# It looks like my LED positioning/FOV are a little different from W8T (when I saw good responses). Moved camera to try to better match that day. Also cleaned some more silicone off of the Flow-it. Took another blood vessels photo (0001). Back down 0.5 rotation.

newSession = {'subject':subject, 'date':'20260303', 'time': '112739', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[32], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Still no clear signal on figure. :(

# Check again that I can consistently see the low poles:
newSession = {'subject':subject, 'date':'20260303', 'time': '113419', 'suffix':'WG',
              'sessionLabel': '3kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[3], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. And, yes, I can see the low poles. They are still blurrier than W8T, though.

# I have a photo from 20260224_093624, where I see clear responses, and can confirm that they were at 4 LED, 32 kHz, 70 dB. I'm starting to worry about hearing loss or photobleaching -- but it was so bright just a week ago. I haven't recorded 026 between then and now -- has Evan?

# Adjusted the depth down just a tad, because I looked a little more in focus than in the image from that session. (Even though both are supposed to be 0.5 rotations.)
newSession = {'subject':subject, 'date':'20260303', 'time': '115539', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[32], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Still nothing in figure...

# Can I get anything at 28 kHz with these settings?
newSession = {'subject':subject, 'date':'20260303', 'time': '120147', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[28], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Nothing clean in the figure.

# 10 kHz? At what point does it stop/start working?
newSession = {'subject':subject, 'date':'20260303', 'time': '120147', 'suffix':'WG',
              'sessionLabel': '10kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[10], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Yes -- I see responses.

# I want to try 28 kHz one more time before messing with paramaters:
newSession = {'subject':subject, 'date':'20260303', 'time': '121833', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':4, 'depth':127, 'frequencies':[28], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Nope.


# Try cranking up the LED...
newSession = {'subject':subject, 'date':'20260303', 'time': '122401', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[28], 'intensities':[70],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Still nothing convincing.

# Try going up to 80 dB...
newSession = {'subject':subject, 'date':'20260303', 'time': '123059', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 99%. Responses!!! Yay!!

# Can I get 32 kHz with 8/8 and 80 dB?
# (Disregard the extra recording here, LED wasn't at the right tick so I aborted.)
newSession = {'subject':subject, 'date':'20260303', 'time': '123836', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. I can just barely make out the pattern that I saw the other day. I think the mouse may have been moving or something, try again...

# Whoops, this was another 28 kHz -- let it run to get an idea of variability
newSession = {'subject':subject, 'date':'20260303', 'time': '124508', 'suffix':'WG',
              'sessionLabel': '28kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Yep, great.

# Now 32 kHz
newSession = {'subject':subject, 'date':'20260303', 'time': '125030', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Still nothing.

# Can I get up to 30 kHz?
newSession = {'subject':subject, 'date':'20260303', 'time': '125653', 'suffix':'WG',
              'sessionLabel': '30kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[30], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Actually pretty clean!

# Ok I want to try 32 kHz just one more time before I give up on it
newSession = {'subject':subject, 'date':'20260303', 'time': '130238', 'suffix':'WG',
              'sessionLabel': '32kHz_mapping', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[32], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# Went to 100%. Nope.

# Ok, mapping time! 3 to 30 kHz at 80 dB and max LED.
# 3800*3 = 11400 triggers
#newSession = {'subject':subject, 'date':'20260303', 'time': '131014', 'suffix':'WG',
#              'sessionLabel': '3freq_to30', 'signalType':signalType, 
#              'LED':8, 'depth':127, 'frequencies':[3, 10, 30], 'intensities':[80],
#              'paradigm':'am_tuning_curve'}
#sessions.append(newSession)
# **** double check what that middle frequency should be recorded as here ****
# Mouse was getting up into the frame towards the end. Took a look -- maybe the paw can reach?
# Went to 99%. 
# Doesn't look like the timestamps saved for this one. :( The application was running weirdly slowly for the last few recordings (e.g. taking a while to let me type or to close). Not sure if I somehow forgot or if there was a computer issue. The timestamps for the next recording are there.

# Let's do one up to 28 before I need to leave.
# (Ignore extra recording here.)
newSession = {'subject':subject, 'date':'20260303', 'time': '132551', 'suffix':'WG',
              'sessionLabel': '3freq_to28', 'signalType':signalType, 
              'LED':8, 'depth':127, 'frequencies':[3, 9, 28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)
# **** double check what that middle frequency should be recorded as here ****
# Went to 100%

#WF optics have been optimized since March 3rd, should be brighter with more even illumination
newSession = {'subject':subject, 'date':'20260408', 'time': '132559', 'suffix':'EDV',
              'sessionLabel': '3freq_to28', 'signalType':signalType, 
              'LED':8, 'depth':200, 'frequencies':[3, 9, 28], 'intensities':[70,80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260408', 'time': '134845', 'suffix':'EDV',
              'sessionLabel': '3kHz_80dB', 'signalType':signalType, 
              'LED':8, 'depth':200, 'frequencies':[3], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260408', 'time': '140205', 'suffix':'EDV',
              'sessionLabel': '15_5kHz_80dB', 'signalType':signalType, 
              'LED':8, 'depth':200, 'frequencies':[15.5], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260408', 'time': '141526', 'suffix':'EDV',
              'sessionLabel': '28kHz_80dB', 'signalType':signalType, 
              'LED':8, 'depth':200, 'frequencies':[28], 'intensities':[80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)

newSession = {'subject':subject, 'date':'20260408', 'time': '142340', 'suffix':'EDV',
              'sessionLabel': '3freq_to28', 'signalType':signalType, 
              'LED':8, 'depth':200, 'frequencies':[3,15.5,28], 'intensities':[70,80],
              'paradigm':'am_tuning_curve'}
sessions.append(newSession)



