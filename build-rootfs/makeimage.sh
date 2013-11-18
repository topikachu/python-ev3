#! /bin/bash


error_out () {
    echo "$1"
    exit 1
}

if [  $# != 3 ]; then
    error_out "makeimage.sh <uImage> <rootfs dir> <image name>"
fi
if [ ! -f $1 ]; then
    error_out "can't find uImage $1"
fi
if [ ! -f $2/etc/issue ]; then
    error_out "can't find correct directory of rootfs $2"
fi
uImage=$1
rootfs=$2
image=$3
rm $image
pv -tpreb /dev/zero | dd of=$image bs=64M count=1048576
sudo losetup /dev/loop0 $image
echo "n
p
1

+64M
t
b
n
p
2


p
w
"|sudo fdisk /dev/loop0


sudo losetup -o 1M --sizelimit 64M /dev/loop1 /dev/loop0
sudo losetup -o 65M /dev/loop2 /dev/loop0
sudo mkfs.msdos -n LMS2012 /dev/loop1
sudo mkfs.ext3 -L LMS2012_EXT /dev/loop2

mkdir /tmp/lms2012
mkdir /tmp/lms2012_ext
sudo mount /dev/loop1 /tmp/lms2012
sudo mount /dev/loop2 /tmp/lms2012_ext

sudo cp $uImage /tmp/lms2012
sudo cp -R  $rootfs/* /tmp/lms2012_ext
sync
sudo umount /tmp/lms2012
sudo umount /tmp/lms2012_ext
rmdir /tmp/lms2012
rmdir /tmp/lms2012_ext

sudo losetup -d /dev/loop2
sudo losetup -d /dev/loop1
sudo losetup -d /dev/loop0