if [ "$(whoami)" != "root" ]
then
echo "Sorry, you are not root!"
exit 1
fi
apt-get install qemu-user-static multistrap
export TARGET_ROOTFS_DIR=ev3-rootfs
multistrap -f multistrap.conf -d ${TARGET_ROOTFS_DIR}
cp /usr/bin/qemu-arm-static ${TARGET_ROOTFS_DIR}/usr/bin
mkdir -p ${TARGET_ROOTFS_DIR}/dev
mount --bind /dev ${TARGET_ROOTFS_DIR}/dev
chroot ${TARGET_ROOTFS_DIR} var/lib/dpkg/info/dash.preinst install
chroot ${TARGET_ROOTFS_DIR} dpkg --configure -a
cp -r py-smbus-python3 ${TARGET_ROOTFS_DIR}/home/py-smbus-python3
chroot ${TARGET_ROOTFS_DIR} /home/py-smbus-python3/build-smbus.sh
mkdir -p py-smbus-python3/build
cp -r ${TARGET_ROOTFS_DIR}/home/py-smbus-python3/build/lib.linux-armv* py-smbus-python3/build
umount ${TARGET_ROOTFS_DIR}/dev
ls ${TARGET_ROOTFS_DIR}/dev
echo "''''''''''''''''''''''''''"
echo "Warning!!"
echo "/dev may still mount at ${TARGET_ROOTFS_DIR}/dev"
echo "Do NOT remove ${TARGET_ROOTFS_DIR} until you check ${TARGET_ROOTFS_DIR}/dev"
echo "''''''''''''''''''''''''''"

