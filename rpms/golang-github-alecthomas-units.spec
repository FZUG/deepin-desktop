# https://github.com/alecthomas/units
%global goipath         github.com/alecthomas/units
%global commit          2efee857e7cfd4f3d0138cc3cbb1b4966962b93a

%gometa

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Helpful unit multipliers and functions for Go
# Detected licences
# - Expat License at 'COPYING'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/stretchr/testify/assert)

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
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git2efee85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181111git2efee85
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git2efee85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git2efee85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git2efee85
- Initial package

