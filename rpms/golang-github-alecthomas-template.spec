# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/alecthomas/template
%global commit  a0175ee3bccc567396460bf5acd36800cb10c49c

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Go's text/template package with newline elision
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
%{import_path} prefix.

%prep
%forgeautosetup

%install
%goinstall

%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%doc README.md
%license LICENSE

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104gita0175ee
- Rewrite rpm spec

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gita0175ee
- Initial package
