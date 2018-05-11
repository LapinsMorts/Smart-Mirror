# Personnalise your smart mirror here
config = {
    "ui_locale":"", # e.g. "fr_FR" fro French, "" as default
    "time_format":24, # 12 or 24
    "date_format":"%b %d, %Y", # check python doc for strftime() for options
    "weather_lang":"en", # see https://darksky.net/dev/docs/forecast for full list of language parameters values
    "weather_unit":"ca", # see https://darksky.net/dev/docs/forecast for full list of unit parameters values
    "weather_forecast_wrap_width":700,
    "days_forecasted":4,
    "forecast_icone_width":50,
    "forecast_icone_height":50,
    "latitude":None, # Set this if IP location lookup does not work for you (must be a string)
    "longitude":None, # Set this if IP location lookup does not work for you (must be a string)
    "xlarge_text_size":94,
    "large_text_size":48,
    "medium_text_size":28,
    "small_text_size":18,
    "font_family":"Helvetica",
    "weather_image_width":100,
    "weather_image_height":100,
    "headline_wrap_width":1600,
    "headlines_url":"https://news.google.com/news/rss/headlines/section/topic/NATION.en_ca/Canada?ned=ca&hl=en-CA&gl=CA" # get your own personnalized headline url at https://news.google.com/news/?ned=us&gl=US&hl=en
}

# maps open weather icons to
# icon reading is not impacted by the "lang" parameter
icon_lookup = {
    "clear-day": "assets/Sun.png",  # clear sky day
    "wind": "assets/Wind.png",   #wind
    "cloudy": "assets/Cloud.png",  # cloudy day
    "partly-cloudy-day": "assets/PartlySunny.png",  # partly cloudy day
    "rain": "assets/Rain.png",  # rain day
    "snow": "assets/Snow.png",  # snow day
    "snow-thin": "assets/Snow.png",  # sleet day
    "fog": "assets/Haze.png",  # fog day
    "clear-night": "assets/Moon.png",  # clear sky night
    "partly-cloudy-night": "assets/PartlyMoon.png",  # scattered clouds night
    "thunderstorm": "assets/Storm.png",  # thunderstorm
    "tornado": "assests/Tornado.png",    # tornado
    "hail": "assests/Hail.png"  # hail
}
