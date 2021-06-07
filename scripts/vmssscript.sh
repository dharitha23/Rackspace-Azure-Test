#!/bin/bash
sudo apt-get -y update

# install Apache2
sudo apt-get -y install apache2

# write some HTML
echo \<center\>\<h1\>Hello World from $Hostname\</h1\>\<br/\>\</center\> > /var/www/Helloworld.html

# restart Apache
sudo systemctl restart apache2.service