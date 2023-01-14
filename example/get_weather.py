import os
import shutil

from meteo_render import render_weather


if __name__ == '__main__':
    location = (51.4, -0.07)

    dest_folder = r"example/output"
    src_file = os.path.join("meteo_render", "templates", "family", "style.css")
    shutil.copy(src_file, dest_folder)

    src_image_folder = os.path.join("meteo_render", "templates", "family", "img")
    image_folder = os.path.join(dest_folder, "img")
    for image in os.listdir(src_image_folder):
        src_file = os.path.join(src_image_folder, image)
        shutil.copy(src_file, image_folder)

    page = render_weather(location, "family", image_folder)
    dest_filepath = os.path.join(dest_folder, "weather.html")
    with open(dest_filepath, "w") as f:
        f.write(page)
