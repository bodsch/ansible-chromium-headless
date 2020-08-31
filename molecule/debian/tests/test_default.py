import pytest
import os
#import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        vars_files)["ansible_facts"]["role_vars"])

    return ansible_vars


@pytest.mark.parametrize("files", [
    "/etc/profile.d/chromedriver.sh",
    "/usr/lib/chromium/chromium",
    "/usr/bin/chromedriver",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file
