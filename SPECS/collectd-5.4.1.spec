Name:	collectd
Version: 5.4.1	
Release:	1%{?dist}
Summary: collectd

Source: https://collectd.org/files/collectd-5.4.1.tar.bz2
URL: https://collectd.org/download.shtml
Distribution: CentOS 6.5
Packager: Yang Hongbo <hongbo@yang.me>

Group:	Administration/Tools
License: GPL v2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# BuildRequires: perl(ExtUtils::MakeMaker)

%description
collectd gathers statistics about the system it is running on and stores this information. Those statistics can then be used to find current performance bottlenecks (i.e. performance analysis) and predict future system load (i.e. capacity planning). Or if you just want pretty graphs of your private server and are fed up with some homegrown solution you're at the right place, too ;).


%prep
%setup

%build
%configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --libdir=%{_libdir} --mandir=%{_mandir} --bindir=%{_bindir} --sbindir=%{_sbindir} --datadir=%{_datadir} --includedir=%{_includedir}
make

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/etc/rc.d/init.d
install -m 755 %{_sourcedir}/init.d/collectd %{buildroot}/etc/rc.d/init.d/collectd

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add collectd
/sbin/chkconfig --level 3456 collectd

%preun
if [ "$1" = 0 ] ; then
  /sbin/service collectd stop > /dev/null 2>&1
  /sbin/chkconfig --del collectd
fi
exit 0

%changelog

%files
%defattr(-,root,root,-)
%{_libdir}/libcollectdclient.*
%{_libdir}/pkgconfig/libcollectdclient.pc
%{_libdir}/collectd/*
%{_sysconfdir}/rc.d/init.d/collectd

%config(noreplace) %{_sysconfdir}/collectd.conf

%{_includedir}/collectd/*

%{_sbindir}/collectdmon
%{_sbindir}/collectd
%{_bindir}/collectdctl
%{_bindir}/collectd-nagios
%{_bindir}/collectd-tg
%{_libdir}/perl5/auto/Collectd/.packlist
%{_libdir}/perl5/perllocal.pod

%doc
%{_datadir}/perl5/Collectd.pm
%{_datadir}/perl5/Collectd/*
%{_mandir}/man3/Collectd*
%{_mandir}/man1/collectd*
%{_mandir}/man5/types.db.5*

%{_mandir}/man5/collectd*

%{_datadir}/collectd/*


