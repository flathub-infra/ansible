# nginx

## Description

Install the nginx HTTP server and opens the HTTP and HTTPS ports in the
firewall. Note that the configuration does not contain any `server`
blocks. It's expected that the role user will provide the appropriate
`server` configurations in `/etc/nginx/conf.d`.

## Variables

* `nginx_network_connect`: Set the SELinux `httpd_can_network_connect`
  boolean to allow nginx to make network connections. This is needed
  when proxying to other http servers. The default is `no`.

* `nginx_resolvers`: DNS resolvers for upstream and OCSP responders.
  This is defined in the `http` context, so it can be overridden in the
  `server` and `location` context. The default is to use the host's
  resolvers as defined in `ansible_dns.nameservers`.
