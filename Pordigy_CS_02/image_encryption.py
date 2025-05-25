from PIL import Image


def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    image.save(output_path)
    print(f"Encrypted image saved as {output_path}")


def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    image.save(output_path)
    print(f"Decrypted image saved as {output_path}")


# MAIN PROGRAM
if __name__ == "__main__":
    key = 50  # Change this number to anything between 1–255

    # Step 1: Encrypt
    encrypt_image("original.jpg", "encrypted.png", key)

    # Step 2: Decrypt
    decrypt_image("encrypted.png", "decrypted.jpg", key)
