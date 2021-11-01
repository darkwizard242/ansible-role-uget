import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'uget'
PACKAGE_BINARY = '/usr/bin/uget'


def test_uget_package_installed(host):
    """
    Tests if uget is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_uget_binary_exists(host):
    """
    Tests if uget binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_uget_binary_file(host):
    """
    Tests if uget binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_uget_binary_which(host):
    """
    Tests the output to confirm uget's binary location.
    """
    assert host.check_output('which uget') == PACKAGE_BINARY
