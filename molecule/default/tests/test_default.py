# coding: utf-8
from __future__ import unicode_literals

from ansible.parsing.dataloader import DataLoader
from ansible.template import Templar

import pytest
import json
import os

import testinfra.utils.ansible_runner

import pprint
pp = pprint.PrettyPrinter()

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def pp_json(json_thing, sort=True, indents=2):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


def base_directory():
    cwd = os.getcwd()

    if ('group_vars' in os.listdir(cwd)):
        directory = "../.."
        molecule_directory = "."
    else:
        directory = "."
        molecule_directory = "molecule/{}".format(os.environ.get('MOLECULE_SCENARIO_NAME'))

    return directory, molecule_directory


@pytest.fixture()
def get_vars(host):
    """

    """
    base_dir, molecule_dir = base_directory()
    distribution = host.system_info.distribution
    operation_system = None

    if distribution in ['debian', 'ubuntu']:
        operation_system = "debian"
    elif distribution in ['redhat', 'ol', 'centos', 'rocky', 'almalinux']:
        operation_system = "redhat"
    elif distribution in ['arch', 'artix']:
        operation_system = "archlinux"

    file_defaults = f"file={base_dir}/defaults/main.yml name=role_defaults"
    file_vars = f"file={base_dir}/vars/main.yml name=role_vars"
    file_molecule = f"file={molecule_dir}/group_vars/all/vars.yml name=test_vars"
    file_distibution = f"file={base_dir}/vars/{operation_system}.yml name=role_distibution"

    defaults_vars = host.ansible("include_vars", file_defaults).get("ansible_facts").get("role_defaults")
    vars_vars = host.ansible("include_vars", file_vars).get("ansible_facts").get("role_vars")
    distibution_vars = host.ansible("include_vars", file_distibution).get("ansible_facts").get("role_distibution")
    molecule_vars = host.ansible("include_vars", file_molecule).get("ansible_facts").get("test_vars")

    ansible_vars = defaults_vars
    ansible_vars.update(vars_vars)
    ansible_vars.update(distibution_vars)
    ansible_vars.update(molecule_vars)

    templar = Templar(loader=DataLoader(), variables=ansible_vars)
    result = templar.template(ansible_vars, fail_on_undefined=False)

    return result


def test_directories(host):
    """
      test existing directories
    """
    distribution = host.system_info.distribution

    directories = []

    if distribution == 'debian':
        directories.append("/usr/lib/chromium")
    elif distribution == 'ubuntu':
        directories.append("/usr/lib/chromium-browser")
    elif distribution in ['centos', 'redhat']:
        directories.append("/usr/lib64/chromium-browser")

    for dirs in directories:
        d = host.file(dirs)
        assert d.is_directory
        assert d.exists


def test_files(host):
    """
      test existing files
    """
    distribution = host.system_info.distribution

    files = []
    files.append("/etc/profile.d/chromedriver.sh")

    if distribution == 'debian':
        files.append("/usr/bin/chromedriver")
    elif distribution == "ubuntu":
        files.append("/usr/lib/chromium-browser/chromedriver")

    elif distribution in ['centos', 'redhat']:
        files.append("/usr/lib64/chromium-browser/chromedriver")

    for _file in files:
        f = host.file(_file)
        assert f.exists
        assert f.is_file


def test_profile(host):

    config_file = "/etc/profile.d/chromedriver.sh"
    content = host.file(config_file).content_string

    assert 'DISPLAY=":20.0"' in content
    assert 'SCREEN_GEOMETRY="1440x900x24"' in content
    assert 'CHROMEDRIVER_PORT=4444' in content
    assert 'CHROMEDRIVER_WHITELISTED_IPS="127.0.0.1"' in content
    assert 'CHROMEDRIVER_URL_BASE=""' in content
    assert 'CHROMEDRIVER_EXTRA_ARGS=""' in content
