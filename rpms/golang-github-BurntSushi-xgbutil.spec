# https://github.com/BurntSushi/xgbutil
%global goipath         github.com/BurntSushi/xgbutil
%global commit          f7c97cef3b4e6c88280a5a7091c3314e815ca243

%gometa

Name:           golang-github-BurntSushi-xgbutil
Version:        0
Release:        0.4%{?dist}
Summary:        A utility library to make use of the X Go Binding easier
# Detected licences
# - do What The Fuck you want to Public License (v2) at 'COPYING'
License:        WTFPL
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/freetype-go/freetype)
BuildRequires:  golang(github.com/BurntSushi/freetype-go/freetype/truetype)
BuildRequires:  golang(github.com/BurntSushi/graphics-go/graphics)
BuildRequires:  golang(github.com/BurntSushi/xgb)
BuildRequires:  golang(github.com/BurntSushi/xgb/shape)
BuildRequires:  golang(github.com/BurntSushi/xgb/xinerama)
BuildRequires:  golang(github.com/BurntSushi/xgb/xproto)

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
%doc README


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181113gitf7c97ce
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf7c97ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf7c97ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitf7c97ce
- Add description

* Wed Dec 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek - 0.0.1.gitf7c97ce
- Initial package build
