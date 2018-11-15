Name:           deepin-voice-recorder
Version:        1.3.8
Release:        1%{?dist}
Summary:        Deepin Voice Recorder
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-voice-recorder
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  qt5-linguist
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Requires:       deepin-manual-directory

%description
%{summary}.

%prep
%setup -q
sed -i 's|=lupdate|=lupdate-qt5|;s|=lrelease|=lrelease-qt5|' %{name}.pro
find manual -executable -name "*.svg" -exec chmod 0644 "{}" \;

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -pDm644 %{S:1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/dman/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.svg

%changelog
* Sun Oct 28 2018 Zamir SUN <sztsian@gmail.com> - 1.3.8-1
- Update to 1.3.8

* Fri Jul 20 2018 mosquito <sensor.wen@gmail.com> - 1.3.7-1
- Update to 1.3.7

* Tue Mar 20 2018 mosquito <sensor.wen@gmail.com> - 1.3.6.1-1
- Update to 1.3.6.1

* Sun Jan 21 2018 Zamir SUN <sztsian@gmail.com> - 1.3.6-3
- Add appdata file

* Fri Jan 12 2018 Zamir SUN <sztsian@gmail.com> - 1.3.6-2
- Prepare for rpmfusion

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 1.3.6-1
- Update to 1.3.6

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 1.3.5-1
- Update to 1.3.5

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 1.3.1-1.git6cf1cb9
- Update to 1.3.1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.3-1.git6c05bf1
- Update to 1.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.2-1.git2a95a46
- Initial build
