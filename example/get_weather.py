import os
import shutil

from meteo_render import render_weather


if __name__ == '__main__':
    location = (51.4, -0.07)
    page = render_weather(location, "family")
    dest_folder = r"example/output"
    dest_filepath = os.path.join(dest_folder, "weather.html")
    with open(dest_filepath, "w") as f:
        f.write(page)
    src_file = os.path.join("meteo_render", "templates", "family", "style.css")
    shutil.copy(src_file, dest_folder)
