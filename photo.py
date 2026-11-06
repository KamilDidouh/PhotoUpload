from PIL import Image
 
# Open an image
img = Image.open("/home/kamil/boot_dev/photo_upload/test_images/PXL_20260718_192322547.jpg")
 
# Get EXIF data
exif_data = img.getexif()
 
# Display EXIF tags and values
for tag_id, value in exif_data.items():
    tag_name = Image.ExifTags.TAGS.get(tag_id, tag_id)
    print(tag_name, ":", value)