# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath  github.com/alecthomas/kingpin
%global goipath2 gopkg.in/alecthomas/kingpin.v2
%global goname2  %gorpmname %{goipath2}
%global commit   947dcec5ba9c011838740e680966fd7087a71d0d

%gometa

Name:           %{goname}
Version:        2.2.6
Release:        1%{?dist}
Summary:        A Go command line and flag parser
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

%package -n compat-%{goname2}-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n compat-%{goname2}-devel
%{summary}.

This package contains compatibility glue for code
that still imports the %{goipath2} Go namespace.

%prep
%forgeautosetup

%install
%goinstall

# Add symlink to older name
install -d -p %{buildroot}%{gopath}/src/%(dirname %{goipath2})
ln -s %{gopath}/src/%{goipath} %{buildroot}%{gopath}/src/%{goipath2}

%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%doc README.md
%license COPYING

%files -n compat-%{goname2}-devel
%dir %{gopath}/src/%(dirname %{goipath2})
%{gopath}/src/%{goipath2}

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 2.2.6-1
- Release 2.2.6

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 2.2.5-1
- Release 2.2.5

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.3-1.gite9044be
- Initial package build
