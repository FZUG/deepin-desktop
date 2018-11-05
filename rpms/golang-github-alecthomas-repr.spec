# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/alecthomas/repr
%global commit  d37bc2a10ba1a7951e19dd5dc10f7d59b142d8d7

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Python's repr() for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  golang(github.com/stretchr/testify/assert)

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
%license COPYING

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104gitd37bc2a
- Update to d37bc2a

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitd44565c
- Initial package build
