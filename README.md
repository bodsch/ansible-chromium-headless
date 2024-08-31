
# Ansible Role: `chromium-headless`

Ansible role to install chromium-headless


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-chromium-headless/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-chromium-headless)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-chromium-headless)][releases]
[![Ansible Downloads](https://img.shields.io/ansible/role/d/bodsch/chromium_headless?logo=ansible)][galaxy]

[ci]: https://github.com/bodsch/ansible-chromium-headless/actions
[issues]: https://github.com/bodsch/ansible-chromium-headless/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-chromium-headless/releases
[galaxy]: https://galaxy.ansible.com/ui/standalone/roles/bodsch/chromium_headless/


## Requirements & Dependencies

Nothing


## Operating systems

Tested on

* Debian based
    - Debian 10 / 11
    - Ubuntu 20.04 / 22.04

## usage

```yaml
chromium_headless_display: ":20.0"
chromium_headless_screen_geometry: "1440x900x24"

chromium_headless_chromedriver_port: 4444
chromium_headless_chromedriver_whitelisted_ips: "127.0.0.1"
chromium_headless_chromedriver_url_base: ''
chromium_headless_chromedriver_extra_args: ''
```

### Variables

[defaults/main.yml](defaults/main.yml)

|*Variable*  | *Default Value* | *Description* |
| --- | --- | --- |
| `chromium_headless_display` | `20.0` | headless display port  |
| `chromium_headless_screen_geometry` | `1440x900x24` | screen geometry |
| `chromium_headless_chromedriver_port` | `4444` | Port |
| `chromium_headless_chromedriver_whitelisted_ips` | `127.0.0.1` | whitelisted IPs |
| `chromium_headless_chromedriver_url_base` | `''` | url base |
| `chromium_headless_chromedriver_extra_args` | `''` | extra args |


### Example Playbook

```
 - hosts: all
   roles:
     - role: chromium-headless
```


---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

`FREE SOFTWARE, HELL YEAH!`
