%global md5() {$(echo -n %1 | md5sum | awk '{print$1}')}
%global fedora_release_name f30

Name:           deepin-wallpapers
Version:        1.7.6
Release:        4%{?dist}
Summary:        Deepin Wallpapers provides wallpapers of dde
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-wallpapers
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  deepin-api
# convert default Fedora wallpaper to jpg format
BuildRequires:  /usr/bin/convert
# for the current default wallpaper
BuildRequires:  %{fedora_release_name}-backgrounds-base

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}
sed -i 's|lib|libexec|' Makefile

%build
mv deepin/desktop.jpg deepin/deepin-desktop.jpg
convert %{_datadir}/backgrounds/%{fedora_release_name}/default/standard/%{fedora_release_name}.png \
        deepin/desktop.jpg
%make_build

%install
install -d %{buildroot}%{_datadir}/wallpapers/deepin/
cp deepin/* deepin-private/* deepin-community/* %{buildroot}%{_datadir}/wallpapers/deepin/

install -d %{buildroot}%{_var}/cache/
cp -ar image-blur %{buildroot}%{_var}/cache/

install -d %{buildroot}%{_datadir}/backgrounds/deepin/
ln -sv ../../wallpapers/deepin/Hummingbird_by_Shu_Le.jpg \
  %{buildroot}%{_datadir}/backgrounds/deepin/desktop.jpg
ln -sv %{md5 %{_datadir}/wallpapers/deepin/Hummingbird_by_Shu_Le.jpg}.jpg \
  %{buildroot}%{_var}/cache/image-blur/%{md5 %{_datadir}/backgrounds/deepin/desktop.jpg}.jpg

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove deepin-deepin-background %{_datadir}/wallpapers/deepin/desktop.jpg
fi

%post
if [ $1 -ge 1 ]; then
  %{_sbindir}/alternatives --install %{_datadir}/backgrounds/default_background.jpg \
    deepin-default-background %{_datadir}/wallpapers/deepin/desktop.jpg 50
fi

%files
%doc README.md
%license LICENSE
%{_datadir}/backgrounds/deepin/
%{_datadir}/wallpapers/deepin/
%{_var}/cache/image-blur/

%changelog
* Wed Mar 13 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.7.6-4
- Convert default wallpaper to jpg instead of schema override, since some other
  deepin packages hard coded the desktop.jpg path.
- Follow upstream to add an alternative 'deepin-default-background'

* Thu Feb 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.7.6-3
- Follow Fedora default wallpaper

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 mosquito <sensor.wen@gmail.com> - 1.7.6-1
- Update to 1.7.6

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 1.7.5-1
- Update to 1.7.5

* Fri Jul 20 2018 mosquito <sensor.wen@gmail.com> - 1.7.4-1
- Update to 1.7.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 1.7-1
- Update to 1.7

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.6-1
- Update to 1.6

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.4-1.gita54c282
- Update to 1.4

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.3-1.gitdbc981b
- Update to 1.3

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build
