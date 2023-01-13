from meteo_render import render_weather


if __name__ == '__main__':
    location = (51.4, -0.07)
    page = render_weather(location, "family")
    with open(r"example/output/weather.html", "w") as f:
        f.write(page)
