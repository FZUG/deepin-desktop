# https://github.com/alecthomas/kingpin
%global goipath         gopkg.in/alecthomas/kingpin.v2
%global forgeurl        https://github.com/alecthomas/kingpin
Version:                2.2.6

%gometa

Name:           golang-github-alecthomas-kingpin
Release:        1%{?dist}
Summary:        A Go command line and flag parser
# Detected licences
# - Expat License at 'COPYING'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alecthomas/template)
BuildRequires:  golang(github.com/alecthomas/units)
BuildRequires:  golang(github.com/stretchr/testify/assert)

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


%check
%gochecks


%files devel -f devel.file-list
%license COPYING
%doc README.md _examples


%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.6-1
- Release 2.2.6
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3.git1087e65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2.git1087e65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 2.2.5-1
- Release 2.2.5

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.3-1.gite9044be
- Initial package build
