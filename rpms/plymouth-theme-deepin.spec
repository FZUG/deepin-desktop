Name:     plymouth-theme-deepin
Version:  15.10.7
Release:  1%{?dist}
Summary:  Deepin theme for Plymouth
License:  GPLv3
URL:      https://github.com/linuxdeepin/plymouth-theme-deepin
Source0:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Requires: plymouth

%description
%{summary}.

%prep
%setup -q

%install
install -d %{buildroot}%{_datadir}/plymouth/
cp -r themes %{buildroot}%{_datadir}/plymouth/

%files
#license LICENSE
#doc README.md
%{_datadir}/plymouth/themes/deepin-hidpi-logo
%{_datadir}/plymouth/themes/deepin-hidpi-ssd-logo
%{_datadir}/plymouth/themes/deepin-logo
%{_datadir}/plymouth/themes/deepin-ssd-logo
%{_datadir}/plymouth/themes/deepin-text

%changelog
* Mon Nov 26 2018 mosquito <sensor.wen@gmail.com> - 15.10.7-1
- Initial build
