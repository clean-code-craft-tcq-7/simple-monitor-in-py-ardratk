from time import sleep
import sys

def check_temperature(temperature):
    if temperature > 102 or temperature < 95:
        return False, 'Temperature critical!'
    return True, ''

def check_pulse(pulseRate):
    if pulseRate < 60 or pulseRate > 100:
        return False, 'Pulse Rate is out of range!'
    return True, ''

def check_spo2(spo2):
    if spo2 < 90:
        return False, 'Oxygen Saturation out of range!'
    return True, ''

def vitals_ok(temperature, pulseRate, spo2):
    checks = [
        check_temperature(temperature),
        check_pulse(pulseRate),
        check_spo2(spo2)
    ]
    for ok, msg in checks:
        if not ok:
            alert(msg)
            return False
    return True

def alert(message):
    print(message)
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)