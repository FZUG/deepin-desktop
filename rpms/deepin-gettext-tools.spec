Name:           deepin-gettext-tools
Version:        1.0.8
Release:        2%{?dist}
Summary:        Deepin Gettext Tools
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-gettext-tools
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::PrettyPrint)
Requires:       gettext
Requires:       qt5-linguist
Requires:       perl(Config::Tiny)
Requires:       perl(Exporter::Tiny)
Requires:       perl(XML::LibXML)
Requires:       perl(XML::LibXML::PrettyPrint)

%description
The tools of gettext function wrapper.

desktop-ts-convert - handling desktop file translations.
policy-ts-convert - convert PolicyKit Policy file to the ts file.
update-pot - scan msgid and generate pot file according to the ini file.
generate-mo - scan po files and generate mo files according to the ini file.

%prep
%setup -q

# fix shebang
find -iname "*.py" | xargs sed -i '1s|.*|#!%{__python3}|'
sed -i '1s|.*|#!%{__perl}|' src/desktop_ts_convert.pl

sed -i 's|sudo cp|cp|' src/generate_mo.py
sed -i 's|lconvert|lconvert-qt5|; s|deepin-lupdate|lupdate-qt5|' src/update_pot.py

%build

%install
install -d %{buildroot}%{_bindir}
install -m755 src/desktop_ts_convert.pl %{buildroot}%{_bindir}/deepin-desktop-ts-convert
install -m755 src/policy_ts_convert.py %{buildroot}%{_bindir}/deepin-policy-ts-convert
install -m755 src/generate_mo.py %{buildroot}%{_bindir}/deepin-generate-mo
install -m755 src/update_pot.py %{buildroot}%{_bindir}/deepin-update-pot

%check
/bin/perl src/desktop_ts_convert.pl --help
/bin/python3 src/generate_mo.py --help
/bin/python3 src/update_pot.py --help

%files
%doc README.md
%license LICENSE
%{_bindir}/deepin-desktop-ts-convert
%{_bindir}/deepin-policy-ts-convert
%{_bindir}/deepin-update-pot
%{_bindir}/deepin-generate-mo

%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Zamir SUN <zsun@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 1.0.7-1
- Update to 1.0.7

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.0.6-1.git8f4a8ab
- Update to 1.0.6

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.0.4-1.git4303c4a
- Rebuild

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.4-1
- Update to version 1.0.4

* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.3-1
- Initial package build
