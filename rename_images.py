import os

images_dir = r"c:\Users\Acer\OneDrive\Desktop\Fishtail-Work\Vivalis solo site\Images"

for filename in os.listdir(images_dir):
    if " " in filename:
        new_filename = filename.replace(" ", "-").lower()
        # Also remove double hyphens if any (e.g. from " - ")
        while "--" in new_filename:
            new_filename = new_filename.replace("--", "-")
        
        old_path = os.path.join(images_dir, filename)
        new_path = os.path.join(images_dir, new_filename)
        
        print(f"Renaming: '{filename}' -> '{new_filename}'")
        try:
            os.rename(old_path, new_path)
        except FileExistsError:
            print(f"Error: {new_filename} already exists. Skipping.")
