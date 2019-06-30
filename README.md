# Deepin packages for Fedora



These files are based on [cz-guardian/fedora-deepin](https://github.com/cz-guardian/fedora-deepin/) and [Arch packages](https://www.archlinux.org/packages/?q=deepin). As of Fedora 30, Deepin Desktop can be installed directly from Fedora repo.


## Installation instructions
    sudo dnf install @deepin-desktop
    sudo dnf install xorg-x11-server-Xorg # (if you don't have other desktop installed before)
    sudo dnf install http://download1.rpmfusion.org/free/fedora/releases/$(rpm -E %fedora)/Everything/$(uname -i)/os/Packages/r/rpmfusion-free-release-$(rpm -E %fedora)-1.noarch.rpm # Optional, only needed for the multi-media packages.
    sudo dnf install deepin-movie deepin-music deepin-screen-recorder deepin-voice-recorder # (need rpmfusion repository)
    sudo systemctl disable gdm.service && sudo systemctl enable lightdm.service # (optional, gdm also works with Deepin Desktop)

After this is done, simply reboot into your new nice environment.


## Resources
* [Deepin Github](https://github.com/linuxdeepin/), [Official site](https://www.deepin.org/en/), [Deepin OS Design](https://my.oschina.net/ManateeLazyCat/blog/831104)
* [Fedora package monitor](https://apps.fedoraproject.org/koschei/groups/mosquito/deepin-sig)
* [Fedora deepin-desktop staging copr](https://copr.fedorainfracloud.org/coprs/mosquito/deepin/packages/)
* [fedora-deepin (jstepanek)](https://github.com/cz-guardian/fedora-deepin/): thanks @cz-guardian
* [arch-deepin](https://github.com/fasheng/arch-deepin/): [Deepin Desktop Environment on Arch](https://bbs.archlinux.org/viewtopic.php?id=181861)
* [manjaro-deepin](https://github.com/manjaro/packages-community/): [issue 98](https://github.com/fasheng/arch-deepin/issues/98)
* [debian-deepin](https://github.com/debiancn/repo/issues/31)
* [gentoo-deepin](https://github.com/zhtengw/deepin-overlay/)
