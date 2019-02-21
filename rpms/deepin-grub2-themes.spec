%global debug_package %{nil}

Name:           deepin-grub2-themes
Version:        1.0.0
Release:        5%{?dist}
Summary:        Deepin grub2 themes
License:        CC-BY-SA
URL:            https://github.com/linuxdeepin/deepin-grub2-themes
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
# matches grub2 pkg archs
ExcludeArch:    s390 s390x
%ifnarch aarch64 %{arm}
Requires:       grub2
%else
Requires:       grub2-efi
%endif

%description
Deepin grub2 themes

%prep
%setup -q

%install
%make_install TARGET="%{buildroot}/boot/grub2/themes"

%files
%license LICENSE
/boot/grub2/themes/deepin/

%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.0-4
- ARMv7 now has grub2-efi

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.0-1
- Initial package build
