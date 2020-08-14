#!/bin/bash

for i in gpg2 gpg; do GPG=$i; which $i >/dev/null && break; done

exec ${GPG} --batch --decrypt --quiet $(dirname $0)/vault-password.gpg
