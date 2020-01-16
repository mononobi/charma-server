#!/bin/bash

# installing dependencies.
./install-dependencies.sh

full_installation="n"
# shellcheck disable=SC2039
read -r -p "Perform a full installation? [y/N] " full_installation

full_installation_length=${#full_installation}
if [ "$full_installation_length" = "0" ]
then
    full_installation="n"
fi

# getting working directory path.
working_dir=$(pwd)

# user name that application should be accessible to it.
user_name=app_user

# checking that user_name is present, if not, create it.
user_exists=$(id -u $user_name > /dev/null 2>&1; echo $?)

if [ "$user_exists" != "0" ]
then
    # user does not exist, creating it.
    echo "Creating $user_name."
    adduser $user_name
else
    echo "$user_name is already present."
fi

# adding user_name into www-data and sudo groups.
usermod -aG sudo $user_name
usermod -aG www-data $user_name

service_file=/etc/systemd/system/imovie.server.service

# stopping current application service.
if [ "$full_installation" = "Y" ] || [ "$full_installation" = "y" ]
then
    if [ -f $service_file ]
    then
        echo "Stopping current application service."
        systemctl stop imovie.server.service
        systemctl disable imovie.server.service
    fi

    # making logging directory and log backup.
    if [ ! -d "/var/log/backup/imovie" ]
    then
        mkdir -p /var/log/backup/imovie/
    fi

    if [ -d "/var/log/imovie" ]
    then
        echo "Archiving and cleaning up previous logs."
        name=$(date "+%Y.%m.%d.%H.%M.%S")
        tar -czf /var/log/backup/imovie/"imovie.log.$name.tar.gz" /var/log/imovie
        rm -r /var/log/imovie
    fi

    mkdir -p /var/log/imovie/nginx

    # setting permissions for log directory.
    chown -R $user_name:www-data /var/log/imovie/
    chmod -R 770 /var/log/imovie/
fi

# making application backup directory and file.
if [ ! -d "/var/app_root/backup/imovie_server" ]
then
    mkdir -p /var/app_root/backup/imovie_server/
fi

if [ -d "/var/app_root/imovie_server" ]
then
    echo "Archiving and cleaning up previous installation."
    name=$(date "+%Y.%m.%d.%H.%M.%S")
    tar -czf /var/app_root/backup/imovie_server/"imovie_server.$name.tar.gz" /var/app_root/imovie_server

    if [ "$full_installation" = "Y" ] || [ "$full_installation" = "y" ]
    then
        rm -r /var/app_root/imovie_server
    else
        rm -r /var/app_root/imovie_server/app/
    fi
else
    if [ "$full_installation" = "Y" ] || [ "$full_installation" = "y" ]
    then
        mkdir -p /var/app_root/backup/imovie_server/
        echo "Performing fresh installation."
    else
        echo "Previous installation is incomplete, a full installation must be performed first."
        exit 1
    fi
fi

# making up required directory.
mkdir -p /var/app_root/imovie_server/app/

echo "Copying applications."
# copying pyrin application.
cp -r ../../src/pyrin/ /var/app_root/imovie_server/app/pyrin/

# copying imovie application.
cp -r ../../src/imovie/ /var/app_root/imovie_server/app/imovie/
cp ../../src/start.py /var/app_root/imovie_server/app/start.py
cp ../../src/wsgi.py /var/app_root/imovie_server/app/wsgi.py

# copying .env file.
cp ../../src/.env /var/app_root/imovie_server/app/.env

# copying pipenv required files.
cp ../../Pipfile.lock /var/app_root/imovie_server/Pipfile.lock
cp ../../Pipfile /var/app_root/imovie_server/Pipfile

if [ "$full_installation" = "Y" ] || [ "$full_installation" = "y" ]
then
    # creating pipenv environment.
    cd /var/app_root/imovie_server/ || exit 1
    export PIPENV_VENV_IN_PROJECT=1
    pipenv install --ignore-pipfile

    #returning to working directory.
    cd "$working_dir" || exit 1
else
    # updating dependencies from Pipfile.lock.
    cd /var/app_root/imovie_server/ || exit 1
    pipenv sync

    #returning to working directory.
    cd "$working_dir" || exit 1
fi

# setting the owner of directory.
chown -R $user_name /var/app_root/

if [ "$full_installation" = "Y" ] || [ "$full_installation" = "y" ]
then
    # configuring system.
    ./configure-system.sh

    # reloading configs
    systemctl daemon-reload

    echo "Starting application service."
    systemctl start imovie.server.service
    systemctl enable imovie.server.service

    echo "Starting nginx service."
    systemctl start nginx
    systemctl reload nginx
    ufw allow 'Nginx Full'
    ufw enable
else
    echo "Reloading application service."
    systemctl daemon-reload
    systemctl reload imovie.server.service
fi

echo
(sleep 5; echo -e "\e[0;32m** Installation completed **\e[0m")
echo

systemctl status imovie.server.service
