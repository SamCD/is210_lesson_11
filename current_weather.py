#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 11, current_weather file"""

import urllib2
import json

base_url = 'http://api.openweathermap.org/data/2.5/weather'

class CurrentWeather(object):
    """Creates a current weather class"""

    zip_codes = {}
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(self, zipcode_data="zipcode_database.csv"):
        self.read_csv(zipcode_data)

    def get_weather(self, city, country, units='metric'):
        api_query = '{}?units={}&q={},{}'.format(
            base_url, units, city, country
        )

        try:
            response = urllib2.urlopen(api_query)
        except urllib2.HTTPError:
            raise CurrentWeatherException(
                error.code,
                'Error: {} {}'.format(error.code, error.msg)
                )

        return json.load(response)['main']

    def read_csv(csv_path):
        try:
            os.path.exists(csv_path)
        except Exception:
            raise CurrentWeatherException(code=9010,
                                          message=
                                          'CSV zipcode database {} not found'
                                          .format(csv_path))
            try:
                fhandler = open(csv_path, 'r')
                line = fhandler.readline()
                while line:
                    zip_codes[line['zipcode']] = {'city': line['city'],
                                             'state': line['state'],
                                             'latitude': line['latitude'],
                                             'longitude': line['longitude'],
                                             'country': line['country']}
                filehandler.close()
            except IOError:
                raise CurrentWeatherException(code=4151,
                                              message=
                                              'Error Reading {}'
                                              .format(csv_path))
            finally:
                fhandler.close()

    print get_weather('New York', 'us', 'metric')
    print get_weather('San Francisco', 'us', 'metric')
    print get_weather('Austin', 'us', 'metric')

    def get_city_by_zipcode(zipcode):
        try:
            return self.zip_codes[zipcode]['city']
        except Exception:
            raise CurrentWeatherException(code=5150,
                                          message=
                                          'Error: Zipcode not found in Zipcode data'
                                          )

    def get_weather_by_zipcode(zipcode):
        city = self.get_city_by_zipcode(zipcode)
        weather = self.get_weather(city, 'us', 'metric')
        return weather

class CurrentWeatherException(Exception):
    """Creates an exception"""
    def __init__(self, code, message):
        super(CurrentWeatherException, self).__init__()
        self.errno = code
        self.message = message

