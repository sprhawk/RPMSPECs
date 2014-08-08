Name:	libevent2
Version: 2.0.21
Release:	1%{?dist}
Summary: libevent 

Source: https://github.com/downloads/libevent/libevent/libevent-%{version}-stable.tar.gz
URL: http://libevent.org/
Distribution: CentOS 6.5
Packager: Yang Hongbo <hongbo@yang.me>

Group:	Libraries
License: 3-Clause BSD
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The libevent API provides a mechanism to execute a callback function when a specific event occurs on a file descriptor or after a timeout has been reached. Furthermore, libevent also support callbacks due to signals or regular timeouts.
libevent is meant to replace the event loop found in event driven network servers. An application just needs to call event_dispatch() and then add or remove events dynamically without having to change the event loop.

%package devel
Summary: Libraries, headers and documentation for libevent
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The libevent libraries, headers and devel document

%prep
%setup -n libevent-%{version}-stable

%build
%configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --libdir=%{_libdir} --mandir=%{_mandir} --bindir=%{_bindir} --sbindir=%{_sbindir} --datadir=%{_datadir} --includedir=%{_includedir}
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig %{_libdir}

%changelog

%files
%defattr(-,root,root,-)
%{_libdir}/libevent_extra-2.0.so.5
%{_libdir}/libevent_pthreads-2.0.so.5
%{_libdir}/libevent_core.so
%{_libdir}/libevent_pthreads-2.0.so.5.1.9
%{_libdir}/libevent_extra.so
%{_libdir}/pkgconfig/libevent_pthreads.pc
%{_libdir}/pkgconfig/libevent.pc
%{_libdir}/libevent_extra-2.0.so.5.1.9
%{_libdir}/libevent_core-2.0.so.5
%{_libdir}/libevent-2.0.so.5
%{_libdir}/libevent_core-2.0.so.5.1.9
%{_libdir}/libevent-2.0.so.5.1.9
%{_libdir}/libevent.so
%{_libdir}/libevent_pthreads.so

%files devel
%defattr(-,root,root,-)
%{_libdir}/libevent.a
%{_libdir}/libevent.la
%{_libdir}/libevent_core.a
%{_libdir}/libevent_core.la
%{_libdir}/libevent_pthreads.a
%{_libdir}/libevent_pthreads.la
%{_libdir}/libevent_extra.a
%{_libdir}/libevent_extra.la
%{_includedir}/evrpc.h
%{_includedir}/evhttp.h
%{_includedir}/event.h
%{_includedir}/evutil.h
%{_includedir}/event2/event-config.h
%{_includedir}/event2/rpc.h
%{_includedir}/event2/bufferevent_compat.h
%{_includedir}/event2/rpc_compat.h
%{_includedir}/event2/event.h
%{_includedir}/event2/thread.h
%{_includedir}/event2/keyvalq_struct.h
%{_includedir}/event2/event_struct.h
%{_includedir}/event2/bufferevent_struct.h
%{_includedir}/event2/http.h
%{_includedir}/event2/bufferevent_ssl.h
%{_includedir}/event2/tag.h
%{_includedir}/event2/buffer_compat.h
%{_includedir}/event2/http_struct.h
%{_includedir}/event2/event_compat.h
%{_includedir}/event2/util.h
%{_includedir}/event2/buffer.h
%{_includedir}/event2/tag_compat.h
%{_includedir}/event2/rpc_struct.h
%{_includedir}/event2/dns.h
%{_includedir}/event2/dns_struct.h
%{_includedir}/event2/bufferevent.h
%{_includedir}/event2/listener.h
%{_includedir}/event2/dns_compat.h
%{_includedir}/event2/http_compat.h
%{_includedir}/evdns.h
%{_bindir}/event_rpcgen.py



