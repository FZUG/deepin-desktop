Name:           zssh
Version:        1.5c
Release:        1%{?dist}
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
* Thu Dec  7 2017 mosquito <sensor.wen@gmail.com> - 1.5c-1
- Initial package build
