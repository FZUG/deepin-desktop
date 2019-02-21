%global repo dde-polkit-agent

Name:           deepin-polkit-agent
Version:        0.2.4
Release:        1%{?dist}
Summary:        Deepin Polkit Agent
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-polkit-agent
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  qt5-linguist

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|lib|libexec|' dde-polkit-agent.pro polkit-dde-authentication-agent-1.desktop \
    pluginmanager.cpp

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%dir %{_libexecdir}/polkit-1-dde
%{_libexecdir}/polkit-1-dde/%{repo}
%{_datadir}/%{repo}/

%files devel
%{_includedir}/dpa/agent-extension-proxy.h
%{_includedir}/dpa/agent-extension.h

%changelog
* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 0.2.4-1
- Update to 0.2.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 mosquito <sensor.wen@gmail.com> - 0.2.1-2
- Deprecate dcombobox.h header

* Wed Jul 18 2018 mosquito <sensor.wen@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 0.1.1-1
- Update to 0.1.1

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 0.1.0-1
- Update to 0.1.0

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 0.0.10-1.git680c12f
- Update to 0.0.10

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 0.0.8-1.git7e0fcbc
- Initial package build
