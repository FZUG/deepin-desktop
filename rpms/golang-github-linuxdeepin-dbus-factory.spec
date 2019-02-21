# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/linuxdeepin/go-dbus-factory
%global commit  375d4e7231a2308a7e3c983280321ef2e9f78cc5

%gometa

Name:           %{goname}
Version:        0.2.0
Release:        2%{?dist}
Summary:        GO DBus factory for Deepin Desktop Environment
License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup

%install
%goinstall

%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%doc README.md

%changelog
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2.git375d4e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 mosquito <sensor.wen@gmail.com> - 0.2.0-1.20181215git375d4e7
- Update to 375d4e7

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 0.1.0-1.20181129git19d6db1
- Update to 19d6db1

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 0.0.7.1-1.20181109git0bb7f20
- Update to 0bb7f20

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 0.0.7-1.20180827gite843337
- Update to e843337

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.git6184b97
- Update to 6184b97

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 0-0.1.git67aca0b
- Initial package build
