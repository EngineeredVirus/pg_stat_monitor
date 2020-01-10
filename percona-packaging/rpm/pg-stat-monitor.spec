%global sname percona-pg-stat-monitor
%global pginstdir /usr/pgsql-11/
%global pgstatmonmajver 1
%global pgstatmonmidver 0
%global pgstatmonminver 0

Summary:        Statistics collector for PostgreSQL
Name:           %{sname}
Version:        %{pgstatmonmajver}.%{pgstatmonmidver}.%{pgstatmonminver}
Release:        1%{?dist}
License:        Apache 2.0
Source0:        %{sname}-%{pgstatmonmajver}.%{pgstatmonmidver}.%{pgstatmonminver}.tar.gz
URL:            https://github.com/Percona-Lab/pg_stat_monitor
BuildRequires:  percona-postgresql11-devel
Requires:       percona-postgresql11-server


%description
The pg_stat_monitor is statistics collector tool
based on PostgreSQL's contrib module "pg_stat_statements".
.
pg_stat_monitor is developed on the basis of pg_stat_statments
as more advanced replacement for pg_stat_statment.
It provides all the features of pg_stat_statment plus its own feature set.


%prep
%setup -q -n %{sname}-%{pgstatmonmajver}.%{pgstatmonmidver}.%{pgstatmonminver}


%build
sed -i 's:PG_CONFIG = pg_config:PG_CONFIG = /usr/pgsql-11/bin/pg_config:' Makefile
%{__make} USE_PGXS=1 %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} USE_PGXS=1 %{?_smp_mflags} install DESTDIR=%{buildroot}
%{__install} -d %{buildroot}%{pginstdir}/share/extension
%{__install} -m 755 README.md %{buildroot}%{pginstdir}/share/extension/README-pg_stat_monitor


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(755,root,root,755)
%doc %{pginstdir}/share/extension/README-pg_stat_monitor
%{pginstdir}/lib/pg_stat_monitor.so
%{pginstdir}/share/extension/pg_stat_monitor--*.sql
%{pginstdir}/share/extension/pg_stat_monitor.control
%{pginstdir}/lib/bitcode/pg_stat_monitor*.bc
%{pginstdir}/lib/bitcode/pg_stat_monitor/*.bc


%changelog
* Thu Dec 19 2019 Oleksandr Miroshnychenko <alex.miroshnychenko@percona.com> - 1.0.0-1
- Initial build
