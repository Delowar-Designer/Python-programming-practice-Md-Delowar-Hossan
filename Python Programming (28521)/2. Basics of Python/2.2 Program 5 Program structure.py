# Program structure
# reused code
import weather
import math
# function definition
def convert(TheStream):
    TempStream = []
    for temp in TheStream:
        celsius = round((temp - 32) / 1.8)
        TempStream.append(celsius)
    return TempStream
# main program
Fstream = weather.get_forecasts('Blacksbarg, VA')
print(Fstream)
Cstream = convert(Fstream)
print(Cstream)