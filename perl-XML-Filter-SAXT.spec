%define real_name XML-Filter-SAXT

Summary:	XML::Filter::SAXT - replicates SAX events to several SAX event handlers
Name:		perl-%{real_name}
Version:	0.01
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SAXT is like the Unix 'tee' command in that it multiplexes the input
stream to several output streams. In this case, the input stream is a
PerlSAX event producer (like XML::Parser::PerlSAX) and the output
streams are PerlSAX handlers or filters.

%prep
%setup -q -n %{real_name}-%{version} 

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


