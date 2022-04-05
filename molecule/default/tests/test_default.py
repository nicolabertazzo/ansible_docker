import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('file', [
    "/var/lib/docker/", 
    "/etc/systemd/system/docker.service.d/10-custom.conf",
    "/etc/docker/ssl/key.pem",
    "/etc/docker/ssl/cert.pem",
    "/etc/docker/ssl/ca.pem"])
def test_files(host, file):
    file = host.file(file)

    assert file.exists

def test_partition(host):
    assert host.block_device("/dev/sdb1").is_partition

def test_docker_service(host):
    docker = host.service("docker")

    assert docker.is_running
    assert docker.is_enabled