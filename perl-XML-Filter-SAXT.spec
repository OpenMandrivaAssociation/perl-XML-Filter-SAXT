%define modname	XML-Filter-SAXT
%define modver	0.01

Summary:	XML::Filter::SAXT - replicates SAX events to several SAX event handlers
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:	http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
Provides:	perl-libxml-enno = %{version}-%{release}

%description
SAXT is like the Unix 'tee' command in that it multiplexes the input
stream to several output streams. In this case, the input stream is a
PerlSAX event producer (like XML::Parser::PerlSAX) and the output
streams are PerlSAX handlers or filters.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/Filter/SAXT.pm
%{_mandir}/man3/*

