
ansible role to install chromium-headless


[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bodsch/ansible-chromium-headless/CI)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-chromium-headless)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-chromium-headless)][releases]

[ci]: https://github.com/bodsch/ansible-chromium-headless/actions
[issues]: https://github.com/bodsch/ansible-chromium-headless/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-chromium-headless/releases


## Requirements & Dependencies

Nothing


### Operating systems

Tested on

* Debian 9 / 10
* Ubuntu 18.04 / 20.04
* CentOS 8
* Oracle Linux 8

## Example Playbook

```
 - hosts: all
   roles:
     - role: chromium-headless
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

|*Variable*  | *Default Value* | *Description* |
| --- | --- | --- |
| `chromium_headless_display` | `20.0` | headless display port  |
| `chromium_headless_screen_geometry` | `1440x900x24` | screen geometry |
| `chromium_headless_chromedriver_port` | `4444` | Port |
| `chromium_headless_chromedriver_whitelisted_ips` | `127.0.0.1` | whitelisted IPs |
| `chromium_headless_chromedriver_url_base` | `''` | url base |
| `chromium_headless_chromedriver_extra_args` | `''` | extra args |

## Tests

```
$ tox -e py37-ansible29 -- molecule test
```
## License

Apache

