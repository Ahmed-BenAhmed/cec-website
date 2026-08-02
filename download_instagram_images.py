import os
import json
import requests

# Path to your JSON file
json_path = r'ce-club-reflection\instagram_posts_data.json'
# Folder to save images
output_folder = r'ce-club-reflection\images'

os.makedirs(output_folder, exist_ok=True)

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, post in enumerate(data):
    # Try to get the image URL from the Instagram post URL
    # If your JSON has direct image URLs, use that field instead
    image_url = post.get('image', {}).get('src')
    if not image_url:
        # No image URL, skip
        continue

    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        ext = os.path.splitext(image_url)[1].split('?')[0] or '.jpg'
        filename = f"post_{post.get('postId', i)}{ext}"
        filepath = os.path.join(output_folder, filename)
        with open(filepath, 'wb') as img_file:
            img_file.write(response.content)
        print(f"Downloaded {image_url} -> {filename}")
        # Update JSON to use local path
        post['image']['src'] = f'images/{filename}'
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")

# Save updated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done. Update your carousel.js to use the local image paths.")