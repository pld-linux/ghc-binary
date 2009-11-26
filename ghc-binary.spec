Summary:	Binary serialisation for Haskell values using lazy ByteStrings
Name:		haskell-binary
Version:	0.5.0.2
Release:	0.1
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/packages/archive/binary/0.5.0.2/binary-%{version}.tar.gz
# Source0-md5:	6bf8f3d1441602c9ab09a75e3bd6e926
URL:		http://hackage.haskell.org/package/hashed-storage/
BuildRequires:	haskell
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Efficient, pure binary serialisation using lazy ByteStrings. Haskell
values may be encoded to and from binary formats, written to disk as
binary, or sent over the network. Serialisation speeds of over 1 G/sec
have been observed, so this library should be suitable for high
performance scenarios.

%prep
%setup -q -n binary-%{version}

%build
runhaskell Setup.lhs configure \
	--global \
	--prefix=%{_prefix}

runhaskell Setup.lhs build

%install
rm -rf $RPM_BUILD_ROOT
runhaskell Setup.lhs copy --destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
FIXME
