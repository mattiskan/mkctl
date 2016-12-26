import sys
import argparse

from src.global_conf import GlobalConf
from src.impl import docker

user_actions = []

def user_action(function):
    user_actions.append(function.__name__)
    return function

@user_action
def stage(docker_client, service):
    build(docker_client, service)
    _unstage(docker_client, service)
    
    sha = docker_client.build(service.build_path)
    docker_client.run(
        sha,
        bind_ports=[(GlobalConf.stage_port, service.port)],
        background=True,
    )
    print('{} has been staged on port'.format(service.name, service.port))

def _unstage(docker_client, service):
    pass


@user_action
def deploy(docker_client, service):
    stage(docker_client, service)
    pass


@user_action
def build(docker_client, service):
    pass


@user_action
def restart(docker_client, service):
    pass


def main(argv):
    args = parse_args(argv[1:])
    docker_client = docker.Client()
    
    user_action_function = globals()[args.action]
    user_action_function(docker_client, GlobalConf.services[args.service])

    
def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=user_actions)
    parser.add_argument('service', choices=GlobalConf.services.keys())

    return parser.parse_args(argv)


if __name__ == '__main__':
    main(sys.argv)
