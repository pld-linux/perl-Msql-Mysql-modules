%include	/usr/lib/rpm/macros.perl
Summary:	Msql-Mysql-modules perl module
Summary(pl):	Modu³ perla Msql-Mysql-modules
Name:		perl-Msql-Mysql-modules
Version:	1.2219
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/Msql-Mysql-modules-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI >= 1.08
BuildRequires:	perl-Data-ShowTable
BuildRequires:	mysql-devel >= 3.23
BuildRequires:	zlib-devel
Obsoletes:	perl-DBD-mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Msql-Mysql-modules package. This package is configured for use with
MySQL only and doesn't contain drivers for mSQL databases.

%description -l pl
Pakiet Msql-Mysql-modules. Ten pakiet jest skonfigurowany do u¿ytku z
MySQL i nie zawiera sterowników dla baz danych mSQL.

%prep
%setup -q -n Msql-Mysql-modules-%{version}

%build
perl Makefile.PL \
	--nomsql-install \
	--noprompt

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/dbimon
%{perl_sitearch}/DBD/mysql.pm
%{perl_sitearch}/Mysql.pm
%{perl_sitearch}/Mysql
%dir %{perl_sitearch}/auto/DBD/mysql
%{perl_sitearch}/auto/DBD/mysql/mysql.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/mysql/mysql.so
%{_mandir}/man1/*
%{_mandir}/man3/DBD*
%{_mandir}/man3/Mysql*
