# -*- coding: utf-8 -*-
import yaml
from StringIO import StringIO
from . import response_cache


class YamlLoader(object):

    @classmethod
    def load(cls, file):
        raw_text = open(file, 'r').read()
        origin = yaml.load(StringIO(raw_text))
        raw_text = raw_text.format(
            app=origin['app_id'], version=origin['version'], date=origin['date'], media=origin['media'])
        return yaml.load(StringIO(raw_text))


class DataParser(object):

    def __init__(self, pattern):
        behavior_name, path = pattern.split('.')[0].replace('! ', ''), pattern.split('.')[1:]
        self.behavior = behavior_name
        self.path = path

    @classmethod
    def validate_pattern(cls, pattern):
        if isinstance(pattern, basestring) and pattern.startswith('! '):
            return True
        else:
            return False

    @classmethod
    def parse_json_path(cls, json_dict, path):
        ret = None
        for node in path:
            ret = json_dict[node]
        return ret

    def parse_data(self):
        if self.behavior not in response_cache:
            raise Exception('Behavior {} 尚未被执行'.format(self.behavior))
        real_value = self.parse_json_path(response_cache[self.behavior], self.path)
        return real_value

