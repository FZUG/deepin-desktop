# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/fogleman/gg
%global commit  0e0ff3ade7039063fe954cc1b45fad6cd4ac80db

%gometa

Name:           %{goname}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Go Graphics - 2D rendering in Go with a simple API
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
%license LICENSE.md

%changelog
* Mon Nov  5 2018 mosquito <sensor.wen@gmail.com> - 1.1.0-1.20181106gite843337
- Initial package build
