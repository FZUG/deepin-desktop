# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/msteinert/pam
%global commit  2c288b3ef8272766b4243917240e04e4221eb4a5

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Go wrapper module for the Pluggable Authentication Modules(PAM) API
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  pam-devel
BuildRequires:  golang(github.com/bgentry/speakeasy)

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%forgeautosetup

%install
gofiles=$(find . %{gofindfilter} -or -iname "*.c" -print)
%goinstall $gofiles

%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%doc README.md
%license LICENSE

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104git2c288b3
- Rewrite rpm spec

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git2c288b3
- Initial package build
