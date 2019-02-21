# https://github.com/axgle/mahonia
%global goipath         github.com/axgle/mahonia
%global commit          3358181d7394e26beccfae0ffde05193ef3be33a

%gometa

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Character-set conversion library implemented in Go
# Detected licences
# - *No copyright* UNKNOWN at 'LICENSE'
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
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git3358181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181112git3358181
- Bump to commit 3358181d7394e26beccfae0ffde05193ef3be33a
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitc528b74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitc528b74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0.1-1
- Initial package build
- First package for Fedora

