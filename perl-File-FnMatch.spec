#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	File
%define		pnam	FnMatch
%include	/usr/lib/rpm/macros.perl
Summary:	File::FnMatch - simple filename and pathname matching
Name:		perl-File-FnMatch
Version:	0.02
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22f77c20d0fb5af01a3165e2df2fe34c
URL:		https://metacpan.org/release/File-FnMatch/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::FnMatch::fnmatch() provides simple, shell-like pattern matching.

Though considerably less powerful than regular expressions, shell
patterns are nonetheless useful and familiar to a large audience of
end-users.

Other possibilities include at least FNM_CASEFOLD (compare qr//i),
FNM_LEADING_DIR to restrict matching to everything before the first
'/', FNM_FILE_NAME as a synonym for FNM_PATHNAME, and the rather more
exotic FNM_EXTMATCH. Consult your system documentation for details.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/File/*.pm
%dir %{perl_vendorarch}/auto/File/FnMatch
%attr(755,root,root) %{perl_vendorarch}/auto/File/FnMatch/*.so
%{_mandir}/man3/*
