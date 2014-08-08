Name:	tmux
Version: 1.9a
Release:	1%{?dist}
Summary: Terminal multiplexer program

Source: http://downloads.sourceforge.net/tmux/tmux-1.9a.tar.gz
URL: http://tmux.sourceforge.net/
Distribution: CentOS 6.5
Packager: Yang Hongbo <hongbo@yang.me>

Group:	Applications/System
License: BSD
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libevent2-devel >= 2.0, ncurses-devel
Requires: libevent2 >= 2.0, ncurses

%description
tmux is a "terminal multiplexer", it enables a number of terminals (or windows)
to be accessed and controlled from a single terminal. tmux is intended to be a
simple, modern, BSD-licensed alternative to programs such as GNU screen.

%prep
%setup

%build
%configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --libdir=%{_libdir} --mandir=%{_mandir} --bindir=%{_bindir} --sbindir=%{_sbindir} --datadir=%{_datadir} --includedir=%{_includedir}
%{__make}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%changelog

%files
%defattr(-,root,root,-)
%{_bindir}/tmux

%doc
%{_mandir}/man1/tmux.1*



