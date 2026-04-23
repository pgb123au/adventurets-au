import zipfile, os

dist_dir = r"C:\Users\peter\Downloads\CC\websites\adventurets.com.au\site\dist"
zip_path = r"C:\Users\peter\Downloads\CC\websites\adventurets.com.au\site\deploy.zip"

count = 0
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(dist_dir):
        for f in files:
            full = os.path.join(root, f)
            arcname = os.path.relpath(full, dist_dir).replace(os.sep, '/')
            zf.write(full, arcname)
            count += 1

print(f"Created deploy.zip with {count} files")
size_mb = os.path.getsize(zip_path) / (1024 * 1024)
print(f"Size: {size_mb:.1f} MB")
