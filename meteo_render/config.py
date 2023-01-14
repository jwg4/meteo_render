from collections import defaultdict


WEATHER_CODE_NAMES = defaultdict(lambda: "???")

WEATHER_CODE_NAMES.update(
    {
        0: "CLEAR SKY",
        3: "OVERCAST",
        61: "SLIGHT RAIN",
        63: "MODERATE RAIN",
        65: "HEAVY RAIN",
    }
)
