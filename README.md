# sonify-floats

Program takes in a text file and a "center frequency" and outputs a series of notes around the center frequency. The text file should have the title of the data set as its first line, and each data point as a line following. The data must consist of numbers, as it will be scaled to range from 0.0 to 2.0. The note corresponding to a data point will have frequency equal to the center frequency multiplied by this scaled number. A frequency of 0 will correspond to a rest.

The examples given all use data sets from the assignment "stripey-data" in Stanford University's introductory CS course CS106A (http://web.stanford.edu/class/cs106a/). The midi files generated have been played in Ableton Live 10 using the synth Sine1 Noise Attack Lead and saved as mp3s for your listening pleasure.
