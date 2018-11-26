# Deepin packages for Fedora

These files are based on [cz-guardian/fedora-deepin](https://github.com/cz-guardian/fedora-deepin/) and [Arch packages](https://www.archlinux.org/packages/?q=deepin). You can visit the [Deepin Copr](https://copr.fedorainfracloud.org/coprs/mosquito/deepin/) to install them. Thanks for all of the community developers and packagers.


## Installation instructions
    sudo dnf install http://download1.rpmfusion.org/free/fedora/releases/$(rpm -E %fedora)/Everything/$(uname -i)/os/Packages/r/rpmfusion-free-release-$(rpm -E %fedora)-1.noarch.rpm
    sudo dnf copr enable mosquito/deepin
    sudo dnf update
    sudo dnf install deepin-desktop (deepin core)
    sudo dnf install deepin-calendar deepin-calculator deepin-draw deepin-editor deepin-image-viewer deepin-picker deepin-screenshot deepin-system-monitor deepin-terminal (deepin applications)
    sudo dnf install deepin-movie deepin-music deepin-screen-recorder deepin-voice-recorder (need rpmfusion repository)
    sudo systemctl disable gdm.service && sudo systemctl enable lightdm.service (optional, gdm also available)
    sudo sed -i "/SELINUX=/s|enforcing|disabled|" /etc/selinux/config

After this is done, simply reboot into your new nice environment.


## fedora-deepin repository content

This repository contains the following .specs for integrating the deepin desktop environment into Fedora. You can simply compile them in order.

* ***Golang Packages***
* |-golang-github-alecthomas-assert
* |-golang-github-alecthomas-colour
* |-golang-github-alecthomas-kingpin
* |-golang-github-alecthomas-repr
* |-golang-github-alecthomas-template
* |-golang-github-alecthomas-units
* |-golang-github-axgle-mahonia
* |-golang-github-BurntSushi-freetype-go
* |-golang-github-BurntSushi-graphics-go
* |-golang-github-BurntSushi-xgb
* |-golang-github-BurntSushi-xgbutil
* |-golang-github-cheekybits-is
* |-golang-github-cryptix-wav
* |-golang-github-disintegration-imaging
* |-golang-github-fogleman-gg
* |-golang-github-howeyc-fsnotify
* |-golang-github-mattn-go-isatty
* |-golang-github-msteinert-pam
* |-golang-github-nfnt-resize
* |-golang-github-sergi-go-diff
* |-golang-github-linuxdeepin-go-dbus-factory
* |-golang-github-linuxdeepin-go-x11-client
* |-golang-deepin-gir-generator
* |-golang-deepin-go-lib
* |-deepin-dbus-generator
* |-golang-deepin-dbus-factory
* |-golang-deepin-api
* ***Window Manager***
* |-deepin-cogl
* |-deepin-metacity
* |-deepin-mutter
* |-deepin-wm
* ***DDE Base***
* |-deepin-account-faces
* |-deepin-desktop-base
* |-deepin-desktop-schemas
* |-deepin-gettext-tools
* |-deepin-artwork-themes
* |-deepin-gtk-theme
* |-deepin-grub2-themes
* |-deepin-icon-theme
* |-deepin-sound-theme
* |-deepin-wallpapers
* |-deepin-polkit-agent
* |-deepin-qml-widgets
* |-deepin-qt-dbus-factory
* |-deepin-qt5integration
* |-deepin-menu
* |-deepin-network-utils
* |-deepin-shortcut-viewer
* |-plymouth-theme-deepin
* |-gsettings-qt
* |-libdbusextended-qt5
* |-libmpris-qt5
* |-imwheel
* |-zssh
* ***DDE API and Service***
* |-dtkcore
* |-dtkwidget
* |-dtkwm
* |-deepin-api
* |-startdde
* |-deepin-session-ui
* |-deepin-daemon
* |-deepin-dock
* |-deepin-control-center
* |-deepin-file-manager
* |-deepin-launcher
* ***Applications***
* |-deepin-calendar
* |-deepin-calculator
* |-deepin-clone
* |-deepin-draw
* |-deepin-editor
* |-deepin-image-viewer
* |-deepin-picker
* |-deepin-screenshot
* |-deepin-system-monitor
* |-deepin-topbar
* |-deepin-terminal
* |-deepin-manual
* |-deepin-movie
* |-deepin-music
* |-deepin-screen-recorder
* |-deepin-voice-recorder
* ***Obsoletes***
* |-deepin-anything
* |-deepin-boot-maker
* |-deepin-desktop
* |-deepin-file-manager-backend
* |-deepin-help
* |-deepin-nautilus-properties
* |-deepin-notifications
* |-deepin-tool-kit
* |-deepin-wm-switcher
* |-dtksettings
* |-perl-xml-libxml-prettyprint
* |-deepin-gsettings
* |-deepin-game
* |-deepin-social-sharing
* |-python2-deepin-ui
* |-python2-deepin-util
* |-python2-deepin-storm
* |-python2-javascriptcore
* |-python2-ass
* |-python3-dae
* |-python2-pysrt
* |-python2-xpybutil
* |-treefrog-framework


## Resources
* [Deepin Github](https://github.com/linuxdeepin/), [Official site](https://www.deepin.org/en/), [Deepin OS Design](https://my.oschina.net/ManateeLazyCat/blog/831104)
* [fedora package monitor](https://apps.fedoraproject.org/koschei/groups/mosquito/deepin-sig)
* [fedora-deepin repository list](https://copr.fedorainfracloud.org/coprs/mosquito/deepin/packages/)
* [fedora-deepin (jstepanek)](https://github.com/cz-guardian/fedora-deepin/): thanks @cz-guardian
* [arch-deepin](https://github.com/fasheng/arch-deepin/): [Deepin Desktop Environment on Arch](https://bbs.archlinux.org/viewtopic.php?id=181861)
* [manjaro-deepin](https://github.com/manjaro/packages-community/): [issue 98](https://github.com/fasheng/arch-deepin/issues/98)
* [debian-deepin](https://github.com/debiancn/repo/issues/31)
* [gentoo-deepin](https://github.com/zhtengw/deepin-overlay/)
