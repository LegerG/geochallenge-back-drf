#! /bin/bash

user="legw3018"
home="/home/$user"
interpreter="python"
version="3.10"
app_name="$1"
domain="gwenael-leger.fr"
app_root="$home/$app_name"

create_app() {
    echo "Creating app..."

    cloudlinux-selector create --json \
        --interpreter "$interpreter" \
        --app-root "$app_root" \
        --domain "$app_name.$domaine" \
        --app_uri "" \
        --version "$version" \
        --startup-file "geochallenge/wsgi.py" \
        --passenger-log-file "$home/logs/$app_name/passenger.log" \
        --entry-point "application"
}

move_files() {
    echo "Moving files..."

    cp -r "$home/repositories/$app_name.git" "$app_root"
}

start_app() {
    echo "Starting app..."

    cloudlinux-selector start --json \
        --interpreter "$interpreter" \
        --app-root "$app_root" \
        --user "$user"
}

install_package() {
    echo "Installing package..."

    cloudlinux-selector install-modules --json \
        --interpreter "$python" \
        --user "$user" \
        --app-root "$app_root" \
        --requirements-file requirements.txt
}

create_app

move_files

install_package

start_app