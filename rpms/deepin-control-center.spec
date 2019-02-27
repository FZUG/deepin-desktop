%global repo dde-control-center

Name:           deepin-control-center
Version:        4.9.4
Release:        1%{?dist}
Summary:        New control center for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-control-center
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  deepin-dock-devel
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dframeworkdbus) >= 2.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(geoip)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  qt5-linguist
Requires:       deepin-account-faces
Requires:       deepin-api
Requires:       deepin-daemon
Requires:       deepin-qt5integration
Requires:       deepin-network-utils
Requires:       GeoIP-GeoLite-data
Requires:       GeoIP-GeoLite-data-extra
Requires:       gtk-murrine-engine
Requires:       proxychains-ng
Requires:       redshift
Requires:       startdde

%description
New control center for Linux Deepin.

%prep
%setup -q -n %{repo}-%{version}
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i '/%{repo}/s|\.\./lib|%{_libdir}|' src/frame/pluginscontroller.cpp

%build
%cmake . -DDCC_DISABLE_GRUB=YES \
         -DDISABLE_SYS_UPDATE=YES
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
# place holder plugins dir
mkdir -p %{buildroot}%{_libdir}/%{repo}/plugins
# https://github.com/linuxdeepin/dde-control-center/issues/115
# And we disabled SYS_UPDATE, so reboot-reminder-dialog is useless.
rm %{buildroot}%{_bindir}/reboot-reminder-dialog

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop ||:

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE
%{_bindir}/%{repo}
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{repo}/
%{_libdir}/%{repo}/

%changelog
* Wed Feb 27 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.9.4-1
- Update to 4.9.4

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 4.9.2.1-1
- Update to 4.9.2.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 4.8.6-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 4.8.6-1
- Update to 4.8.6

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 4.8.2-1
- Update to 4.8.2

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 4.7.7-1
- Update to 4.7.7

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 4.7.6.1-1
- Update to 4.7.6.1

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 4.7.4-1
- Update to 4.7.4

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 4.6.4-1
- Update to 4.6.4

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 4.6.3-1
- Update to 4.6.3

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 4.6.2-1
- Update to 4.6.2

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 4.6.1-1
- Update to 4.6.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 mosquito <sensor.wen@gmail.com> - 4.3.7-3
- Exclude ppc64le, ppc64 and aarch64

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 4.3.7-1
- Update to 4.3.7

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Thu Sep 21 2017 mosquito <sensor.wen@gmail.com> - 4.2.5.10-1
- Update to 4.2.5.10

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 4.2.5.4-1
- Update to 4.2.5.4

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 4.2.5-1
- Update to 4.2.5

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 4.2.4-1.git21d68b6
- Update to 4.2.4

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.2.3-1.git2f420f2
- Update to 4.2.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.1.2-1.git4d3827b
- Update to 4.1.2

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 4.0.7-1.git10c3be2
- Update to 4.0.7

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 3.0.24-1.git481255b
- Downgrade to 3.0.24 for end user

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 4.0.2-2.git8b1a736
- Fix can not start

* Thu Jan 19 2017 mosquito <sensor.wen@gmail.com> - 4.0.2-1.git8b1a736
- Update to 4.0.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.1-1.gitd1c1c9a
- Update to 4.0.1

* Tue Dec 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Bump to newer release because of copr signature

* Fri Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to 3.0.24

* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.21-1
- Initial package build
