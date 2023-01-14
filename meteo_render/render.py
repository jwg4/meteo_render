import datetime
import os

import jinja2
import requests

URL_PATTERN = "https://api.open-meteo.com/v1/forecast?latitude=%f&longitude=%f&hourly=temperature_2m,apparent_temperature,precipitation,weathercode"


def format_data(raw_data):
    timestamps = raw_data["hourly"]["time"]
    return raw_data


def render_weather(location, template):
    url = URL_PATTERN % location
    result = requests.get(url)
    result.raise_for_status()
    raw_data = result.json()
    data = format_data(raw_data)

    now = datetime.datetime.now()
    extra = {
        "timestamp": now,
    }

    env = jinja2.Environment(
        loader=jinja2.PackageLoader("meteo_render")
    )
    env.globals.update(zip=zip)
    template = env.get_template(os.path.join(template, "page.html.j2"))

    return template.render(data=data, extra=extra)
