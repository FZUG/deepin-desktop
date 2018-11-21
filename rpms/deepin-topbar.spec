Name:           deepin-topbar
Version:        0.5.1
Release:        1%{?dist}
Summary:        Topbar for Deepin desktop environment
License:        GPLv3
URL:            https://github.com/justforlxz/deepin-topbar
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
Requires:       hicolor-icon-theme
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/dbus-1/services/*.service

%files devel
%{_includedir}/%{name}/

%changelog
* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 0.5.1-1
- Initial build
