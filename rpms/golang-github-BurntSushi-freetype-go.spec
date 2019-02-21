# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath     github.com/BurntSushi/freetype-go/freetype
%global forgeurl    https://github.com/golang/freetype
%global commit      e2365dfdc4a05e4b8299a783240d4a7d5a65d4e4
%global goipath2    github.com/golang/freetype
%global goname2     %gorpmname %{goipath2}

%gometa

Name:           golang-github-BurntSushi-freetype-go
Version:        0
Release:        0.7%{?dist}
Summary:        The Freetype font rasterizer in the Go programming language
# Detected licences
# - *No copyright* UNKNOWN at 'LICENSE'
License:        GPLv2+ or FTL
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

%package -n %{goname2}-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{goname2}-devel
%{summary}.

This package contains compatibility glue for code
that still imports the %{goipath2} Go namespace.

%prep
%forgeautosetup

%install
%goinstall -i %{goipath2}

# Add symlink to older name
install -d -p %{buildroot}%{gopath}/src/%(dirname %{goipath})
ln -s %{gopath}/src/%{goipath2} %{buildroot}%{gopath}/src/%{goipath}

%if %{with check}
%check
%gochecks
%endif

%files devel
%dir %{gopath}/src/%(dirname %{goipath})
%{gopath}/src/%{goipath}

%files -n %{goname2}-devel -f golang-github-freetype-devel.file-list
%license LICENSE
%doc README CONTRIBUTORS AUTHORS

%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gite2365df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 mosquito <sensor.wen@gmail.com> - 0-0.6.20181119gite2365df
- Fix go import path

* Wed Nov 14 2018 mosquito <sensor.wen@gmail.com> - 0-0.5.20181114gite2365df
- Change upstream to github.com/golang/freetype

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181113gitb763ddb
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitb763ddb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitb763ddb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitb763ddb
- Initial package build
