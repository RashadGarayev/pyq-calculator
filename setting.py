#!/usr/bin/python
import time,subprocess
time.sleep(5)
subprocess.call('sudo sh setup.sh', shell=True)
subprocess.call('python calculator.py', shell=True)