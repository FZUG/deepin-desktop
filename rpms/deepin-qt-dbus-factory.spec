%global project dde-qt-dbus-factory
%global repo %{project}

Name:           deepin-qt-dbus-factory
Version:        0.2.1
Release:        1%{?dist}
Summary:        A repository stores auto-generated Qt5 dbus code
License:        GPLv3+ and LGPLv2+
URL:            https://github.com/linuxdeepin/dde-qt-dbus-factory
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)

%description
A repository stores auto-generated Qt5 dbus code.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}

%build
%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README
%license LICENSE
%{_libdir}/libdframeworkdbus.so.*

%files devel
# LGPLv2+
%{_includedir}/libdframeworkdbus-1.0/dbusextended.h
%{_includedir}/libdframeworkdbus-1.0/dbusextendedabstractinterface.h
%{_includedir}/libdframeworkdbus-1.0/dbusextendedpendingcallwatcher_p.h
# GPLv3+
%{_includedir}/libdframeworkdbus-1.0/DBusExtended
%{_includedir}/libdframeworkdbus-1.0/DBusExtendedAbstractInterface
%{_includedir}/libdframeworkdbus-1.0/com_deepin*.h
%{_includedir}/libdframeworkdbus-1.0/org_freedesktop*.h
%{_includedir}/libdframeworkdbus-1.0/types/*.h
%{_libdir}/pkgconfig/dframeworkdbus.pc
%{_libdir}/libdframeworkdbus.so

%changelog
* Sat Aug  5 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1
- Fix license

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1.gitbecf852
- Update to 0.2.1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 0.2.0-1.git98d9901
- Update to 0.2.0

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 0.1.0-1.git9adc304
- Update to 0.1.0

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 0.0.4-1.gitefa4f7f
- Update to 0.0.4

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.0.3-1.gitffda1af
- Initial build
