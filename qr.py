import qrcode
import matplotlib.pyplot as plt

# 1. Generate the QR code
data = "Fuck OFF!!!"
img = qrcode.make(data)

# 2. Save the QR code as an image
img.save("qr_image.png")
print("QR code saved as qr_image.png")

# 3. Display the QR code using matplotlib
plt.imshow(img, cmap='gray')  # QR codes are black & white
plt.axis('off')               # Hide axes
plt.show()
