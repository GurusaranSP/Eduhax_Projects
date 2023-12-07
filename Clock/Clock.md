# Digital Clock Program

This Python program implements a graphical digital clock using the Tkinter library. The program displays the current time, date, day of the week, timezone, and timezone abbreviation.

## Features

-  Digital Clock Display:  The program displays a digital clock with the current time, date, day of the week, timezone, and timezone abbreviation.

## Usage

1.  Requirements:  Make sure you have Python installed on your system.

2.  Dependencies:  The program uses the Tkinter library for the GUI, time for handling time-related operations, and winsound for potential future enhancements (currently not utilized).

3.  Run the Program: 
   ```bash
   python digital_clock.py
   ```

4.  Note: 
   - The clock updates every second.

## Code Explanation

The program uses the `Tkinter` library to create a GUI window and display a digital clock. It utilizes the `strftime` function from the `time` module to format and update the clock's text every second.

### `time` Function
- Formats the current time, date, day of the week, timezone, and timezone abbreviation using `strftime`.
- Updates the clock display every second using the `after` method.

### Main Execution
- Creates an instance of the `Tk` class.
- Sets the window size using `grid_bbox`.
- Sets the window title to "Clock."
- Creates a `Label` widget (`clk`) for displaying the digital clock.
- Invokes the `time` function to start the clock update loop.
- Starts the Tkinter event loop with `mainloop()`.

# License

The Digital Clock Program is the sole property of Guru Saran Satsangi and was created in 2022 as part of an internship.

## Ownership and License

1.  Ownership:  This program is the sole creation and property of Guru Saran Satsangi.

2.  License: 
   - Permission is hereby granted to any person obtaining a copy of this software to use, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
   - The software is provided "as is," without warranty of any kind, express or implied.
   - In no event shall Guru Saran Satsangi be liable for any claim, damages, or other liability arising from, out of, or in connection with the software or the use or other dealings in the software.

3.  Attribution: 
   - Users of this software are required to provide attribution to Guru Saran Satsangi.

© 2022 Guru Saran Satsangi. All rights reserved.