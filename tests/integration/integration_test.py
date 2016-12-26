import pytest
import requests
import time

from src.impl import docker
from src.impl.service import Service
from src.mkctl import stage
from src.global_config import GlobalConfig


DIND_PORT = 12345
DOCKER_PORT = 2375


@pytest.yield_fixture
def sandbox_client():
    """ Tests run against docker-in-docker(DIND) to not pollute
    the local docker process with orphaned containers.
    """
    
    localclient = docker.Client()
    sha = localclient.run(
        'docker:dind',
        bind_ports=[
            (DIND_PORT, DOCKER_PORT),
            (GlobalConfig.stage_port, GlobalConfig.stage_port)
        ],
        privileged=True,
    )
    
    try:
        localclient.wait_for(sha)
        yield docker.Client('localhost', DIND_PORT)
    finally:
        localclient.stop(sha)
        localclient.rm(sha)


def test_run_in_sandbox(sandbox_client):
    """ Simple docker in docker test """
    assert len(sandbox_client.ps(list_all=True).split('\n')) == 1  # header line

    sha = sandbox_client.run('hello-world')  # any small container should do
    assert len(sandbox_client.ps(list_all=True).split('\n')) == 2

    sandbox_client.stop(sha)
    sandbox_client.rm(sha)
    assert len(sandbox_client.ps(list_all=True).split('\n')) == 1


@pytest.fixture
def http_service():
    return Service('test_http', '')


def test_stage(sandbox_client, http_service):
    stage(sandbox_client, http_service)

    sandbox_client.wait_for(None)
    assert requests.get(
        'http://localhost:{port}/'.format(port=GlobalConfig.stage_port),
    ).status_code == 200
