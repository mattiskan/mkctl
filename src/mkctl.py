from src.global_config import GlobalConfig
from src.impl import docker
from src.impl.cli import get_user_action
from src.impl.cli import define_user_action


@define_user_action
def stage(docker_client, service):
    build(docker_client, service)
    _unstage(docker_client, service)
    
    sha = docker_client.build(
        path='testing/services/http_server/',
    )
    docker_client.run(
        sha,
        bind_ports=[(GlobalConfig.stage_port, 80)],
        background=True,
    )


def _unstage(docker_client, service):
    pass


@define_user_action
def deploy(docker_client, service):
    stage(docker_client, service)
    pass


@define_user_action
def build(docker_client, service):
    pass


@define_user_action
def restart(docker_client, service):
    pass


if __name__ == '__main__':
    docker_client = docker.Client()

    action = get_user_action()
    action(docker_client, None)
