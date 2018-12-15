# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath  pkg.deepin.io/lib
%global forgeurl https://github.com/linuxdeepin/go-lib
%global commit   4d9427f49e7ce0d4c50beece26f9f86d473401e1

%gometa

Name:           golang-deepin-go-lib
Version:        1.6.0
Release:        1%{?dist}
Summary:        Go bindings for Deepin Desktop Environment development
License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

%description
DLib is a set of Go bindings/libraries for DDE development.
Containing dbus (forking from guelfey), glib, gdkpixbuf, pulse and more.

%package devel
Summary:        %{summary}
BuildArch:      noarch
%if %{with check}
# Required for tests
BuildRequires:  deepin-gir-generator
BuildRequires:  dbus-x11
BuildRequires:  iso-codes
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  golang(github.com/linuxdeepin/go-x11-client)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(libpulse)
%endif

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

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
* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 1.6.0-1.20181212git4d9427f
- Update to 1.6.0

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 1.4.0-1.20181129gitd86462c
- Update to 1.4.0

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 1.3.0-1.20181119gitb199d0d
- Update to 1.3.0

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 1.2.11-1
- Back to 1.2.11

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 1.2.15-1
- Update to 1.2.15

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 1.2.14-1
- Update to 1.2.14

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 mosquito <sensor.wen@gmail.com> - 1.2.4-2
- Disable test suit

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 mosquito <sensor.wen@gmail.com> - 1.2.3-1
- Update to 1.2.3

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Sat Oct 14 2017 mosquito <sensor.wen@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Thu Aug 24 2017 mosquito <sensor.wen@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Sun Aug  6 2017 mosquito <sensor.wen@gmail.com> - 1.0.5-2
- Rename to golang-deepin-go-lib

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.0.5-1.git3c9791f
- Update to 1.0.5

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.0.3-1.gitb084e27
- Update to 1.0.3

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 0.5.5-1.git01150d5
- Update to 0.5.5

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.5.3-1.git44767e8
- Update to 0.5.3

* Sun Jul 12 2015 mosquito <sensor.wen@gmail.com> - 0.3.0-1.git98ac007
- Update to 0.3.0-1.git98ac007

* Mon Sep 29 2014 mosquito <sensor.wen@gmail.com> - 0.0.4git20140928-1
- Initial build
