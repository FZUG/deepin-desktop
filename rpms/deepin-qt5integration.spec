%global repo qt5integration
%global plug qt5dxcb-plugin
%global plug_url https://github.com/linuxdeepin/qt5dxcb-plugin
%global plug_ver 1.1.14

Name:           deepin-qt5integration
Version:        0.3.6
Release:        2%{?dist}
Summary:        Qt platform theme integration plugins for DDE
# The entire source code is GPLv3+ except styles/ which is BSD,
# dstyleplugin/ which is GPLv3, dstyleplugin/dstyleanimation* which is LGPL
License:        GPLv3 and BSD and LGPLv2+
URL:            https://github.com/linuxdeepin/qt5integration
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
Source1:        %{plug_url}/archive/%{plug_ver}/%{plug}-%{plug_ver}.tar.gz

BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xdg) >= 3.0.0
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt5-qtbase-common
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep
%setup -q -a1 -n %{repo}-%{version}
pushd %{plug}-%{plug_ver}
rm -r platformplugin/libqt5xcbqpa-dev
sed -i 's|error.*|INCLUDEPATH += %{_qt5_includedir}/QtXcb|' platformplugin/linux.pri

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

pushd %{plug}-%{plug_ver}
%qmake_qt5 PREFIX=%{_prefix} QMAKE_LFLAGS+="-fuse-ld=gold"
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

pushd %{plug}-%{plug_ver}
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_qt5_plugindir}/platforms/libdxcb.so
%{_qt5_plugindir}/platformthemes/libqdeepin.so
%{_qt5_plugindir}/styles/libdstyleplugin.so
%{_qt5_plugindir}/iconengines/libdsvgicon.so
%{_qt5_plugindir}/imageformats/libdsvg.so

%changelog
* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 0.3.6-2
- Update qt5dxcb to 1.1.14

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 0.3.6-1
- Update to 0.3.6
- Use of the gold linker by QMAKE_LFLAGS+="-fuse-ld=gold"
  https://bugreports.qt.io/browse/QTBUG-65071

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 0.3.4-2
- rebuild (qt5)

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 0.3.4-1
- Update to 0.3.4

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 0.3.1-1
- Update to 0.3.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8.3-6
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8.3-5
- rebuild (qt5)

* Sun Feb 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8.3-4
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8.3-2
- rebuild (qt5)

* Sat Dec  9 2017 mosquito <sensor.wen@gmail.com> - 0.2.8.3-1
- Update to 0.2.8.3

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2.3-3
- rebuild (qt5)

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 0.2.8.1-1
- Update to 0.2.8.1

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 0.2.7-1
- Update to 0.2.7

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 0.2.4-1
- Update to 0.2.4
- Included qt5xcbqpa private header files in the project

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2.3-2
- BR: qt5-qtbase-private-devel

* Tue Aug 22 2017 mosquito <sensor.wen@gmail.com> - 0.2.3-1
- Update to 0.2.3

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 0.2.2-1
- Update to 0.2.2

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1.git2cd7432
- Update to 0.2.1

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 0.1.8-1.gitb03be20
- Update to 0.1.8

* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 0.1.2-1.gitecde076
- Update to 0.1.2

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 0.1.1-1.gitaa563fd
- Update to 0.1.1

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 0.0.6-1.git40401af
- Update to 0.0.6

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.0.5-1.gitc0dc3cf
- Initial build
