import os
import shutil
import urllib.request

# Base dataset folder
base_dataset = "dataset"
prepared_dataset = os.path.join(base_dataset, "prepared")

# Create folders
os.makedirs(os.path.join(prepared_dataset, "text"), exist_ok=True)
os.makedirs(os.path.join(prepared_dataset, "non_text"), exist_ok=True)

# STEP 1️⃣: Move your cleaned document images to "text"
cleaned_images = "cleaned_images"  # already processed document images
for img_file in os.listdir(cleaned_images):
    src = os.path.join(cleaned_images, img_file)
    dst = os.path.join(prepared_dataset, "text", img_file)
    shutil.copy(src, dst)

# STEP 2️⃣: Download some non-text images for "non_text"
non_text_folder = os.path.join(prepared_dataset, "non_text")

urls = [
    "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d",
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e",
    "https://images.unsplash.com/photo-1507149833265-60c372daea22",
    "https://images.unsplash.com/photo-1517816428104-797789379ee6",
    "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759"
]


for i, url in enumerate(urls):
    try:
        filename = f"non_text_{i+1}.jpg"
        urllib.request.urlretrieve(url, os.path.join(non_text_folder, filename))
        print(f"✅ Downloaded {filename}")
    except Exception as e:
        print(f"⚠️ Failed to download {url}: {e}")

print("\n✅ Dataset prepared successfully!")
print(f"Check: {prepared_dataset}")
