#!/bin/bash
until mysqladmin ping -h"mysql" -P"3306" -u"root" -p"1a2b3c4d" --silent; do
    echo "Esperando a MySQL..."
    sleep 2
done
echo "MySQL está listo!"