# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/alecthomas/units
%global commit  2efee857e7cfd4f3d0138cc3cbb1b4966962b93a

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
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104git2efee85
- Rewrite rpm spec

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git2efee85
- Initial package
