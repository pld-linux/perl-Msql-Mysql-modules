%include	/usr/lib/rpm/macros.perl
Summary:	Msql-Mysql-modules perl module
Summary(pl):	Modu³ perla Msql-Mysql-modules
Name:		perl-Msql-Mysql-modules
Version:	1.2210
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/Msql-Mysql-modules-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-DBI >= 1.08
BuildRequires:	perl-Data-ShowTable
BuildRequires:	mysql-devel
BuildRequires:	zlib-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Msql-Mysql-modules package. 
This package is configured for use with MySQL only and doesn't contain 
drivers for mSQL databases.

%description -l pl
Pakiet Msql-Mysql-modules. 
Ten pakiet jest skonfigurowany do u¿ytku z MySQL i nie zawiera sterowników
dla baz danych mSQL.

%prep
%setup -q -n Msql-Mysql-modules-%{version}

%build
perl Makefile.PL \
	--nomsql-install \
	--noprompt

make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{perl_sitearch}/auto/DBD/mysql/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Msql-Mysql-modules
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz
%attr(755,root,root) %{_bindir}/dbimon

%{perl_sitearch}/Bundle/DBD/mysql.pm
%{perl_sitearch}/DBD/mysql.pm
%{perl_sitearch}/Mysql.pm
%{perl_sitearch}/Mysql
%{perl_sitearch}/auto/DBD/mysql/mysql.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/mysql/mysql.so

%{perl_sitearch}/auto/Msql-Mysql-modules

%{_mandir}/man[13]/*
