currentSignalStatus=False



def turn_on_signal():
    global currentSignalStatus
    currentSignalStatus=True
    print("Signal is ***ON***")


def turn_off_signal():
    global currentSignalStatus
    currentSignalStatus=False
    print("Signal is ---OFF---")
