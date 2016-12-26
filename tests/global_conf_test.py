import os

from src.global_conf import GlobalConf
from src.impl.service import Service


def test_config_content():
    services = GlobalConf.services

    for key, service_conf in services.items():
        assert key == service_conf.name
        assert os.path.isfile(service_conf.path)


