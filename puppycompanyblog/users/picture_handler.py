import os
from PIL import Image
from flask import current_app, url_for

def add_profile_pic(pic_upload, username):
    file_name = pic_upload.filename
    ext_type = file_name.split('.')[-1]
    storage_path = str(username)+'.'+ext_type
    file_path = os.path.join(current_app.root_path,'static/profile_pics', storage_path)
    output_size = (200, 200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(file_path)
    return storage_path
