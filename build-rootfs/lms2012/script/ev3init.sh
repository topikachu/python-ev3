#!/bin/bash


echo "Setting up VirtualDrive...";
mount -t tmpfs tmpfs /mnt/tmpdisk/ -o size=4M
dd if=/dev/mtd4 of=/mnt/tmpdisk/data.tgz bs=64k > /dev/null 2>&1
tar -xzf /mnt/tmpdisk/data.tgz -C /mnt/ramdisk/ > /dev/null 2>&1
umount /mnt/tmpdisk/
if [ ! -d /mnt/ramdisk/settings ]; then
  tar -xzf /etc/def_sett.tgz -C /mnt/ramdisk/
  echo "Default Settings in use..."
fi

#Read name from filesystem + update hostname 
NAME="EV3"
while read LINE
do
#    echo $LINE
    NAME=$LINE
done < "/mnt/ramdisk/settings/BrickName"
#hostname $NAME
#bluetoothd -n > /dev/null 2>&1 &

echo "Initialize Bluetooth..."
#Read Hw version from eeprom and save it in HwId file
Hw1=$(eeprog /dev/i2c-1 0x50 -16 -r 0x3F00:1 -x -f -q)
Hw2=$(eeprog /dev/i2c-1 0x50 -16 -r 0x3F01:1 -x -f -q)
Hw1=0x${Hw1//3f00| /}
Hw2=0x${Hw2//3f01| /}
Hw1=${Hw1//[[:space:]]}
Hw2=${Hw2//[[:space:]]}

if [ $((Hw1 ^ Hw2)) == 255 ]; then
  echo -e "HwId="${Hw1//0x/} > /mnt/ramdisk/settings/HwId
  adr=$(eeprog /dev/i2c-1 0x50 -16 -r 0x3F06:6 -x -f -q)
  STRING=${adr//3f06| /}
else
  echo -e "HwId=03" > /mnt/ramdisk/settings/HwId
  adr=$(eeprog /dev/i2c-1 0x50 -16 -r 0x3F00:6 -x -f -q)
  STRING=${adr//3f00| /}
fi
#----------------------------------------
# OPTIMIZE THIS SECTION

#Save Bluetooth address in file
echo -e ${STRING//[[:space:]]} > /mnt/ramdisk/settings/BTser

#Remove first 2 spaces
STRING=${STRING/  /}
#Replace spaces with :
STRING=${STRING// /:}

#Remove last character
STRING="${STRING%?}"

#---------------------------------------------
#Invert string
STRING=`echo $STRING | sed "s/\(.*\):\(.*\):\(.*\):\(.*\):\(.*\):\(.*\)/\6:\5:\4:\3:\2:\1/"`

sleep 2
#hciattach /dev/ttyS2 texas 2000000 "flow" "nosleep" $STRING
#sdptool add SP
