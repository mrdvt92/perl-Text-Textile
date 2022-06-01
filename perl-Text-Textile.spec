Name:           perl-Text-Textile
Version:        2.13
Release:        1%{?dist}
Summary:        Text::Textile Perl module
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Textile/
Source0:        http://www.cpan.org/modules/by-module/Text/Text-Textile-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Harness) >= 2.5
BuildRequires:  perl(Test::More)
Requires:       perl(Exporter)
Requires:       perl(Test::Harness) >= 2.5
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
bc. perl Makefile.PL make make test make install

%prep
%setup -q -n Text-Textile-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ARTISTIC Changes META.json README.textile
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Tue May 31 2022 Michael R. Davis <mrdvt92@yahoo.com> 2.13-1
- Specfile autogenerated by cpanspec 1.78.
