# -*- coding: utf-8 -*-
from . import *
from .utils import YamlLoader


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
        return self.config['version']

    @property
    def authorization(self):
        return 'token ' + self.config['token']


it_config = ITConfig()

