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
BuildRequires: perl(ExtUtils::MakeMaker)

%description
collectd gathers statistics about the system it is running on and stores this information. Those statistics can then be used to find current performance bottlenecks (i.e. performance analysis) and predict future system load (i.e. capacity planning). Or if you just want pretty graphs of your private server and are fed up with some homegrown solution you're at the right place, too ;).


%prep
%setup

%build
./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/etc/rc.d/init.d
install -m 755 %{_sourcedir}/init.d/collectd %{buildroot}/etc/rc.d/init.d/collectd

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add collectd

%preun
if [ "$1" = 0 ] ; then
  /sbin/service collectd stop > /dev/null 2>&1
  /sbin/chkconfig --del collectd
fi
exit 0

%files
%defattr(-,root,root,-)
/usr/local/lib/libcollectdclient.*
/usr/local/lib/pkgconfig/libcollectdclient.pc
/usr/local/lib/collectd/*
/etc/rc.d/init.d/collectd

%config(noreplace) /etc/collectd.conf

/usr/local/include/collectd/*

/usr/local/sbin/collectdmon
/usr/local/sbin/collectd
/usr/local/bin/collectdctl
/usr/local/bin/collectd-nagios
/usr/local/bin/collectd-tg
/usr/local/lib64/perl5/auto/Collectd/.packlist
/usr/local/lib64/perl5/perllocal.pod

%doc
/usr/local/share/perl5/Collectd.pm
/usr/local/share/perl5/Collectd/*
/usr/local/share/man/man3/Collectd*

/usr/local/share/man/man1/collectd*
/usr/local/share/man/man5/types.db.5

/usr/local/share/man/man5/collectd*

/usr/local/share/collectd/*


%changelog

