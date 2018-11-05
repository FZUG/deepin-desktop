# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/alecthomas/colour
%global commit  60882d9e27213e8552dcff6328914fe4c2b44bc9

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Quake-style colour formatting for Unix terminals
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
%license COPYING

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104git60882d9
- Rewrite rpm spec

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git60882d9
- Initial package build
