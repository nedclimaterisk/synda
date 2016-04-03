# Synda upgrade guide (Debian package installation)

## Synopsis

This document contains instructions to upgrade to new Synda version using Debian package.

## Procedure

### Pre-upgrade

Backup /etc/synda/sdt and /var/log/synda/sdt folders

### Upgrade

Remove previous package version using command below:

    dpkg -P synda

Install new package version using [this guide](sdt/doc/install_deb.md)


### Post-upgrade

As configuration files located in $ST_HOME/conf may have been reinitialized
during upgrade, you need to check if parameters are still correctly set (e.g.
openid, password..).

Note: you can use a diff program to compare post-upgrade configuration files
over pre-upgrade configuration files (from the backup).