from PIL import Image

# Load the image
image_path = 'dataset/image2.png'
image = Image.open(image_path)

# Get the image dimensions (for reference, not necessarily used in the formula)
width, height = image.size

# Crop the second ball from the image (adjust the crop coordinates based on where the ball is)
# Here, it's estimated the ball is in the right portion of the image.
ball_2_cropped = image.crop((450, 100, 650, 300))

# Get the width and height of the ball in the cropped image (in pixels)
ball_2_size = ball_2_cropped.size
ball_2_width_pixels = ball_2_size[0]  # assuming width and height are the same (since the ball is round)

# Given data
ball_actual_size_cm = 20  # cm (real size of the ball)
distance_image_1 = 100  # cm (distance in the first image)
ball_size_image_1_pixels = 200  # pixels (size of the ball in image 1, assumed same as image 2)

# Calculate the distance to the ball in the second image using the proportional formula
distance_image_2 = (distance_image_1 * ball_size_image_1_pixels) / ball_actual_size_cm

# Output the result
print(f"Distance to the ball in the second image: {distance_image_2} cm")
