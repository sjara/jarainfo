from jaratoolbox import celldatabase

subject = 'test193'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

### TEMPLATE ###
'''
### MOUSE IN xxxx

# pia ~ xxx   (manipulator value at putative pia)
# final ~ xxx   (manipulator value at final depth)
# depth ~ x.x mm

exp0.maxDepth = xxxx    # depth of probe tip in microns
exp0.add_site(xxxx) # xxx ref
exp0.add_session('xx-xx-xx','a','tuningFreq','am_tuning_curve')
exp0.add_session('yy-yy-yy','b','tuningAM','am_tuning_curve')
exp0.add_session('zz-zz-zz','a','naturalSounds','natural_sound_detection')

experiments.append(exp0)
'''

### MOUSE OUT xxxx

exp0 = celldatabase.Experiment(subject, '2026-10-01', brainArea='left_AC', probe='NPv2-5422',
                               recordingTrack='leftAC_DiI', info=['facesleft', 'soundBinaural'])

### MOUSE IN 950am

# pia ~ x=22124
# final x=25760
# depth ~= 3.6 mm

exp0.maxDepth = 3600
exp0.add_site(3600) # tip 1 ref
exp0.add_session('11-50-23','a','tuningFreq','am_tuning_curve')
exp0.add_session('12-00-29','a','clickSeqs','gardner_clicks')
exp0.add_session('12-31-16','a','naturalSounds','natural_sound_detection')

experiments.append(exp0)

### MOUSE OUT 1325


exp1 = celldatabase.Experiment(subject, '2026-10-06', brainArea='left_AC', probe='NPv2-5422',
                               recordingTrack='leftAC_DiD', info=['facesleft', 'soundBinaural'])

### MOUSE IN 330pm

# pia ~ x=17144.4
# final x=20331.4
# depth ~= 3.2 mm

exp1.maxDepth = 3200
exp1.add_site(3200) # tip 1 ref
exp1.add_session('16-55-55','a','tuningFreq','am_tuning_curve')
exp1.add_session('17-17-30','b','tuningFreq','am_tuning_curve')
exp1.add_session('17-33-53','c','tuningAM','am_tuning_curve')
exp1.add_session('17-43-28','a','clickSeqs','gardner_clicks')
exp1.add_session('18-09-03','a','naturalSounds','natural_sound_detection')

experiments.append(exp1)

### MOUSE OUT
