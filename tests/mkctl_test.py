import mock
import pytest
from src import mkctl
from src.impl import docker
from src.impl.service import Service
from contextlib import contextmanager


@contextmanager
def mocked_actions():
    mocks = {}
    patchers = []
    
    for action in mkctl.user_actions:
        patcher =  mock.patch.object(mkctl, action, autospec=True)
        patchers.append(patcher)
        mocks[action] = patcher.__enter__()

    yield mocks

    for patcher in patchers:
        patcher.__exit__()

def test_main():
    with mocked_actions() as action_mocks:
        mkctl.main(['mkctl.py', 'stage', 'http_test_service'])

    assert action_mocks['stage'].call_count == 1
    assert sum(action_mock.call_count for action_mock in action_mocks.values()) == 1

    args, kwargs = action_mocks['stage'].call_args
    assert isinstance(args[0], docker.Client) and isinstance(args[1], Service)
