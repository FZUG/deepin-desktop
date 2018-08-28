%global repo qtdbusextended

Name:           libdbusextended-qt5
Summary:        Extended DBus for Qt
Version:        0.0.3
Release:        1%{?dist}
License:        LGPLv2.1
URL:            https://github.com/nemomobile/qtdbusextended
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)

%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_libdir}/lib*.so.1*

%files devel
%{_qt5_includedir}/DBusExtended/DBusExtended
%{_qt5_includedir}/DBusExtended/DBusExtendedAbstractInterface
%{_qt5_includedir}/DBusExtended/dbusextended.h
%{_qt5_includedir}/DBusExtended/dbusextendedabstractinterface.h
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Tue Aug 28 2018 mosquito <sensor.wen@gmail.com> - 0.0.3-1
- Initial package build
