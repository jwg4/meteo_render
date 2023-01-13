import datetime
import os

import jinja2
import requests

URL_PATTERN = "https://api.open-meteo.com/v1/forecast?latitude=%f&longitude=%f&hourly=temperature_2m,apparent_temperature,precipitation,weathercode"


def render_weather(location, template):
    url = URL_PATTERN % location
    result = requests.get(url)
    result.raise_for_status()
    data = result.json()

    now = datetime.datetime.now()
    extra = {
        "timestamp": now,
    }

    env = jinja2.Environment(
        loader=jinja2.PackageLoader("meteo_render")
    )
    template = env.get_template(os.path.join(template, "page.html.j2"))

    return template.render(data=data, extra=extra)
