import requests
from PIL import Image
import numpy as np
from io import BytesIO

def download_tiger_image():
    # ✅ Tiger image URL (public domain)
    url = "https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg"
    response = requests.get(url)

    if 'image' not in response.headers.get('Content-Type', ''):
        raise Exception("URL did not return an image. Please check the URL.")

    image = Image.open(BytesIO(response.content))
    print("✅ Tiger image downloaded successfully.")
    return image

def encrypt_image(image, key):
    pixels = np.array(image)

    # Convert to int16 to avoid overflow during encryption
    encrypted_pixels = (pixels.astype(np.int16) + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))

    print("🔐 Image encrypted successfully.")
    return encrypted_image

def decrypt_image(encrypted_image, key):
    encrypted_pixels = np.array(encrypted_image)

    # Convert to int16 to avoid underflow during decryption
    decrypted_pixels = (encrypted_pixels.astype(np.int16) - key) % 256
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))

    print("🔓 Image decrypted successfully.")
    return decrypted_image

# === Main Execution ===
if __name__ == "__main__":
    try:
        key = 42  # 🗝️ Encryption/Decryption key

        # Download and encrypt
        tiger_image = download_tiger_image()
        encrypted_image = encrypt_image(tiger_image, key)

        # Decrypt the encrypted image back
        decrypted_image = decrypt_image(encrypted_image, key)

        # Save images (optional)
        tiger_image.save("tiger_original.jpg")
        encrypted_image.save("tiger_encrypted.jpg")
        decrypted_image.save("tiger_decrypted.jpg")

        # ✅ Display images
        print("🖼️ Showing original image...")
        tiger_image.show(title="Original Tiger")

        print("🖼️ Showing encrypted image...")
        encrypted_image.show(title="Encrypted Tiger")

        print("🖼️ Showing decrypted image...")
        decrypted_image.show(title="Decrypted Tiger")

        print("✅ Done!")

    except Exception as e:
        print(f"❌ Error: {e}")
