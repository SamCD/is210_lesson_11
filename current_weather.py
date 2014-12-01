#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 11, current_weather file"""

import decimal
import json
import os
import urllib2


base_url = 'http://api.openweathermap.org/data/2.5/weather'


class CurrentWeatherException(Exception):
    """Creates an exception"""
    def __init__(self, code, message):
        Exception.__init__(self, code, message)
        super(CurrentWeatherException, self).__init__()
        self.errno = code
        self.message = message

        
class CurrentWeather(object):
    """Creates a current weather class"""
    

    def __init__(self, zipcode_data="zipcode_database.csv"):
        self.zip_codes = {}
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'
        self.read_csv(zipcode_data)

    def get_weather(self, city, country, units='metric'):
        """Retrieves weather data

        Args: city, country, units (default is metric)

        Ex: get_weather('anytown', 'us'):
        >>> {u'pressure': 1017, u'temp_min': 3,
        u'temp_max': 6, u'temp': 4.67, u'humidity': 44}"""
        
        api_query = '{}?units={}&q={},{}'.format(
            base_url, units, city, country
        )

        try:
            response = urllib2.urlopen(api_query)
        except urllib2.HTTPError as error:
            raise CurrentWeatherException(
                error.code,
                'Error: {} {}'.format(error.code, error.msg)
            )

        return json.load(response)['main']

    def read_csv(self, csv_path):
        """Reads CSV files"""

        if os.path.exists(csv_path):
            try:
                fhandler = open(csv_path, 'r')

                line = file_obj.readline()
                line = file_obj.readline()

                while line:
                    parts = line.strip().split(',')
                    parts = [part.strip() for part in parts]
                        
                    self.zip_codes[parts[0]] = {
                        'city': parts[1],
                        'state': parts[2],
                        'latitude': decimal.Decimal(parts[3]),
                        'longitude': decimal.Decimal(parts[4]),
                        'country': parts[5]
                        }

            except IOError:
                raise CurrentWeatherException(
                    4151,
                    'Error reading {}'.format(csv_path)
                )
            
            finally:
                if file_obj is not None:
                    file_obj.close()
            
        else:
            raise CurrentWeatherException(
                9010,
                message='CSV zipcode database not found'
            )
            

    print get_weather('New York', 'us', 'metric')
    print get_weather('San Francisco', 'us', 'metric')
    print get_weather('Austin', 'us', 'metric')


    def get_city_by_zipcode(self, zipcode):
        """Identifies city given zipcode

        Args: zipcode

        ex: get_city_by_zipcode('10013')
        >>> 'New York'"""
        try:
            zipcode = self.zip_codes[zipcode]
        except KeyError:
            raise CurrentWeatherException(
                5150,
                'Error: Zipcode not found in Zipcode data'
            )
        return zipcode['city']


    def get_weather_by_zipcode(self, zipcode):
        """Retrieves weather data given zipcode

        Args: zipcode

        Ex: get_weather_by_zipcode('10001')
        >>> {u'pressure': 1017, u'temp_min': 3, u'temp_max': 6,
        u'temp': 4.67, u'humidity': 44}"""
        city = self.get_city_by_zipcode(zipcode)
        weather = self.get_weather(city, 'us')
        return weather
