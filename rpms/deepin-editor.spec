Name:           deepin-editor
Version:        1.2.6.3
Release:        1%{?dist}
Summary:        Simple editor for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  freeimage-devel
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
Requires:       deepin-notifications
Requires:       deepin-qt5integration

%description
%{summary}.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release .
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/dedit
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Feb 19 2019 mosquito <sensor.wen@gmail.com> - 1.2.6.3-1
- Update to 1.2.6.3

* Sat Jan 12 2019 mosquito <sensor.wen@gmail.com> - 1.2.6.2-1
- Update to 1.2.6.2

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Jul 23 2018 mosquito <sensor.wen@gmail.com> - 0.0.5-1
- Initial package build
