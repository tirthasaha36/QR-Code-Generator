# QR Code Generator

This is a simple Python script to generate QR codes from input data. The script uses the `qrcode` library to create QR codes and the `Pillow` library to handle image creation and display.

## Installation

Make sure you have Python installed. Then install the required dependencies using pip:

```bash
pip install qrcode[pil] pillow
```

## Usage

Run the script using Python:

```bash
python qr_generator.py
```

You will be prompted to enter the data to encode in the QR code. If you press enter without typing anything, a default URL (`https://www.openai.com`) will be used.

The generated QR code will be saved as `qr_code.png` in the current directory and displayed automatically.

## Example

```
Enter the data to encode in the QR code (or press enter to use default): Hello, world!
QR code saved as qr_code.png
```

## License

This project is provided as-is without any warranty.
