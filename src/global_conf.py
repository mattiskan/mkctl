import yaml
from src.impl.service import Service
from src.impl.util import classproperty

class GlobalConf:

    stage_port = 8080

    @classproperty
    def services(self):
        with open('config.yaml', 'r') as rfile:
            config = yaml.load(rfile)

        return {name: Service(name, path) for name, path in config['services'].items()}
