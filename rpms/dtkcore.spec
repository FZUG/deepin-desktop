Name:           dtkcore
Version:        2.0.9.5
Release:        1%{?dist}
Summary:        Deepin tool kit core modules
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         fix-symbol.patch
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)

%description
Deepin tool kit core modules.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
%patch0 -p1 -b .fix_symbol
sed -i 's|qmake|qmake-qt5|' src/dtk_module.prf
sed -i 's|/lib|/libexec|' tools/settings/settings.pro
sed -i 's|lrelease|lrelease-qt5|' tools/script/dtk-translate.py src/dtk_translation.prf

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir} BIN_INSTALL_DIR=%{_libexecdir}/dtk2 TOOL_INSTALL_DIR=%{_libexecdir}/dtk2
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_libdir}/lib*.so.*
%{_libexecdir}/dtk2/dtk-settings
%{_libexecdir}/dtk2/dtk-license.py*
%{_libexecdir}/dtk2/dtk-translate.py*
%{_libexecdir}/dtk2/deepin-os-release

%files devel
%doc doc/Specification.md
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/Dtk/DtkConfig.cmake
%{_libdir}/cmake/DtkCore/DtkCoreConfig.cmake
%{_libdir}/cmake/DtkCMake/DtkCMakeConfig.cmake
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.5-1
- Update to 2.0.9.5

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 2.0.9-1
- Update to 2.0.9

* Sat Mar 24 2018 mosquito <sensor.wen@gmail.com> - 2.0.7.1-1
- Update to 2.0.7.1

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 28 2017 mosquito <sensor.wen@gmail.com> - 2.0.5.3-1
- Update to 2.0.5.3

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 2.0.5.2-1
- Update to 2.0.5.2

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 29 2017 mosquito <sensor.wen@gmail.com> - 0.3.3-1
- Initial build
