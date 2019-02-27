%global project ~system-settings-touch
%global _revision 85

# for fedora 24
# %%global _qt5_qmldir %%{_qt5_archdatadir}/qml
%global __provides_exclude ^libGSettingsQmlPlugin\\.so.*$

Name:           gsettings-qt
Version:        0
Release:        0.18.20180723bzr%{_revision}%{?dist}
Summary:        Qt/QML bindings for GSettings
License:        LGPLv3
URL:            https://launchpad.net/gsettings-qt
Source0:        http://bazaar.launchpad.net/%{project}/%{name}/trunk/tarball/%{_revision}#/%{name}-%{_revision}.tar.gz
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  glib2-devel
BuildRequires:  gcc-c++

%description
Qt/QML bindings for GSettings.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{project}/%{name}/trunk

%build
%qmake_qt5 PREFIX=%{_prefix}
# sed -i "/\t\tsub-tests-tests-pro/d" Makefile
# sed -i "/\t\tsub-tests-cpptest-pro/d" Makefile
# Parallel build not supported. It causes error when linking
make

%install
%make_install INSTALL_ROOT=%{buildroot}

# remove test
rm -rf %{buildroot}%{_qt5_prefix}/tests -rf
find %{buildroot} -iname test* -exec rm -f {} \;
find %{buildroot} -iname cpptest* -exec rm -f {} \;

%ldconfig_scriptlets

%files
%{_libdir}/lib%{name}.so.*
%license COPYING
%dir %{_qt5_qmldir}/GSettings.1.0/
%{_qt5_qmldir}/GSettings.1.0/libGSettingsQmlPlugin.so
%{_qt5_qmldir}/GSettings.1.0/plugins.qmltypes
%{_qt5_qmldir}/GSettings.1.0/qmldir

%files devel
%license COPYING
%dir %{_qt5_headerdir}/QGSettings/
%{_qt5_headerdir}/QGSettings/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20180723bzr85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 0-0.17.20180723bzr
- better fix for removal of test-dir

* Thu Aug 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 0-0.16.20180723bzr
- drop BR: qt5-qtbase-private-devel
- use %%ldconfig_scriptlets

* Mon Jul 23 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.15.20180723.bzr85
- Upload new source package

* Mon Jul 23 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.14.20180723.bzr85
- Update to upstream bzr r85

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20170715bzr83
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 0-0.12.20170715bzr
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0-0.11.20170715bzr
- rebuild (qt5)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 0-0.10.20170715bzr83
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20170715bzr83
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 0-0.8.20170715bzr83
- rebuild (qt5)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 0-0.7.20170715bzr83
- rebuild (qt5)

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 0-0.6.20170715bzr
- BR: qt5-qtbase-private-devel

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20170715bzr83
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.4.20170715bzr83
- Add s390x and ppc64 back as it can be built on rawhide today

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170715bzr83

* Sat Jul 15 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.2.20170715bzr83
- Update to bzr r83 and change the versioning style

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.20160329-3
- Update to 0.1.20160329

* Tue Jan 03 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0-0.1.20160329-2
- Major rewrite of SPEC file

* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0-0.1.20160329-1
- Initial package build
