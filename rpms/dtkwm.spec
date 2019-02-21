Name:           dtkwm
Version:        2.0.9
Release:        3%{?dist}
Summary:        Deepin graphical user interface library
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtkwm
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-static
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)

%description
DtkWm is used to handle double screen for deepin desktop development.
This package contains the shared libraries.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE
%{_libdir}/libdtkwm.so.2*

%files devel
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtkwm.pri
%dir %{_libdir}/cmake/DtkWm/
%{_libdir}/cmake/DtkWm/DtkWmConfig.cmake
%{_libdir}/pkgconfig/dtkwm.pc
%{_libdir}/libdtkwm.so

%changelog
* Wed Feb 20 2019 mosquito <sensor.wen@gmail.com> - 2.0.9-3
- use %%_qt5_bindir
- add gcc-c++ BReq

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 2.0.9-1
- Update to 2.0.9

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Sat Aug 19 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-1
- Initial package build
