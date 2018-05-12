from Tkinter import *
from Config import config, icon_lookup
from PIL import Image, ImageTk
from ForecastedWeather import ForecastedWeather
from ApiToken import weather_api_token
import traceback
import requests
import json

class Weather(Frame):
    def __init__(self, parent, today_weekday_name, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.today_weekday_name = today_weekday_name
        self.days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.temperature = ''
        self.forecast = ''
        self.location = ''
        self.currently = ''
        self.icon = ''
        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=TOP, anchor=W)
        self.temperatureLbl = Label(self.degreeFrm, font=(config["font_family"], config["xlarge_text_size"]), fg="white", bg="black")
        self.temperatureLbl.pack(side=LEFT, anchor=N)
        self.iconLbl = Label(self.degreeFrm, bg="black")
        self.iconLbl.pack(side=LEFT, anchor=CENTER, padx=20)
        self.currentlyLbl = Label(self, font=(config["font_family"], config["medium_text_size"]), fg="white", bg="black")
        self.currentlyLbl.pack(side=TOP, anchor=W, padx=(11, 0))
        self.forecastLbl = Label(self, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black", wraplength=config["weather_forecast_wrap_width"], justify=LEFT)
        self.forecastLbl.pack(side=TOP, anchor=W, pady=(0, 10), padx=(11, 0))
        self.locationLbl = Label(self, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black")
        self.locationLbl.pack(side=TOP, anchor=W, pady=(0, 20), padx=(11, 0))
        self.next_days = [ForecastedWeather(self) for i in range(config['days_forecasted'])]

        self.get_weather()

    def get_ip(self):
        try:
            ip_url = "http://jsonip.com/"
            req = requests.get(ip_url)
            ip_json = json.loads(req.text)
            return ip_json['ip']
        except Exception as e:
            traceback.print_exc()
            return "Error: %s. Cannot get ip." % e

    def get_weather(self):
        try:

            if config["latitude"] is None and config["longitude"] is None:
                # get location
                location_req_url = "http://freegeoip.net/json/%s" % self.get_ip()
                r = requests.get(location_req_url)
                location_obj = json.loads(r.text)

                lat = location_obj['latitude']
                lon = location_obj['longitude']

                location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])

                # get weather
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&exclude=minutely,flags,alerts&units=%s" % (weather_api_token, lat,lon, config["weather_lang"], config["weather_unit"])
            else:
                location2 = ""
                # get weather
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&exclude=minutely,flags,alerts&units=%s" % (weather_api_token, config["latitude"], config["longitude"], config["weather_lang"], config["weather_unit"])

            r = requests.get(weather_req_url)
            weather_obj = json.loads(r.text)

            degree_sign= u'\N{DEGREE SIGN}'
            temperature2 = "%s%s" % (str(int(weather_obj['currently']['temperature'])), degree_sign)
            currently2 = weather_obj['currently']['summary']
            forecast2 = weather_obj["hourly"]["summary"]

            icon_id = weather_obj['currently']['icon']
            icon2 = None

            if icon_id in icon_lookup:
                icon2 = icon_lookup[icon_id]

            if icon2 is not None:
                if self.icon != icon2:
                    self.icon = icon2
                    image = Image.open(icon2)
                    image = image.resize((config["weather_image_width"], config["weather_image_height"]), Image.ANTIALIAS)
                    image = image.convert('RGB')
                    photo = ImageTk.PhotoImage(image)

                    self.iconLbl.config(image=photo)
                    self.iconLbl.image = photo
            else:
                # remove image
                self.iconLbl.config(image='')

            if self.currently != currently2:
                self.currently = currently2
                self.currentlyLbl.config(text=currently2)
            if self.forecast != forecast2:
                self.forecast = forecast2
                self.forecastLbl.config(text=forecast2)
            if self.temperature != temperature2:
                self.temperature = temperature2
                self.temperatureLbl.config(text=temperature2)
            if self.location != location2:
                if location2 == ", ":
                    self.location = "Cannot Pinpoint Location"
                    self.locationLbl.config(text="Cannot Pinpoint Location")
                else:
                    self.location = location2
                    self.locationLbl.config(text=location2)
            if len(weather_obj["daily"]["data"]) > config["days_forecasted"]:
                i = 0
                for forecast in weather_obj["daily"]["data"][1 : config["days_forecasted"]+1]:
                    d = self.days_of_week[(self.days_of_week.index(self.today_weekday_name) + i + 1) % len(self.days_of_week)]
                    ic = forecast["icon"] if forecast["icon"] is not None else ""
                    mn = str(round(forecast["temperatureLow"], 0))[:-2] + degree_sign if forecast["temperatureLow"] is not None else ""
                    mx = str(round(forecast["temperatureHigh"], 0))[:-2] + degree_sign if forecast["temperatureHigh"] is not None else ""
                    self.next_days[i].destroy()
                    self.next_days[i] = ForecastedWeather(self, d, ic, mn, mx)
                    self.next_days[i].pack(side=TOP, anchor=W, pady=10, padx=(11, 0))
                    i += 1


        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get weather." % e

        self.after(600000, self.get_weather)

    @staticmethod
    def convert_kelvin_to_fahrenheit(kelvin_temp):
        return 1.8 * (kelvin_temp - 273) + 32
