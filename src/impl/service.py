

class Service:

    def __init__(self, name, config_path):
        self.name = name
        self.conf = {'port': 80}

    @property
    def port(self):
        return self.conf['port']

    @property
    def dockerfile_path(self):
        return self.conf.get('dockerfile_path', './Dockerfile')

    
