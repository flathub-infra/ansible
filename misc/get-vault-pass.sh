#!/bin/bash

exec gpg2 --batch --decrypt --quiet $(dirname $0)/vault-password.gpg
