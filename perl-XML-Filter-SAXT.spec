%define upstream_name    XML-Filter-SAXT
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	XML::Filter::SAXT - replicates SAX events to several SAX event handlers
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
Provides:	perl-libxml-enno = %{version}-%{release}

%description
SAXT is like the Unix 'tee' command in that it multiplexes the input
stream to several output streams. In this case, the input stream is a
PerlSAX event producer (like XML::Parser::PerlSAX) and the output
streams are PerlSAX handlers or filters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/Filter/SAXT.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-4mdv2012.0
+ Revision: 765842
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-3
+ Revision: 764338
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2
+ Revision: 667419
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 401861
- rebuild using %%perl_convert_version

* Wed Sep 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.01-6mdv2009.0
+ Revision: 287786
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.01-4mdv2008.1
+ Revision: 180655
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.01-3mdv2007.0
+ Revision: 85632
- Import perl-XML-Filter-SAXT

* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.01-3
- use the %%mkrel macro

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.01-2mdk
- fix deps

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdk
- initial Mandriva package

