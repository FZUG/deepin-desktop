# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/disintegration/imaging
%global commit  0bd5694c78c9c3d9a3cd06a706a8f3c59296a9ac

%gometa

Name:           %{goname}
Version:        1.5.0
Release:        1%{?dist}
Summary:        Simple Go image processing package
License:        MIT
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
%{import_path} prefix.

%prep
%forgeautosetup

%install
%goinstall
sed -i 's|\r||g' README.md

%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%doc README.md
%license LICENSE

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3.gita585802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2.gita585802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug  8 2017 mosquito <sensor.wen@gmail.com> - 1.2.1-1
- Initial package build
