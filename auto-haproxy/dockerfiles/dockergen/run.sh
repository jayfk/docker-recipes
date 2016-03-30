#!/bin/bash
/usr/local/bin/docker-gen -notify-sighup ${PROJECT}_${SERVICE}_1 -watch /etc/docker-gen/templates/haproxy.tmpl /usr/local/etc/haproxy/haproxy.cfg