# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/BurntSushi/freetype-go
%global commit  b763ddbfe298bf71c999a2833470da508f3a0677

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        A fork of freetype-go with bounding box calculations
License:        GPLv2+ or FTL
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
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104gitb763ddb
- Rewrite rpm spec

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0.1-1
- Initial package build
