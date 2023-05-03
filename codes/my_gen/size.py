import tensorflow as tf

# Load the image as a tensor
image_path = "/dataset/train/left/66.jpg"
image = tf.io.read_file(image_path)
image = tf.image.decode_jpeg(image, channels=3)

# Get the dimensions of the image
height, width, channels = image.shape
print("Image dimensions: {} x {} x {}".format(height, width, channels))
