%define upstream_name    XML-Filter-SAXT
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	XML::Filter::SAXT - replicates SAX events to several SAX event handlers
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno

%description
SAXT is like the Unix 'tee' command in that it multiplexes the input
stream to several output streams. In this case, the input stream is a
PerlSAX event producer (like XML::Parser::PerlSAX) and the output
streams are PerlSAX handlers or filters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML/Filter/SAXT.pm
%{_mandir}/*/*
