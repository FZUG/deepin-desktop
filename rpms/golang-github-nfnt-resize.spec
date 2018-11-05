# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/nfnt/resize
%global commit  83c6a9932646f83e3267f353373d47347b6036b2

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Pure golang image resize
License:        ISC
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
%license LICENSE

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104git83c6a99
- Update to 83c6a99

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git891127d
- Initial package build
