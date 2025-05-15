import qrcode
from PIL import Image

def generate_qr_code(data, filename="qr_code.png"):
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add data to the instance
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")

    # Optionally display the image
    img.show()

if __name__ == "__main__":
    user_input = input("Enter the data to encode in the QR code (or press enter to use default): ")
    if not user_input:
        user_input = "https://www.openai.com"
    generate_qr_code(user_input)
