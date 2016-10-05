#!/bin/sh

#~ Jon Ernster
#~ 10/04/16

echo status | hbase shell
echo "status 'simple'" | hbase shell
echo "status 'summary'" | hbase shell
echo "status 'detailed'" | hbase shell
echo version | hbase shell
echo whoami | hbase shell
