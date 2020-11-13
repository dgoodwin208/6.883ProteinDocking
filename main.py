# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    python train.py abdg_demo --pkl_dir=./data/firstpkltry/ --pretrained ./pretrained/pretrained.pth.tar --epochs 0 --train 0 --val 0 --test 1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
