Name:           zssh
Version:        1.5c
Release:        3%{?dist}
Summary:        SSH and Telnet client with ZMODEM file transfer capability
License:        GPLv3
URL:            http://zssh.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/zssh/zssh/1.5/%{name}-%{version}.tgz
BuildRequires:  gcc
BuildRequires:  readline-devel
BuildRequires:  libtermcap-devel

%description
%{summary}.

%prep
%setup -q

%build
%configure
%make_build

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/ztelnet
install -Dm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 0644 ztelnet.1 %{buildroot}%{_mandir}/man1/ztelnet.1

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/ztelnet
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/ztelnet.1.*

%changelog
* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5c-3
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  7 2017 mosquito <sensor.wen@gmail.com> - 1.5c-1
- Initial package build
