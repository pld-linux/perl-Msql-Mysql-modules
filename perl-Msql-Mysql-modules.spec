#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# require server access
#
%include	/usr/lib/rpm/macros.perl
Summary:	Msql-Mysql-modules perl module
Summary(pl):	Modu³ Perla Msql-Mysql-modules
Name:		perl-Msql-Mysql-modules
Version:	1.2219
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/Msql-Mysql-modules-%{version}.tar.gz
# Source0-md5:	ad3dec1881d4c4ff9a353f33ff434b5f
BuildRequires:	mysql-devel >= 3.23
BuildRequires:	perl-DBI >= 1.08
BuildRequires:	perl-Data-ShowTable
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--mysql-libdir=%{_libdir} \
	--nomsql-install \
	--noprompt
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/dbimon
%{perl_vendorarch}/DBD/mysql.pm
%{perl_vendorarch}/Mysql.pm
%{perl_vendorarch}/Mysql
%dir %{perl_vendorarch}/auto/DBD/mysql
%{perl_vendorarch}/auto/DBD/mysql/mysql.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/mysql/mysql.so
%{_mandir}/man1/*
%{_mandir}/man3/DBD*
%{_mandir}/man3/Mysql*
