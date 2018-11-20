# https://github.com/BurntSushi/graphics-go
%global goipath         github.com/BurntSushi/graphics-go
%global commit          b43f31a4a96688fba0b612e25e22648b9267e498

%gometa

Name:           golang-github-BurntSushi-graphics-go
Version:        0
Release:        0.5%{?dist}
Summary:        Graphics library for the Go programming language
# Detected licences
# - BSD 3-clause "New" or "Revised" License at 'LICENSE'
License:        BSD
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
%{goipath} prefix.


%prep
%forgeautosetup


%install
files=$(find . -name "testdata" -type d)
%goinstall $files


%check
# Fail on some arches
%ifnarch s390x ppc64le aarch64
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README CONTRIBUTORS AUTHORS


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20181113gitb43f31a
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitb43f31a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitb43f31a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 mosquito <sensor.wen@gmail.com> - 0-0.2.gitb43f31a
- ignore test error for ppc64le

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitb43f31a
- Initial package build
