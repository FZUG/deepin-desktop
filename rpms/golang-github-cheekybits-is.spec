# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/cheekybits/is
%global commit  68e9c0620927fb5427fda3708222d0edee89eae9

%gometa

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        A mini testing helper for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       golang(%{import_path}) = %{version}-%{release}

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
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git68e9c06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 0-0.3.20181109git68e9c06
- Rewrite rpm spec

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20150226git68e9c06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 mosquito <sensor.wen@gmail.com> - 0-0.1.20150226git68e9c06
- Initial package build
