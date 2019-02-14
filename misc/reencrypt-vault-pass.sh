#!/bin/bash

exec gpg2 --batch --decrypt $(dirname $0)/vault-password.gpg | gpg --armor --recipient 487328A9 --recipient E06F63B5 --recipient B76C70E9 --recipient C7EC6914  -e -o $(dirname $0)/vault-password.gpg
