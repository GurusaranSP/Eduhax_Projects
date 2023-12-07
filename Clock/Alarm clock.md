# Alarm Clock Program

This Python program implements a graphical alarm clock using the Tkinter library. The program displays a digital clock and allows users to set an alarm time. When the set alarm time is reached, the program plays a sound.

## Features

-  Digital Clock Display:  The program displays a digital clock with the current time, date, day of the week, timezone, and timezone abbreviation.

-  Alarm Setting:  Users can set an alarm in a 24-hour format using the provided Entry fields.

-  Alarm Sound:  When the current time matches the set alarm time, the program plays a sound ("Music.wav").

## Usage

1.  Requirements:  Make sure you have Python installed on your system.

2.  Dependencies:  The program uses the Tkinter library for the GUI, time for handling time-related operations, and winsound for playing the alarm sound.

3.  Run the Program: 
   ```bash
   python alarm_clock.py
   ```

4.  Set Alarm: 
   - Enter the desired hour, minute, and second in the respective Entry fields.
   - Click the "Set Your Alarm" button.

5.  Note: 
   - The time must be entered in the 24-hour format.
   - The program will continue running in the background until the alarm is triggered.

## Code Explanation

### `Clock` Class
- Initializes a digital clock using Tkinter's Label widget.
- Updates the clock display every second using the `time` method.

### `AlarmClock` Class (Inherits from `Clock`)
- Extends the `Clock` class to include alarm functionality.
- Adds Entry fields for setting the alarm time and a button to trigger the alarm.
- Implements the `alarm_clock` method to continuously check for the alarm time match and play the sound.

### Main Execution
- Creates an instance of the `Tk` class.
- Instantiates the `AlarmClock` class, initializing the GUI.
- Starts the Tkinter event loop with `mainloop()`.

# License

The Alarm Clock Program is the sole property of Guru Saran Satsangi and was created in 2022 as part of an internship.

## Ownership and License

1.  Ownership:  This program is the sole creation and property of Guru Saran Satsangi.

2.  License: 
   - Permission is hereby granted to any person obtaining a copy of this software to use, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
   - The software is provided "as is," without warranty of any kind, express or implied.
   - In no event shall Guru Saran Satsangi be liable for any claim, damages, or other liability arising from, out of, or in connection with the software or the use or other dealings in the software.

3.  Attribution: 
   - Users of this software are required to provide attribution to Guru Saran Satsangi.

© 2022 Guru Saran Satsangi. All rights reserved.