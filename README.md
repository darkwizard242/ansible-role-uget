[![build-test](https://github.com/darkwizard242/ansible-role-uget/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-uget/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-uget/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-uget/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/uget) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-uget&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-uget) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-uget&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-uget) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-uget&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-uget) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-uget?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-uget?color=orange&style=flat-square)

# Ansible Role: uget

Role to install (_by default_) [uget](https://ugetdm.com/) package or uninstall (_if passed as var_) on **Debian/Ubuntu** and **EL** systems. **uget** is a multi-platform open source download manager.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
uget_app: uget
uget_desired_state: present
```

### Variables table:

Variable           | Description
------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------
uget_app           | Defines the app to install i.e. **uget**
uget_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **uget** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.uget
```

For customizing behavior of role (i.e. installation of latest **uget** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.uget
  vars:
    uget_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **uget** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.uget
  vars:
    uget_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-uget/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
