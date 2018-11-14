# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/cryptix/wav
%global commit  8bdace674401f0bd3b63c65479b6a6ff1f9d5e44

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        golang wav reader and writer
License:        GPLv2
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       golang(%{import_path}) = %{version}-%{release}

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
%doc README.md examples/
%license LICENSE

%changelog
* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181109git8bdace6
- Update to 8bdace6

* Thu Dec 21 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.20171018git7b3d650
- Initial package build
