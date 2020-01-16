#!/bin/bash

remove="n"
# shellcheck disable=SC2039
read -r -p "Uninstall 'imovie_server' application? [y/N] " remove

service_file=/etc/systemd/system/imovie.server.service
nginx_file=/etc/nginx/sites-available/imovie.server.nginx
nginx_symlink=/etc/nginx/sites-enabled/imovie.server.nginx

if [ "$remove" = "Y" ] || [ "$remove" = "y" ]
then
    if [ -f $service_file ]
    then
        echo "Stopping current application service."
        systemctl stop imovie.server.service
        systemctl disable imovie.server.service
        rm -r $service_file
    fi

    if [ -d "/var/log/imovie" ]
    then
        rm -r /var/log/imovie/*
    fi

    if [ -d "/var/app_root/imovie_server" ]
    then
        rm -r /var/app_root/imovie_server/
    fi

    if [ -f $nginx_file ]
    then
        echo "Removing application nginx configs."
        rm $nginx_file
        rm $nginx_symlink

        systemctl daemon-reload
        systemctl start nginx
        systemctl reload nginx
    fi

    echo
    echo -e "\e[0;32m** Uninstallation completed **\e[0m"
    echo
fi
