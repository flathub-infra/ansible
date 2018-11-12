# nginx

## Description

Install the nginx HTTP server and opens the HTTP and HTTPS ports in the
firewall. Note that the configuration does not contain any `server`
blocks. It's expected that the role user will provide the appropriate
`server` configurations in `/etc/nginx/conf.d`.
