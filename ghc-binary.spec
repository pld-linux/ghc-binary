%define	pkgname	binary
Summary:	Binary serialisation for Haskell values using lazy ByteStrings
Name:		ghc-%{pkgname}
Version:	0.5.0.2
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/packages/archive/%{pkgname}/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	6bf8f3d1441602c9ab09a75e3bd6e926
URL:		http://hackage.haskell.org/package/%{pkgname}/
BuildRequires:	ghc >= 6.10
%requires_eq	ghc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		libsubdir	ghc-%(/usr/bin/ghc --numeric-version)/%{pkgname}-%{version}

%description
Efficient, pure binary serialisation using lazy ByteStrings. Haskell
values may be encoded to and from binary formats, written to disk as
binary, or sent over the network. Serialisation speeds of over 1 G/sec
have been observed, so this library should be suitable for high
performance scenarios.

%prep
%setup -q -n %{pkgname}-%{version}

%build
./Setup.lhs configure -v2 \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--libsubdir=%{libsubdir} \
	--docdir=%{_defaultdocdir}/%{name}-%{version}

./Setup.lhs build
./Setup.lhs haddock --executables

%install
rm -rf $RPM_BUILD_ROOT
./Setup.lhs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
rm -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version} %{name}-%{version}-doc

./Setup.lhs register \
	--gen-pkg-config=$RPM_BUILD_ROOT/%{_libdir}/%{libsubdir}/%{pkgname}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/ghc-pkg update %{_libdir}/%{libsubdir}/%{pkgname}.conf

%postun
if [ "$1" = "0" ]; then
	/usr/bin/ghc-pkg unregister %{pkgname}-%{version}
fi

%files
%defattr(644,root,root,755)
%doc README todo
%doc %{name}-%{version}-doc/html
%{_libdir}/%{libsubdir}
