SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd $SCRIPTPATH
export LANG=C
rm -r i2c-tools-3.1.1
rm *.deb
apt-get source i2c-tools
cd i2c-tools-3.1.1
patch -p1<../python3.patch
dpkg-buildpackage -uc -B
