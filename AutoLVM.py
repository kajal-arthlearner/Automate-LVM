import os
os.system("tput setaf 10")
#print("\t"+40*"-")
print( )
print()
print()
print("\tThis is Task7.1C: Automating LVM using python")
print("\t"+45*"~")
os.system("tput setaf 220")
while True:
    os.system("tput setaf 200")
    print("\n\t"+34*".")
    print("\t\tWhat would you prefer ?")
    print("\t"+34*".")
    os.system("tput setaf 7")

    print()
    os.system("tput setaf 50")
    print("\t1.Create a new LV")
    print("\t2.Increase the size of LV")
    print("\t3.Decrease the size of LV")
    print("\t4.Mount new LV")
    print("\t5.Display list of all mounted disk")
    print("\t6.List all LG(Logical Group)")
    print("\t7.List all LV(Logical Volume)")
    print("\t8.List all Hard Disk")
    print("\t9.Exit")
    print()
    print("\t")
    os.system("tput setaf 11")
    a=int(input("       Enter Your Choice (between 0 to 9) : "))

    if(a==1):
            os.system("fdisk -l")
            num=int(input("Enter the no. hardrive you want to join: "))
            num1=num
            l=[]
            while(num>0):
                c=input("Enter the name of your LV (storage) : ")
                l.append(c)
                num=num-1
            for i in range (0,num1):
                os.system("pvcreate {}".format(l[i]))
            print("Physical Volume Created")
            vgname=input("Enter the name of Volume Group: ")
            syntax=""
            for i in l:
                syntax+=i+" "
            os.system("vgcreate {} {}".format(vgname,syntax))
            print("Volume Group Created")
            os.system("vgdisplay {}".format(vgname))
            print()
            lvmsize=int(input("Enter the size of logical volume you want to create: "))
            lvmname=input("Enter the name of logical volume: ")
            print("Creating the logical volume of size-{} GIB with name- {}".format(lvmsize,lvmname))
            os.system("lvcreate --size {}G --name {} {}".format(lvmsize,lvmname,vgname))
            print("\t\t\tLVM with name- {} Successfully Created".format(lvmsize,lvmname))
            os.system("lvdisplay")
            print()
            input("Press enter for Main Menu: ")
    elif(a==2):

            vgname=input("Enter the name of Volume Group: ")
            lvname=input("Enter the name of logical volume group: ")
            os.system("vgdisplay {}".format(vgname))
            size=int(input("Enter the storage you want more in GB : "))

            os.system("lvextend --size +{}G /dev/{}/{}".format(size,vgname,lvname))
            os.system("resize2fs /dev/{}/{}".format(vgname,lvname))
            os.system("lvdisplay")
            print()
            print("\t\t\tExtended Successfully")
            os.system("df -h")
            input("Press enter to Main Menu: ")

    elif(a==3):

            vgname=input("Enter the name of volume group: ")
            lvname=input("Enter the name of logical volume group: ")
            mdir=input("Enter the mounted drive location: ")
            os.system("lvdisplay")
            size=int(input("Enter the size you actually want to reduce to : "))
            print("unmounting the logical volume")
            os.system("hadoop-daemon.sh stop datanode")
            os.system("umount /dev/{}/{}".format(vgname,lvname))
            os.system("e2fsck -f /dev/{}/{}".format(vgname,lvname))
            os.system("resize2fs /dev/{}/{} {}G".format(vgname,lvname,size))
            os.system("lvreduce -L {}G /dev/{}/{}".format(size,vgname,lvname))
            print("mounting the new shrinked volume to drive: {} ")
            os.system("mount /dev/{}/{} {}".format(vgname,lvname,mdir))
            os.system("lvdisplay")
            print("mounted shrinked volume: ")
            os.system("hadoop-daemon.sh start datanode")
            os.system("df -h")
            print()
            input("Press enter to Main Menu: ")

    elif(a==4):
            dirname=input("Enter the name of mounting directory: ")
            os.system("mkdir /{}".format(dirname))
            vgname=input("Enter the vgname: ")
            lvmname=input("Enter the LVMname: ")
            state=input("New lvm storage then press yes else no :")
            if(state=="yes"):
                os.system("fdisk /dev/{}/{}".format(vgname,lvmname))
                os.system("fdisk -l")
                dire=input("enter the directory: ")
                os.system("mkfs.ext4 {}".format(dire))
            if(state=="no"):
                os.system("mkfs.ext4 /dev/{}/{}".format(vgname,lvmname))
                os.system("mount /dev/{}/{} /{}".format(vgname,lvmname,dirname))
                print("successfully mounted")
                os.system("df -h")
                print()
            else:
                exit()
            input("Press enter to Main Menu: ")

    elif(a==5):
            os.system("df -h")
            input("Press enter to continue")

    elif(a==6):
            os.system("vgdisplay")
            input("Press enter to continue")

    elif(a==7):
            os.system("lvdisplay")
            input("Press enter to continue")

    elif(a==8):
            os.system("fdisk -l")
            input("Press enter to continue")

    elif(a==9):
            exit()
