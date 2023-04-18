#!/usr/bin/env bash
# This script installs MySQL 5.7.x

# Get and install MySQL respository
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

#    During installation
#+   select Ubuntu Bionic/MySQL Server and Cluster/mysql-5.7 

# Update APT repository
sudo apt update

