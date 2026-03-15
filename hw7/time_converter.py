"""
This program converts time from 24-hour format
hh:mm to 12-hour format with AM/PM.
"""

import sys
input_time = input("Enter time in 24h format hh:mm ").split(":")
hours = int(input_time[0])
minutes = int(input_time[1])
if minutes < 10:
    display_minutes = "0" + str(minutes)  # pylint: disable=invalid-name
elif minutes in range(11, 60):
    display_minutes = str(minutes)  # pylint: disable=invalid-name
else:
    print('Invalid input')
    sys.exit()

if hours in range(13, 24):
    print(str(hours - 12) + ":" + display_minutes + " PM")
elif hours in range(0, 13):
    print(str(hours) + ":" + display_minutes + " AM")
else:
    print('Invalid input')
