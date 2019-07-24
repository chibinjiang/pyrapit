# -*- coding: utf-8 -*-
# Json Query Language: http://jmespath.org/tutorial.html
import json
import traceback

import requests
from copy import deepcopy
from pprint import pprint
from . import response_cache
from .config import it_config
from .utils import DataParser


class Behavior(object):
    name = 'Behavior'

    def __init__(self, name=None):
        if name:
            self.name = name
        config = it_config.behaviors[self.name]
        self.validate_config(config)
        self.request_config = config['request']
        self.response_config = config['response']
        self.method = self.request_config['method']
        self.api = it_config.host + self.request_config['url'].format(app=it_config.app_id)
        self.args = self.request_config.get('data', {})
        for key in self.args:
            if isinstance(self.args[key], basestring):
                if '{version}' in self.args[key]:
                    self.args[key] = self.args.format(version=it_config.version)

    @classmethod
    def validate_config(cls, config):
        """
        校验 config
        :param config: it_config.behaviors[self.name]
        :return:
        """
        if 'request' not in config:
            raise Exception("没有request")
        if 'response' not in config:
            raise Exception("没有response")
        return True

    @property
    def dependencies(self):
        return self.request_config.get('dependencies', [])

    def parse_args(self):
        args = deepcopy(self.args)
        for key in args:
            value = args[key]
            if DataParser.validate_pattern(value):
                args[key] = DataParser(value).parse_data()
            elif isinstance(value, list):
                new_values = list()
                for _value in value:
                    if DataParser.validate_pattern(_value):
                        new_value = DataParser(_value).parse_data()
                        new_values.append(new_value)
                    else:
                        new_values.append(_value)
                args[key] = new_values
        self.args = args
        pprint(self.args)
        return self.args

    def send_request(self):
        self.parse_args()
        print "Behavior {} send request ...".format(self.name)
        header = {'Authorization': it_config.authorization, 'Content-Type': 'application/json'}
        if self.method == 'GET':
            response = requests.get(self.api, query_string=self.args, headers=header)
        elif self.method == 'POST':
            response = requests.post(self.api, data=json.dumps(self.args), headers=header)
        else:
            raise Exception("Unknown Requests Method: {}".format(self.method))
        if response.status_code != 200:
            print response.text
            raise Exception("Wrong HTTP Status Code: {}".format(response.status_code))
        try:
            json_data = response.json()
            if json_data.get('meta', {}).get('code', 200) != 200:
                print response.text
                raise Exception("Wrong HTTP Status Code: {}".format(response.status_code))
        except Exception as e:
            print response.text
            traceback.print_exc()
            return
        response_cache[self.name] = json_data
        return json_data

    def gen_report(self):
        pass

