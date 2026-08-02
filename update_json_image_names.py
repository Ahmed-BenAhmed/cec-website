import json
import os

json_path = r'ce-club-reflection\instagram_posts_data.json'
images_folder = r'ce-club-reflection\images'

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for post in data:
    post_id = post.get('postId')
    if post_id:
        image_filename = f"{post_id}.png"
        image_path = f"images/{image_filename}"
        if os.path.exists(os.path.join(images_folder, image_filename)):
            if 'image' not in post or not isinstance(post['image'], dict):
                post['image'] = {}
            post['image']['src'] = image_path

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated JSON with new image names.")