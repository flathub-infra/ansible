# dehydrated

## Description

Installs and runs the dehydrated Let's Encrypt client to obtain SSL
certificates. Note that an HTTP server must be running to receive the
ACME challenged from Let's Encrypt. This likely means that the HTTP
server role (e.g., `nginx`) should be included before this role so that
its handlers run before `dehydrated --cron`.

## Variables

* `dehydrated_domains` - A list of domains to acquire certificates for.
  Each entry will be a line in `/etc/dehydrated/domains.txt`.

* `dehydrated_sync_domains` - A list of primary domain names whose
  certificates should be synced to a remote host.

* `dehydrated_sync_hosts` - A list of hostnames to sync certificates to.
  The certificates will be sent via `rsync` as the `certsync` user.
