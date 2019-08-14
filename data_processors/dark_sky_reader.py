"""Module that reads data from DarkSky API. """

from dark_sky_response import DarkSkyResponse
import requests


class DarkSkyReader(object):

    def __init__(self, apikey):
        self.apikey = apikey
        self.base_url = 'https://api.darksky.net/forecast/'

    def get_weather(self, lat, lon, yyyy, mm, dd, h='01', m='00', s='00'):
        time = '{yyyy}-{mm}-{dd}T{h}:{m}:{s}'.format(yyyy=yyyy,
                                                     mm=mm,
                                                     dd=dd,
                                                     h=h,
                                                     m=m,
                                                     s=s)

        weather_url = '{base}{apikey}/{lat},{lon},{time}'.format(base=self.base_url,
                                                                 apikey=self.apikey,
                                                                 lat=lat,
                                                                 lon=lon,
                                                                 time=time)
        print('Rquesting: ', weather_url)
        weather_req = requests.get(weather_url)
        assert weather_req.status_code == 200

        weather_json = weather_req.json()
        weather_json['querytime'] = time

        weather_response = DarkSkyResponse(weather_json)

        return weather_response

