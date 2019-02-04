# Run tests in check section
# disable for bootstrapping
%bcond_with check

# out of memory on armv7hl
%ifarch %{arm}
%global _smp_mflags -j1
%endif

%global goipath  pkg.deepin.io/dde/api
%global forgeurl https://github.com/linuxdeepin/dde-api
%global tag      %{version}

%gometa

Name:           deepin-api
Version:        3.16.0
Release:        1%{?dist}
Summary:        Go-lang bingding for dde-daemon
License:        GPLv3+
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         %{name}_makefile.patch

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  deepin-gettext-tools
BuildRequires:  deepin-gir-generator
BuildRequires:  golang-deepin-dbus-factory-devel
BuildRequires:  golang(pkg.deepin.io/lib)
BuildRequires:  golang(github.com/linuxdeepin/go-x11-client)
BuildRequires:  golang(github.com/linuxdeepin/go-dbus-factory/org.bluez)
BuildRequires:  golang(github.com/BurntSushi/xgb)
BuildRequires:  golang(github.com/BurntSushi/xgbutil)
BuildRequires:  golang(github.com/disintegration/imaging)
BuildRequires:  golang(github.com/cryptix/wav)
BuildRequires:  golang(github.com/fogleman/gg)
BuildRequires:  golang(github.com/nfnt/resize)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)
%{?systemd_requires}
Requires:       deepin-desktop-base
Requires:       rfkill
Requires(pre):  shadow-utils

%description
%{summary}.

%package -n golang-%{name}-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n golang-%{name}-devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup -p1

sed -i 's|/usr/lib|%{_libexecdir}|' misc/*services/*.service \
    misc/systemd/system/deepin-shutdown-sound.service \
    lunar-calendar/main.go \
    theme_thumb/gtk/gtk.go \
    thumbnails/gtk/gtk.go

sed -i 's|PREFIX}${libdir|LIBDIR|; s|libdir|LIBDIR|; s|boot/grub/|boot/grub2/|' \
    Makefile adjust-grub-theme/main.go

%build
%gobuildroot
for cmd in $(make binaries); do
    %gobuild -o _bin/$cmd %{goipath}/$cmd
done
%make_build

%install
rm -rf $(make binaries)
gofiles=$(find $(make libraries) %{?gofindfilter} -print)
%goinstall $gofiles
%make_install SYSTEMD_SERVICE_DIR="%{_unitdir}" LIBDIR="%{_libexecdir}"
# HOME directory for user deepin-sound-player
mkdir -p %{buildroot}%{_sharedstatedir}/deepin-sound-player

%if %{with check}
%check
%gochecks
%endif

%pre
getent group deepin-sound-player >/dev/null || groupadd -r deepin-sound-player
getent passwd deepin-sound-player >/dev/null || \
    useradd -r -g deepin-sound-player -d %{_sharedstatedir}/deepin-sound-player\
    -s /sbin/nologin \
    -c "User of com.deepin.api.SoundThemePlayer.service" deepin-sound-player
exit 0

%post
%systemd_post deepin-shutdown-sound.service

%preun
%systemd_preun deepin-shutdown-sound.service

%postun
%systemd_postun_with_restart deepin-shutdown-sound.service

%files
%doc README.md
%license LICENSE
/boot/grub2/themes/deepin-fallback/
%{_bindir}/dde-open
%{_libexecdir}/%{name}/
%{_unitdir}/*.service
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/actions/*
%{_datadir}/dde-api/data/pkg_depends
%{_datadir}/dde-api/data/grub-themes/
%{_polkit_qt_policydir}/com.deepin.api.locale-helper.policy
%{_polkit_qt_policydir}/com.deepin.api.device.unblock-bluetooth-devices.policy
%{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.api.device.pkla
%attr(-, deepin-sound-player, deepin-sound-player) %{_sharedstatedir}/deepin-sound-player

%files -n golang-%{name}-devel -f devel.file-list

%changelog
* Wed Jan 30 2019 mosquito <sensor.wen@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Jan 29 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.12.0-2
- Create deepin-sound-player user

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 3.1.26-1
- Update to 3.1.26
- build error with gobject-introspection 1.58 by gir-generator
  https://github.com/linuxdeepin/developer-center/issues/604

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.1.20-3
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 3.1.20-1
- Update to 3.1.20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.18.1-2
- Remove obsolete scriptlets

* Thu Dec 21 2017 mosquito <sensor.wen@gmail.com> - 3.1.18.1-1
- Update to 3.1.18.1

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 3.1.17-1
- Update to 3.1.17

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 3.1.15-1
- Update to 3.1.15

* Mon Oct 16 2017 mosquito <sensor.wen@gmail.com> - 3.1.14-2
- Fix out of memory on armv7hl

* Sat Oct 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.14-1
- Update to 3.1.14

* Sat Aug 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.13-1
- Update to 3.1.13

* Tue Aug  8 2017 mosquito <sensor.wen@gmail.com> - 3.1.11-2
- Rename deepin-api-devel to golang-deepin-api-devel

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 3.1.11-1
- Update to 3.1.11

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.10-1.git79125e7
- Update to 3.1.10

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.1.7-1.git4c8e030
- Update to 3.1.7

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.2-1.gitf93dbd7
- Update to 3.1.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.16.1-1.gitcfdb295
- Update to 3.0.16.1

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.16-1
- Update to version 3.0.16

* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.15-1
- Update to version 3.0.15

* Wed Dec 07 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14-2
- Changed compilation procedure

* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14-1
- Initial package build
