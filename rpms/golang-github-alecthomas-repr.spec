# https://github.com/alecthomas/repr
%global goipath         github.com/alecthomas/repr
%global commit          d37bc2a10ba1a7951e19dd5dc10f7d59b142d8d7

%gometa

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Python's repr() for Go
# Detected licences
# - Expat License at 'COPYING'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/stretchr/testify/assert)

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license COPYING
%doc README.md


%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitd37bc2a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181111gitd37bc2a
- Bump to commit d37bc2a10ba1a7951e19dd5dc10f7d59b142d8d7
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitd44565c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitd44565c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitd44565c
- Initial package build

