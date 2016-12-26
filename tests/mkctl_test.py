import mock
import pytest
from src import mkctl
from src.impl import docker
from src.impl.service import Service



def test_stage():
    docker_client = mock.create_autospec(docker.Client)
    mkctl.stage(docker_client, Service('test_service', ''))
   
