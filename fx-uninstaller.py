#!/usr/bin/env python
import os
import getpass

#adding some color to the terminal.
colorred = "\033[01;31m{0}\033[00m"
highlight = "\033[01;47m{0}\033[1;m"
coloryellow = '\033[1;33m{0}\033[1;m'

user = getpass.getuser()

def show_status(stat):
    print '\033[1;42m'+'\033[1;37m'+stat+'\033[1;m'+'\033[1;m'

print "\nWelcome "+user+" to One Click Firefox Un-installer"
print coloryellow.format("------------------------------------------------")

print colorred.format(highlight.format("IMPORTANT: By executing this code you are about to remove Firefox and it's related contents, folders, plugins, user data (Example: bookmarks, saved password, history etc) from your computer. YOU ARE LIABLE FOR THE ACTIONS WILL BE TAKEN BY THIS SCRIPT"))
print "Are you sure you want to remove Firefox from you'r computer and all of it's data?"+coloryellow.format("(yes/no)")

#function which triggers all the commands in order to remove fx and it's related content.
def takeAction():
    #let's take some pretty action ;)
    show_status("Un-installing Firefox from your computer")
    os.system("sudo apt-get purge firefox")
    print "Congratulation: Firefox has been removed."

    show_status("Deleting .mozilla/firefox/ from your home directory")
    os.system("sudo rm -rf '/home/hasan/.mozilla/firefox/'")
    print "Success"

    show_status("Deleting .macromedia/ and .adobe in your home directory, these can contain \"Flash Cookies\" stored by the browser. The same is true, if applicable, for Silverlight (Moonlight) and other plugins, they can allow websites to store data on your computer.")
    os.system("sudo rm -rf '/home/hasan/.macromedia/'")
    os.system("sudo rm -rf '/home/hasan/.adobe'")
    print "Success"

    show_status("Deleting /etc/firefox/, this is where your preferences and user-profiles are stored")
    os.system("sudo rm -rf '/etc/firefox/'")
    print "Success"

    show_status("Deleting /usr/lib/firefox/")
    os.system("sudo rm -rf '/etc/firefox/'")
    print "Success"

    show_status("Delete /usr/lib/firefox-addons/")
    os.system("sudo rm -rf '/usr/lib/firefox-addons/'")
    print "Success"

    print colorred.format(highlight.format("All set :D Firefox has completely removed from your computer... enjoy"))
#end of takeAction() function

#listening from you.
command = raw_input()

#understanding you.
if command == "yes":
    print "Great, you want to remove Firefox from your computer, let me do the rest for you :)"
    takeAction()
elif command == "no":
    print "All right, you dont want to remove Firefox from your computer."
else:
    print "Hello, please type \"yes\" if you want to un-install firefox from your computer, write \"no\" if you want to keep firefox in your computer."

print "\nFind more here> http://creativesdiary.com/article/one-click-firefox-uninstaller-linux\n\n"
