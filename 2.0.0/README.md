# 2.0.0

This update of the [Berlin EmoDB](http://database.syntheticspeech.de/)

* adds 281 previously not contained files (that have not been recognized by 80% of the labelers).
* adds 816 (for every audio file) [laryngograms](https://en.wikipedia.org/wiki/Electroglottograph), in wav format with 16kHz sampling rate.
* adds a "natural" value to all samples, like the "confidence" values, as the original authors asked the labelers also "how natural does this sample sound?"


## How to replicate this update:
* get a copy of the original database (containes a folder "wav_laryng" with 817 stereo files) by mailing the original authors

* unpack the folder "wav_laryng" and the file "listener_judgements.txt"
  
* make two folders : "audio" and "laryngo"
  
* use sox to split the files:
```
for f in wav_laryng/*wav; do sox $f audio/`basename $f` remix 1; done
for f in wav_laryng/*wav; do sox $f laryngo/`basename $f` remix 2; done
```

* install the requirements.txt.lock

* run the update.py script

* run the publish.py script
