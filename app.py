from flask import Flask, render_template
import glob
import os

app = Flask(__name__)

@app.route('/')
def gallery():
    image_folder = os.path.join(app.static_folder, 'images', '*.jpeg')  # Pattern to match all .jpeg files
    image_files = glob.glob(image_folder)
    # Convert full paths back to relative paths
    image_files = [os.path.relpath(file, start=app.static_folder) for file in image_files]
    images = [{'filename': file} for file in image_files]
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
