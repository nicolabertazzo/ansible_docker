import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file', [("/var/lib/docker/")])
def test_docker_partition(host, file):
    file = host.file(file)

    assert file.exists