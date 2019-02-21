Name:           deepin-sound-theme
Version:        15.10.3
Release:        2%{?dist}
Summary:        Deepin sound theme
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-sound-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Sound files for the Deeping Desktop Environment.

%prep
%setup -q

%build

%install
%make_install

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/sounds/deepin/
%dir %{_datadir}/sounds/deepin/stereo/
%{_datadir}/sounds/deepin/index.theme
%{_datadir}/sounds/deepin/stereo/*.wav

%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 15.10.3-1
- Update to 15.10.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 15.10.2-1
- Update to 15.10.2

* Sun Aug  6 2017 mosquito <sensor.wen@gmail.com> - 15.10.1-1
- Rebuild

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 15.10.1-1.git0045de4
- Update to 15.10.1

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build
