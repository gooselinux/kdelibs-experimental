Name:    kdelibs-experimental
Version: 4.3.4
Release: 3%{?dist}
Summary: KDE libraries with experimental or unstable api/abi
Group:   System Environment/Libraries
License: LGPLv2+
URL:     http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdelibs-experimental-%{version}.tar.bz2
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: kdelibs4-devel >= %{version}

Requires: dbus

%description
%{summary}.

%package devel
Group:    Development/Libraries
Summary:  Development files for %{name} 
Requires: %{name} = %{version}-%{release}
Requires: kdelibs4-devel

%description devel
%{summary}.



%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot} 
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot} 


%files
%defattr(-,root,root,-)
%{_kde4_libdir}/libknotificationitem-1.so.*
%{_datadir}/dbus-1/interfaces/org.kde.NotificationItem.xml
%{_datadir}/dbus-1/interfaces/org.kde.NotificationItemWatcher.xml

%files devel
%defattr(-,root,root,-)
%{_kde4_libdir}/libknotificationitem-1.so
%{_kde4_includedir}/knotificationitem-1/


%changelog
* Tue Mar 30 2010 Than Ngo <than@redhat.com> - 4.3.4-3
- rebuilt against qt-4.6.2

* Tue Dec 29 2009 Than Ngo <than@redhat.com> - 4.3.4-2
- fix url

* Tue Dec 01 2009 Than Ngo <than@redhat.com> - 4.3.4-1
- 4.3.4

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Fri Jul 10 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Fri Jun 26 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Thu May 14 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-1
- first try
