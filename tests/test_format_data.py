from meteo_render.render import format_data


MINIMAL_SAMPLE_DATA = {
    "latitude": 51.4,
    "longitude": -0.06000018,
    "generationtime_ms": 0.6250143051147461,
    "utc_offset_seconds": 0,
    "timezone": "GMT",
    "timezone_abbreviation": "GMT",
    "elevation": 57.0,
    "hourly_units": {
        "time": "iso8601",
        "temperature_2m": "°C",
        "apparent_temperature": "°C",
        "precipitation": "mm",
        "weathercode": "wmo code",
    },
    "hourly": {
        "time": [
            "2023-01-13T00:00",
        ],
        "temperature_2m": [
            8.0,
        ],
        "apparent_temperature": [
            3.4,
        ],
        "precipitation": [
            0.00,
        ],
        "weathercode": [
            2,
        ],
    },
}

MINIMAL_SAMPLE_RESULT = [
    {
        "date": "2023-01-13",
        "hours": [
            {
                "time": "2023-01-13T00:00",
                "temperature_2m": 8.0,
                "apparent_temperature": 3.4,
                "precipitation": 0.0,
                "weathercode": 2,
            }
        ],
    }
]


def test_format_data():
    assert format_data(MINIMAL_SAMPLE_DATA) == MINIMAL_SAMPLE_RESULT
