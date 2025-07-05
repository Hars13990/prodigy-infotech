def process_image(image_path, output_path, key):
    img = Image.open(image_path)         
    pixels = img.load()                  
    width, height = img.size             

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]  
            r ^= key                     
            g ^= key            
            b ^= key                     
            pixels[x, y] = (r, g, b)

    img.save(output_path)               
    print(f"Done! Image saved as {output_path}")

print("Simple Image Encryptor / Decryptor")

mode = input("Type 'e' for encrypt or 'd' for decrypt: ").lower()
image_file = input("Enter image file name (e.g., photo.png): ")
output_file = input("Enter output file name (e.g., result.png): ")
key = int(input("Enter a secret key (0-255): "))

process_image(image_file, output_file, key)
