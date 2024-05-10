from PIL import Image

def merge_images(image1_path, image2_path, output_path):
    # Open both images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Create a new image with a size that can contain both input images
    new_width = image1.width + image2.width
    new_height = max(image1.height, image2.height)
    merged_image = Image.new("RGB", (new_width, new_height))

    # Paste the first image onto the new image
    merged_image.paste(image1, (0, 0))

    # Paste the second image next to the first image
    merged_image.paste(image2, (image1.width, 0))

    # Save the merged image
    merged_image.save(output_path)

# Example usage
image1_path = "./image1.png"
image2_path = "./image2.png"
output_path = "./4-new_buttons.png"
merge_images(image1_path, image2_path, output_path)

