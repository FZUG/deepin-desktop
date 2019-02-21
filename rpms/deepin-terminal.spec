%global _terminals gnome-terminal mate-terminal xfce4-terminal lxterminal qterminal qterminal-qt5 terminology yakuake fourterm roxterm lilyterm termit xterm mrxvt

Name:           deepin-terminal
Version:        3.2.1
Release:        1%{?dist}
Summary:        Default terminal emulation application for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-terminal
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vala-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(vte-2.91)
# right-click menu style
Requires:       deepin-menu
# run command by create_from_commandline
Requires:       deepin-shortcut-viewer
Requires:       expect
Requires:       xdg-utils
Recommends:     deepin-manual
Recommends:     zssh
Requires:       %{name}-data = %{version}-%{release}

%description
%{summary}.

%package data
Summary:        Data files of Deepin Terminal
BuildArch:      noarch
Requires:       hicolor-icon-theme

%description data
The %{name}-data package provides shared data for Deepin Terminal.

%prep
%setup -q
sed -i '/ssh_login/s|lib|libexec|' lib/utils.vala CMakeLists.txt
sed -i '/stdc++/d' CMakeLists.txt

# remove es_419 locale
rm -rf po/es_419/
sed -i '/es_419/d' deepin-terminal.desktop

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DTEST_BUILD=OFF \
       -DUSE_VENDOR_LIB=OFF \
       -DVERSION=%{version} \
       .
%make_build

%install
%make_install

%find_lang %{name}

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove x-terminal-emulator %{_bindir}/%{name}
fi

%post
if [ $1 -ge 1 ]; then
  %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
    x-terminal-emulator %{_bindir}/%{name} 20
fi

%triggerin -- konsole5 %_terminals
if [ $1 -ge 1 ]; then
  PRI=20
  for i in konsole %{_terminals}; do
    PRI=$((PRI-1))
    test -x %{_bindir}/$i && \
    %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
      x-terminal-emulator %{_bindir}/$i $PRI
  done
fi

%triggerpostun -- konsole5 %_terminals
if [ $2 -eq 0 ]; then
  for i in konsole %{_terminals}; do
    test -x %{_bindir}/$i || \
    %{_sbindir}/alternatives --remove x-terminal-emulator %{_bindir}/$i &>/dev/null ||:
  done
fi

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libexecdir}/%{name}/ssh_login.sh

%files data -f %{name}.lang
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 3.0.12-2
- Append curdir to CMake invokation. (#1668512)

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.0.12-1
- Update to 3.0.12

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 3.0.11.1-1
- Update to 3.0.11.1

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 3.0.10.2-1
- Update to 3.0.10.2

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.0.10-1
- Update to 3.0.10

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec  7 2017 mosquito <sensor.wen@gmail.com> - 2.9.2-1
- Update to 2.9.2

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 2.7.6-1
- Update to 2.7.6

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 2.7.4-1
- Update to 2.7.4

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 2.7.2-1
- Update to 2.7.2

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 2.7-1
- Update to 2.7

* Mon Oct 16 2017 mosquito <sensor.wen@gmail.com> - 2.6.4-1
- Update to 2.6.4
- Unbundle vte

* Thu Sep 21 2017 mosquito <sensor.wen@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Tue Aug 29 2017 mosquito <sensor.wen@gmail.com> - 2.5.5-1
- Update to 2.5.5

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 2.5.3-1
- Update to 2.5.3

* Mon Jul 31 2017 mosquito <sensor.wen@gmail.com> - 2.5.2-1
- Update to 2.5.2

* Fri Jul 21 2017 mosquito <sensor.wen@gmail.com> - 2.5.1-2.git82c4a12
- Split package

* Tue Jul 18 2017 mosquito <sensor.wen@gmail.com> - 2.5.1-1.git82c4a12
- Update to 2.5.1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 2.5.0-1.git439ab57
- Update to 2.5.0

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 2.4.2-1.git76b20cd
- Update to 2.4.2

* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 2.2.2-1.git3ec5488
- Update to 2.2.2

* Sat Feb 11 2017 mosquito <sensor.wen@gmail.com> - 2.1.12-1.git4f7069e
- Update to 2.1.12

* Sun Feb  5 2017 mosquito <sensor.wen@gmail.com> - 2.1.9-3.git1ded038
- Rewrite Req depends

* Sat Jan 28 2017 mosquito <sensor.wen@gmail.com> - 2.1.9-2.git1ded038
- Add trigger for terminal emulator

* Sat Jan 28 2017 mosquito <sensor.wen@gmail.com> - 2.1.9-1.git1ded038
- Update to 2.1.9

* Sun Jan 22 2017 mosquito <sensor.wen@gmail.com> - 2.1.7-2.git32f96be
- Add x-terminal-emulator command for dde-file-manager

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 2.1.7-1.git32f96be
- Update to 2.1.7

* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.6-1
- Updated to version 2.1.6

* Thu Dec 15 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.5-2
- Fixed icon path

* Mon Dec 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.5-1
- Initial package build
