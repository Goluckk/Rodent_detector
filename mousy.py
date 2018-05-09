import subprocess
import time

#  helper modules
import analyzer
import sendsms

# activate microphone, record for 10 seconds
activeMic = "arecord -r 160000 -d 10 ./a.wav -D sysdefault:CARD=1"

while True:
    # 1: Collect data
    p = subprocess.Popen(activeMic, shell=True)
    time.sleep(10)
    p.terminate()

    # 2: Analyse data
    overThreshold = analyzer.analyze(10000)
    if overThreshold > 0:
        # 3: Send out notifications
        sendsms.sendText()
