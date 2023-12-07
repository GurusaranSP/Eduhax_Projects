# QR Code Generation Program

This Python program uses the PyQRCode library to generate a QR code for the given text (in this case, the name 'Saran'). The program then saves the generated QR code as a PNG image.

## Features

-  QR Code Generation:  The program utilizes the PyQRCode library to create a QR code.
-  Saving as PNG:  The generated QR code is saved as a PNG image.

## Usage

1.  Requirements:  Make sure you have Python installed on your system.

2.  Install Dependencies: 
   ```bash
   pip install pyqrcode pypng
   ```

3.  Run the Program: 
   ```bash
   python generate_qrcode.py
   ```

4.  Note: 
   - The program will create a PNG file named 'qrcode.png' containing the generated QR code for the text 'Saran'.

## Code Explanation

The program uses the `pyqrcode` library to create a QR code for the specified text ('Saran') and then saves it as a PNG image using the `png` module.

### Main Execution
- Imports the `pyqrcode` and `png` modules.
- Defines the text to be encoded in the QR code ('Saran').
- Creates a QR code using `pyqrcode.create`.
- Saves the generated QR code as a PNG image using the `png` module and the specified scale.

Feel free to modify the code to generate QR codes for different texts!

# License

The QR Code Generation Program is the sole property of Guru Saran Satsangi and was created in 2022 as part of an internship.

## Ownership and License

1.  Ownership:  This program is the sole creation and property of Guru Saran Satsangi.

2.  License: 
   - Permission is hereby granted to any person obtaining a copy of this software to use, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
   - The software is provided "as is," without warranty of any kind, express or implied.
   - In no event shall Guru Saran Satsangi be liable for any claim, damages, or other liability arising from, out of, or in connection with the software or the use or other dealings in the software.

3.  Attribution: 
   - Users of this software are required to provide attribution to Guru Saran Satsangi.

© 2022 Guru Saran Satsangi. All rights reserved.