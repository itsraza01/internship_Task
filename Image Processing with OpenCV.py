#Image Processing with OpenCV
import cv2

# Load image
img = cv2.imread('image.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blur, 50, 150)

# Display original image and processed image
cv2.imshow('Original Image', img)
cv2.imshow('Processed Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
