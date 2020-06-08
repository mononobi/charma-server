# imovie-server

Server side application for imovie, personal movie collection manager.

# prerequisites

create an entry in /etc/hosts with 'imovie.server' value.

# code editing in pycharm

first you should execute the scripts/setup/install-dependencies.sh script.
then open the project in pycharm and it will create the required pipenv environment.
then you could start developing the application.

# running application in pycharm

add a new script in pycharm's edit configurations dialog and choose the src/start.py script.
then run or debug it.

# installation

to install the application in production environment, you must put a copy of pyrin
application main package in src directory beside imovie package. also a valid .env
file must be existed there.

based on different situations you could perform one of the following sections
to install the application:

A. if the server is raw and you want to perform installation for the first time,
   you should execute these scripts in order:

1. setup/scripts/initial-configure.sh
   - answering "Y" to "Force update all installed dependencies?"
   - answering "Y" to "Reboot system now?"
2. setup/scripts/install.sh
   - answering "N" to "Force update all installed dependencies?"
   - answering "Y" to "Perform a full installation?"

B. if the server is not raw (meaning that you have already executed
   setup/scripts/initial-configure.sh once on it) and you want to perform a full installation,
   you should execute this script:

1. setup/scripts/install.sh
   - answering "Y" to "Force update all installed dependencies?"
   - answering "Y" to "Perform a full installation?"

C. if you have already installed the application on the server before, you could run
   this script to only update the code and uwsgi configs without downtime:

1. setup/scripts/install.sh
   - answering "N" to "Force update all installed dependencies?"
   - answering "N" to "Perform a full installation?"

at any time if any of the dependencies should be updated or you needed to perform a full
installation, you could repeat the section B. but you must be aware
that performing the aforementioned section will cause a downtime to the application.

# uninstallation

to uninstall the application from system, you should execute the scripts/setup/uninstall.sh
script. be aware that uninstallation process will not make any backup of installed version.