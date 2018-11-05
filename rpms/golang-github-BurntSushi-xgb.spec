# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/BurntSushi/xgb
%global commit  27f122750802c950b2c869a5b63dafcf590ced95

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        XGB is the X protocol Go language Binding
License:        BSD
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
%{import_path} prefix.

%prep
%forgeautosetup

%install
%goinstall

%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%doc README
%license LICENSE

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104git27f1227
- Rewrite rpm spec

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git27f1227
- Initial package
