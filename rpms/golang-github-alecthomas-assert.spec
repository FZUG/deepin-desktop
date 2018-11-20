# https://github.com/alecthomas/assert
%global goipath         github.com/alecthomas/assert
%global commit          405dbfeb8e38effee6e723317226e93fff912d06

%global common_description %{expand:
This is a fork of stretchr's assertion library that does two things:

 - It makes spotting differences in equality much easier. It uses repr and 
   diffmatchpatch to display structural differences in colour.
 - Aborts tests on first assertion failure (the same behaviour as 
   stretchr/testify/require).}

%gometa

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Go assertion library
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alecthomas/colour)
BuildRequires:  golang(github.com/alecthomas/repr)
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires:  golang(github.com/stretchr/testify/require)

%description
%{common_description}


%package devel
Summary:        %{summary}
BuildArch:      noarch

%description devel
%{common_description}

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
%doc README.md


%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181111git405dbfe
- Bump to commit 405dbfeb8e38effee6e723317226e93fff912d06
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git561411b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git561411b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git561411b
- Initial package build

