# https://github.com/alecthomas/colour
%global goipath         github.com/alecthomas/colour
%global commit          60882d9e27213e8552dcff6328914fe4c2b44bc9

%gometa

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Quake-style colour formatting for Unix terminals
# Detected licences
# - Expat License at 'COPYING'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/mattn/go-isatty)

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
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git60882d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181111git60882d9
- Bump to commit 60882d9e27213e8552dcff6328914fe4c2b44bc9
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git60882d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git60882d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git60882d9
- Initial package build

