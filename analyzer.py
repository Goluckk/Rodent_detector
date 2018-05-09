import numpy as np
import wave
# import matplotlib.pyplot as plt

def analyze(threshold):
    ''' analyze sound file and return number of frequencies above the given threshold '''
    wr = wave.open('a.wav', 'r')
    framerate = wr.getframerate()
    windowlength = 5  # time window to analyze in seconds
    windows = 2  # number of time windows to process, 10 seconds, 2 windows of 5 seconds

    frequencies = []

    for window in range(windows):  # process time windows
        print('\nProcessing from {} to {} s'.format(window * windowlength, (window + 1) * windowlength))
        avgf = np.zeros(int(framerate / 2 + 1))

        #	the sound signal for q seconds is concatenated. The fft over that
        # period is averaged to average out noise.
        for pt in range(windowlength):
            da = np.fromstring(wr.readframes(framerate), dtype=np.int8)
            left, right = da[0::2], da[1::2]

            lf, rf = abs(np.fft.rfft(left)), abs(np.fft.rfft(right))
            max_lf, max_rf = max(lf), max(rf)

            avgf += (max_lf + max_rf) / 2
        avgf /= (windowlength*1000)
	print(avgf)
        frequencies.extend(list(filter(lambda x: x > threshold, avgf.tolist())))
    return len(frequencies)
