

class Service:

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.conf = {'port': 80}

    @property
    def port(self):
        return self.conf['port']

    @property
    def dockerfile_path(self):
        return self.conf.get('dockerfile_path', './Dockerfile')


    
