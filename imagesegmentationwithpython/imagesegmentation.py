import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("rabbitsimage.jpg")
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(7,7),0)
print(f"original image shape: {image.shape}\nrgb image shape: {image_rgb.shape}\ngray image shape: {gray.shape}\nblur image shape: {blur.shape}")

fig, ax = plt.subplots(figsize=(5,5))
ax.imshow(image_rgb)
ax.set_title('Original Image')
#ax.axis("off")
plt.show()


"""
# renk filtreleri
fig, axs = plt.subplots(1,3,figsize=(15,5))
axs[0].imshow(image_rgb[:,:,0],cmap="Reds")
axs[0].axis("off")
plt.axis('off')
plt.show()
"""

# threshold ( eşik değer ) atayarak
optimal, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) # OTSU yöntemi
#  2. parametre 0 -> eşik değeri için OTSU yöntemi tarafından otomatik olarak hesaplanacak bir değer kullanılacak.
#  3. parametre 255 -> max piksel değeri (255 = beyaz)
#  4. parametre cv2.THRESH_BINARY_INV: belirli bir eşik değeri üzerindeki pikselleri beyaz yapacak, diğerlerini ise siyah

print(optimal) # OTSU yöntemi ile belirlenmiş optimal eşik değeri

plt.imshow(thresh)
plt.axis('off')
plt.show()

# kenar belirleyerek

kenar = cv2.Canny(blur,50,150)

cv2.imshow("images",np.hstack([gray,blur,kenar]))
cv2.waitKey(0)
cv2.destroyAllWindows()

# yeşil renk için segmentasyon

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# yeşil renk için hsv değerleri
yesil_alt_sinir = np.array([38, 100, 100])
yesil_ust_sinir = np.array([75, 255, 255])


mask = cv2.inRange(hsv_image, yesil_alt_sinir, yesil_ust_sinir)
mask_rgb = cv2.cvtColor(mask,cv2.COLOR_BGR2RGB)

segmented_image = cv2.bitwise_and(image_rgb, image_rgb, mask=mask) # Maskeleme işlemi yaparak yeşil nesneleri içeren görüntüyü oluşturuyoruz.
segmented_image_rgb = cv2.cvtColor(segmented_image,cv2.COLOR_BGR2RGB)

fig, axs = plt.subplots(3,3,figsize=(5,5))
axs[0, 0].imshow(image_rgb)
axs[0, 0].set_title('Original Image')

axs[0, 1].imshow(mask_rgb)
axs[0, 1].set_title('Mask Image')

axs[0, 2].imshow(segmented_image_rgb)
axs[0, 2].set_title('Segmented Image')

for ax in axs.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()







