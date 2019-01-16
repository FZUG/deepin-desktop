# fedora-live-deepin.ks
#
# Description:
# – Fedora Live media kickstart with the Deepin desktop environment
#
# Maintainer(s):
# – Zamir SUN <zsun@fedoraproject.org>
#

%include fedora-live-base.ks
%include fedora-live-minimization.ks
%include fedora-deepin-common.ks

%post
# add initscript
cat >> /etc/rc.d/init.d/livesys << EOF

# set up autologin for user liveuser
if [ -f /etc/sddm.conf ]; then
sed -i 's/^#User=.*/User=liveuser/' /etc/sddm.conf
sed -i 's/^#Session=.*/Session=deepin.desktop/' /etc/sddm.conf
else
cat > /etc/sddm.conf << SDDM_EOF
[Autologin]
User=liveuser
Session=deepin.desktop
SDDM_EOF
fi

# show liveinst.desktop on desktop and in menu
sed -i 's/NoDisplay=true/NoDisplay=false/' /usr/share/applications/liveinst.desktop
mkdir /home/liveuser/Desktop
cp -a /usr/share/applications/liveinst.desktop /home/liveuser/Desktop/

# no updater applet in live environment
rm -f /etc/xdg/autostart/org.mageia.dnfdragora-updater.desktop

# make sure to set the right permissions and selinux contexts
chown -R liveuser:liveuser /home/liveuser/
restorecon -R /home/liveuser/
# Temporary set selinux to permissive to workaround the dbus-broker bug
sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/sysconfig/selinux
EOF

%end

