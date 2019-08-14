"""Module that will handle DarkSky responses."""


class DarkSkyResponse(object):

    def __init__(self, response_json):
        self.response_json = response_json

    def get_daily_summary(self):
        return self.response_json['daily']['data'][0]['summary']

    def get_precip_intensity(self):
        return self.response_json['daily']['data'][0]['precipIntensity']
