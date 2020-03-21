

# DATA SONIFICATION BY SCALED FREQUENCY

# This program takes in numerical data as a text file and
# scales each element to lie between 0.0 and 2.0. The corresponding
# note will be at a specified center frequency weighted by the
# scaled value. A frequency of 0.0 will map to a rest.

import sys
from music21 import *

def read_data(filename):
    """
    Given filename, returns a list
    of data in the file.
    The element with index 0 is processed
    separately, as it is meant to be the
    title of the data set.
    The rest of the elements are the float values.
    """
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        # Title as first line
        data.append(lines.pop(0))
        # Other lines are floats
        for line in lines:
            data.append(float(line))
        return data

def normalize_data(data):

    """
    Modifies each element in the data list
    to return a list of floats between
    0 and 2. Uses the formula
    xnorm = 2 * (x - min) / (max - min)
    to achieve this scaling,
    where max and min are the maximum
    and minimum of the data set.
    The normalized data point is multiplied
    by 2 to ensure that one travels by the
    magnitude of the center frequency away
    from the specified center frequency to
    reach the minimum and maximum.
    """
    floats = data[1:]
    diff = max(floats) - min(floats)
    for i in range(1, len(data)):
        data[i] = 2*(data[i] - min(floats)) / diff
    return data

def freq_append(freq, data):
    freq_stream = stream.Stream()
    for el in data[1:]:
        if el*freq != 0:
            new_note = note.Note()
            new_note.pitch.frequency = int(el * freq)
            freq_stream.append(new_note)
        else:
            r = note.Rest()  # frequency of 0 will be a rest
            freq_stream.append(r)
    return freq_stream



def main():
    args = sys.argv[1:]

    # To run from terminal:
    # filename center-frequency

    # To save:
    # filename center-frequency save

    filename = str(args[0])
    freq = float(args[1])

    raw_data = read_data(filename)
    normed_data = normalize_data(raw_data)
    freq_stream = freq_append(freq, normed_data)
    freq_stream.show('midi')

    # To save midi output:

    if len(args) == 3:
        data_name = raw_data[0].strip()
        track_name = data_name + str(freq) + '.mid'
        freq_stream.write("midi", track_name)

if __name__ == '__main__':
    main()
