#!/bin/bash
# -*- ENCODING: UTF-8 -*-
cd ~
apt-get install aptitude
estado=`aptitude show pyqt4-dev-tools | grep Estado`
if [ "$estado" != "Estado: instalado" ]; then
apt-get install pyqt4-dev-tools
fi

estado=`aptitude show python-dateutil | grep Estado`
if [ "$estado" != "Estado: instalado" ]; then
apt-get install python-dateutil
fi

estado=`aptitude show python-kde4-dev | grep Estado`
if [ "$estado" != "Estado: instalado" ]; then
apt-get install python-kde4-dev
fi