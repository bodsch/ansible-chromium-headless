# ansible role for chromium-headless


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

$ tox -e py37-ansible29 -- molecule test --scenario-name debian
```
