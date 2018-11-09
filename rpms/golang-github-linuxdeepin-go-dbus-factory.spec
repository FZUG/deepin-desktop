# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/linuxdeepin/go-dbus-factory
%global commit  0bb7f2053da193e4f200841f67e66be695512b3a

%gometa

Name:           %{goname}
Version:        0.0.7.1
Release:        1%{?dist}
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
* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 0.0.7.1-1.20181109git0bb7f20
- Update to 0bb7f20

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 0.0.7-1.20180827gite843337
- Update to e843337

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.git6184b97
- Update to 6184b97

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 0-0.1.git67aca0b
- Initial package build
