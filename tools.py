import network

def ifconfig():

    sta_if = network.WLAN(network.STA_IF)
    ip = sta_if.ifconfig()
    return ip

def cp(source_file, destination_file):
    # Open the source file in read mode
    with open(source_file, "r") as source:
        # Read the contents of the source file
        contents = source.read()

    # Open the destination file in write mode
    with open(destination_file, "w") as destination:
        # Write the contents to the destination file
        destination.write(contents)

def clear():
    print('\033[2J\033[H', end='')

