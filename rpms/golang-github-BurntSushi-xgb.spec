# https://github.com/BurntSushi/xgb
%global goipath         github.com/BurntSushi/xgb
%global commit          27f122750802c950b2c869a5b63dafcf590ced95

%gometa

Name:           golang-github-BurntSushi-xgb
Version:        0
Release:        0.5%{?dist}
Summary:        A low-level API to communicate with the X server in Go
# Detected licences
# - BSD 3-clause "New" or "Revised" License at 'LICENSE'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

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
%gochecks -d xproto


%files devel -f devel.file-list
%license LICENSE
%doc README CONTRIBUTORS AUTHORS


%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git27f1227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181113git27f1227
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git27f1227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git27f1227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git27f1227
- Initial package
