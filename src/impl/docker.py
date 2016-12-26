import subprocess
from time import sleep

class Client(object):
    def __init__(self, host='', port=0):
        if host and port:
            self.host_str = 'tcp://{}:{}'.format(host, port)
        else:
            self.host_str = ''

    def wait_for(self, sha):
        sleep(0.3)

    def start(self):
        pass

    def build(self, path, tag='', fpath=''):
        options = ['-q']
        if tag:
            options.append('-t')
            options.append(tag)
        if fpath:
            options.append('-f')
            options.append(fpath)
        

        return self._exec(['docker', 'build'] + options + [path])
    
    def ps(self, list_all=False):
        options = []
        if list_all:
            options.append('-a')

        return self._exec(['docker', 'ps'] + options)

    def images(self, list_all=False):
        options = []
        if list_all:
            options.append('-a')
        
        return self._exec(['docker', 'images'] + options)
    
    def stop(self, sha):
        self._exec(['docker', 'stop', sha])

    def rm(self, sha):
        self._exec(['docker', 'rm', sha])
        
    def run(
        self,
        container,
        bind_ports=(),
        volumes=(),
        background=True,
        privileged=False,
        extra_args=None,
        cmd=[],
    ):
        if any(len(bind_port) != 2 for bind_port in bind_ports):
            raise
        
        options = []
            
        for bind_port in bind_ports:
            options.append('-p')
            options.append('{}:{}'.format(*bind_port))
        if privileged:
            options.append('--privileged')
        if background:
            options.append('-d')
        for vol in volumes:
            options.append('-v')
            options.append(':'.join(vol))
        if extra_args:
            if not hasattr(extra_args, '__iter__'):
                extra_args = [extra_args]
        else:
            extra_args = []

        return self._exec(['docker', 'run'] + options + [container] + extra_args + cmd)

    def _exec(self, cmd):
        if self.host_str:
            # inserts hostname for remote clients
            cmd.insert(1, '-H')
            cmd.insert(2, self.host_str)

        #print(*cmd)
        return subprocess.check_output(cmd).decode('utf-8').strip()
        
