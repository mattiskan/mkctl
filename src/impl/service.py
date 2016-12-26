import yaml
import os.path


class Service:

    def __init__(self, name, conf_path):
        self.name = name
        self.conf_path = conf_path
        with open(conf_path, 'r') as rfile:
            self.conf = yaml.load(rfile) or {}

    @property
    def port(self):
        return self.conf.get('port', 80)

    @property
    def build_path(self):
        return self.conf.get('path', os.path.dirname(self.conf_path))

    @property
    def dockerfile_path(self):
        return self.conf.get('dockerfile_path', './Dockerfile')


    
