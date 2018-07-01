#!/bin/sh

sudo chmod 755 /usr/src/linux/include/generated
sudo chmod 644 /usr/src/linux/include/generated/*.h

sudo chmod 755 /usr/src/linux/include/config
sudo chmod 644 /usr/src/linux/include/config/auto.conf

sudo chmod 755 /usr/src/linux/arch/x86/include/generated
sudo chmod 755 /usr/src/linux/arch/x86/include/generated/uapi
sudo chmod 755 /usr/src/linux/arch/x86/include/generated/uapi/asm
sudo chmod 644 /usr/src/linux/arch/x86/include/generated/uapi/asm/*.h
sudo chmod 755 /usr/src/linux/arch/x86/include/generated/asm
sudo chmod 644 /usr/src/linux/arch/x86/include/generated/asm/*.h

sudo chmod 755 /usr/src/linux/include/generated/uapi
sudo chmod 755 /usr/src/linux/include/generated/uapi/linux
sudo chmod 644 /usr/src/linux/include/generated/uapi/linux/*.h

sudo chmod 755 /usr/src/linux/scripts/basic/fixdep
sudo chmod 755 /usr/src/linux/scripts/mod/modpost
sudo chmod o+r /usr/src/linux/vmlinux


# added 2018-05-13
sudo chmod o+rx "/lib/modules/$(uname -r)"
sudo chmod o+rx /usr/src/linux/tools/objtool/objtool
sudo chmod o+rx /usr/src/linux/scripts/recordmcount
sudo chmod o+rx /usr/src/linux/scripts/genksyms/genksyms
