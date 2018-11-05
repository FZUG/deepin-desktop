# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/alecthomas/assert
%global commit  405dbfeb8e38effee6e723317226e93fff912d06

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Units - Helpful unit multipliers and functions for Go
License:        MIT
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
%doc README.md
%license LICENCE.txt

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104git405dbfe
- Update to 405dbfe

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git561411b
- Initial package build
