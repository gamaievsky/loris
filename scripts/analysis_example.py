# analysis_example.py
#
# Use the Loris procedural interface to perform a
# Reassigned Bandwidth-Enhanced analysis of a
# clarinet tone, having fundamental frequency of
# approximately 415 Hz.

import loris
import librosa

# pitch is G#4
FUNDAMENTAL = 415.0

# import the clarinet samples
fin = loris.AiffFile( "clarinet.aiff" )
samples = fin.samples()
sr = 44100

y_librosa, sr_librosa = librosa.load("clarinet.aiff")
print(sr_librosa)

# configure a Loris Analyzer, use frequency
# resolution equal to 80% of the fundamental
# frequency, main lobe width equal to the
# fundamental frequency, and frequency drift
# equal to 20% of the fundamental frequency
# (approx. 83 Hz )

myAnalyzer = loris.Analyzer(100, 150);
myAnalyzer.setFreqDrift(100);
myAnalyzer.setHopTime( 0.008 );
myAnalyzer.setCropTime(myAnalyzer.hopTime() * 2.0);


# analyze and store partials
partials = myAnalyzer.analyze(samples,sr);

# export to SDIF file
fsdif = loris.SdifFile(partials)
fsdif.write( "clarinet.sdif" )

# synthesize
sampsout = loris.synthesize(partials,sr)

# export samples to AIFF file
faiff = loris.AiffFile(sampsout,sr)
faiff.write("synth_clar.aiff")
