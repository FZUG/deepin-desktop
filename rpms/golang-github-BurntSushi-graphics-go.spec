# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/BurntSushi/graphics-go
%global commit  b43f31a4a96688fba0b612e25e22648b9267e498

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Graphics library for the Go programming language
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
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.3.20181104gitb43f31a
- Rewrite rpm spec

* Fri Aug 18 2017 mosquito <sensor.wen@gmail.com> - 0-0.2.gitb43f31a
- ignore test error for ppc64le

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitb43f31a
- Initial package build
