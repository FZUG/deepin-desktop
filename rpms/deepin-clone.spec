Name:           deepin-clone
Version:        1.1.0
Release:        1%{?dist}
Summary:        Disk and partition backup/restore tool
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-clone
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       hicolor-icon-theme
Requires:       partclone
# Check app/src/fixboot/bootdoctor.cpp
# RHBZ#1687369
ExclusiveArch:  x86_64 %{ix86} aarch64

%description
%{summary}.

%prep
%setup -q
sed -i 's|/usr/sbin|/usr/bin|' app/{%{name}-app.pro,%{name}-ionice,%{name}-pkexec,com.deepin.pkexec.%{name}.policy.tmp}

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/%{name}.xml
%{_polkit_qt_policydir}/com.deepin.pkexec.%{name}.policy

%changelog
* Mon Mar 11 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.1.0-1
- Add ExclusiveArch
- Requires partclone

* Tue Mar  5 2019 mosquito <sensor.wen@gmail.com> - 1.1.0-1
- Initial build

* Mon Nov 26 2018 mosquito <sensor.wen@gmail.com> - 0.1.2-1
- Initial build
