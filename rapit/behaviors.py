# -*- coding: utf-8 -*-
import os
import json
import yaml
import requests
from io import StringIO
here = os.path.abspath(os.path.dirname(__file__))


class YamlLoader(object):

    @classmethod
    def load(cls, file):
        raw_text = open(file, 'r').read()
        origin = yaml.load(StringIO(raw_text))
        raw_text = raw_text.format(app=origin['app_id'], version=origin['version'])
        return yaml.load(StringIO(raw_text))


class ITConfig(object):
    @property
    def config(self):
        return YamlLoader.load(os.path.join(here, 'behavior_args.yaml'))

    @property
    def host(self):
        return self.config['host']

    @property
    def app_id(self):
        return self.config['app_id']

    @property
    def behaviors(self):
        return self.config['behaviors']

    @property
    def version(self):
        return it_config['version']

    @property
    def authorization(self):
        return 'token ' + self.config['token']


it_config = ITConfig()


class Behavior(object):
    name = 'Behavior'

    def __init__(self):
        config = it_config.behaviors[self.name]
        self.validate_config(config)
        self.request_config = config['request']
        self.response_config = config['response']
        self.method = self.request_config['method']
        self.api = it_config.host + self.request_config['url'].format(app=it_config.app_id)
        self.args = self.request_config.get('data', {})

    @classmethod
    def validate_config(cls, config):
        """
        校验 config
        :param config: it_config.behaviors[self.name]
        :return:
        """
        if 'request' not in config:
            raise Exception("")
        if 'response' not in config:
            raise Exception("")
        return True

    @property
    def dependencies(self):
        return self.request_config.get('dependencies', [])

    def set_request(self):
        header = {'Authorization': it_config.authorization, 'Content-Type': 'application/json'}
        if self.method == 'GET':
            response = requests.get(self.api, query_string=self.args, headers=header)
        elif self.method == 'POST':
            response = requests.post(self.api, data=json.dumps(self.args), headers=header)
        else:
            raise Exception("Unknown Requests Method: {}".format(self.method))
        return response.json()

    def gen_report(self):
        pass

