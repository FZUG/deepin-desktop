# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/sergi/go-diff
%global commit  da645544ed44df016359bd4c0e3dc60ee3a0da43

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Diff, match and patch text in Go
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
%license LICENSE

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.3.20181104gitda64554
- Update to da64554

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.2.gitfeef008
- Add golang(%%{import_path}) provide

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitfeef008
- Initial package
