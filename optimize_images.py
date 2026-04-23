"""Optimize wp-assets images: resize to max 1200px wide, convert to WebP, keep originals as fallback."""
import os
from pathlib import Path
from PIL import Image

WP_ASSETS = Path(r"C:\Users\peter\Downloads\CC\websites\adventurets.com.au\site\public\images\wp-assets")
MAX_WIDTH = 1200
WEBP_QUALITY = 82

total_saved = 0
converted = 0

for img_path in sorted(WP_ASSETS.iterdir()):
    if img_path.suffix.lower() not in ('.jpg', '.jpeg', '.png', '.webp'):
        continue

    original_size = img_path.stat().st_size

    try:
        with Image.open(img_path) as im:
            # Convert RGBA to RGB for JPEG/WebP compatibility
            if im.mode in ('RGBA', 'P'):
                im = im.convert('RGB')

            # Resize if wider than MAX_WIDTH
            if im.width > MAX_WIDTH:
                ratio = MAX_WIDTH / im.width
                new_height = int(im.height * ratio)
                im = im.resize((MAX_WIDTH, new_height), Image.LANCZOS)

            # Save as WebP with same stem
            webp_path = img_path.with_suffix('.webp')
            im.save(webp_path, 'WEBP', quality=WEBP_QUALITY, method=6)
            new_size = webp_path.stat().st_size

            # If original wasn't already webp, remove original and keep webp
            if img_path.suffix.lower() != '.webp':
                saved = original_size - new_size
                total_saved += saved
                os.remove(img_path)
                converted += 1
                print(f"  {img_path.name} ({original_size//1024}KB) -> {webp_path.name} ({new_size//1024}KB) saved {saved//1024}KB")
            else:
                # Was already webp, just overwrite with optimized version
                saved = original_size - new_size
                total_saved += saved
                converted += 1
                print(f"  {img_path.name} ({original_size//1024}KB) -> optimized ({new_size//1024}KB) saved {saved//1024}KB")
    except Exception as e:
        print(f"  SKIP {img_path.name}: {e}")

print(f"\nDone: {converted} images optimized, {total_saved//(1024*1024)}MB saved")
