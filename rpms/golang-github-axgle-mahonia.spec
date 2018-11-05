# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/axgle/mahonia
%global commit  3358181d7394e26beccfae0ffde05193ef3be33a

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Character-set conversion library implemented in Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.

Mahonia is a character-set conversion library implemented in Go. All data
is compiled into the executable; it doesn't need any external data files.

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

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104git3358181
- Rewrite rpm spec

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0.1-1
- Initial package build
