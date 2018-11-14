%global pkgrel    1.0.0
%global extver    pre12

Name:           imwheel
Version:        %{pkgrel}
Release:        0.1.%{extver}%{?dist}
Summary:        Mouse Event to Key Event Mapper Daemon
License:        GPLv2+
Url:            http://imwheel.sourceforge.net
Source:         http://prdownloads.sourceforge.net/%{name}/%{name}-%{pkgrel}%{extver}.tar.gz
# PATCH-FIX-UPSTREAM to prevent compiler warnings
# "cast from pointer to integer of different size"
Patch1:         imwheel-intptr_t.patch
# PATCH-FIX-UPSTREAM to fix uninitialized variable hsi.
Patch2:         imwheel-fix_uninitialized_var.patch
# PATCH-FIX-OPENSUSE not to install to root only.
Patch3:         imwheel-fix_destdir.patch
# PATCH-FEATURE-OPENSUSE to put configs to /etc/ instead of /etc/X11.
Patch4:         imwheel-config_file_path.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)

%description
A daemon for X11, which watches for mouse wheel actions and outputs them as
keypresses. It can be configured separately for different windows. It also
allows input from it's own (included) gpm, or from jamd, or from XFree86 ZAxis
mouse wheel conversion.

%prep
%autosetup -p0 -n %{name}-%{pkgrel}%{extver}

%build
autoreconf -fiv
%configure \
  --with-x 
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog EMACS
%doc FREEBSD NEWS README
%license COPYING
%config(noreplace) %{_sysconfdir}/imwheelrc
%{_bindir}/imwheel
%{_mandir}/man1/imwheel.1*

%changelog
* Tue Nov 13 2018 mosquito <sensor.wen@gmail.com> - 1.0.0-0.1.pre12
- Package for fedora

* Tue Aug 29 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0-0.1.pre12
- Correct spec for fedora
