from jaratoolbox import celldatabase

subject = 'test193'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType, paradigmName.

#expX = celldatabase.Experiment(subject, '2025-05-xx', brainArea='right_AC', probe='NPv2-5422', recordingTrack='anteriorxxx_DYE', info=['facesxx', 'soundLeft'])

# Reference electrode is x:tip

#experiments.append(expx)

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
