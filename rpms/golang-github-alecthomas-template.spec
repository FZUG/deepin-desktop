# https://github.com/alecthomas/template
%global goipath         github.com/alecthomas/template
%global commit          a0175ee3bccc567396460bf5acd36800cb10c49c

%gometa

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Go's text/template package with newline elision
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
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181111gita0175ee
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gita0175ee
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gita0175ee
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gita0175ee
- Initial package
