# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/BurntSushi/xgbutil
%global commit  f7c97cef3b4e6c88280a5a7091c3314e815ca243

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        XGB is the X protocol Go language Binding
License:        WTFPL
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch

%description devel
%{summary}.

xgbutil is a utility library designed to work with the X Go Binding. This
project's main goal is to make various X related tasks easier. For example,
binding keys, using the EWMH or ICCCM specs with the window manager,
moving/resizing windows, assigning function callbacks to particular events,
drawing images to a window, etc.

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
%doc README
%license COPYING

%changelog
* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.2.20181104gitf7c97ce
- Rewrite rpm spec

* Tue Aug 15 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitf7c97ce
- Add description

* Wed Dec 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.1.gitf7c97ce
- Initial package build
