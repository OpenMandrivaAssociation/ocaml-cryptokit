Name:           ocaml-cryptokit
Version:        1.3
Release:        %mkrel 2
Summary:        OCaml library of cryptographic and hash functions
License:        LGPLv2 with exceptions
Group:          Development/Other
URL:            http://pauillac.inria.fr/~xleroy/software.html#cryptokit
Source0:        http://caml.inria.fr/distrib/bazar-ocaml/cryptokit-%{version}.tar.gz
Source1:        cryptokit-META
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  zlib-devel
BuildRequires:  chrpath

%description
The Cryptokit library for Objective Caml provides a variety of
cryptographic primitives that can be used to implement cryptographic
protocols in security-sensitive applications. The primitives provided
include:

* Symmetric-key cryptography: AES, DES, Triple-DES, ARCfour, in ECB,
  CBC, CFB and OFB modes.
* Public-key cryptography: RSA encryption and signature; Diffie-Hellman
  key agreement.
* Hash functions and MACs: SHA-1, SHA-256, RIPEMD-160, MD5, and MACs
  based on AES and DES.
* Random number generation.
* Encodings and compression: base 64, hexadecimal, Zlib compression. 

Additional ciphers and hashes can easily be used in conjunction with
the library. In particular, basic mechanisms such as chaining modes,
output buffering, and padding are provided by generic classes that can
easily be composed with user-provided ciphers. More generally, the
library promotes a "Lego"-like style of constructing and composing
transformations over character streams.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cryptokit-%{version}

%build
make all
make allopt
chrpath --delete dllcryptokit.so
strip dllcryptokit.so

%check
# This opens /dev/random but never reads from it.
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml/cryptokit
mkdir -p %{buildroot}%{_libdir}/ocaml/cryptokit/stublibs
make INSTALLDIR=%{buildroot}%{_libdir}/ocaml/cryptokit install
mv %{buildroot}%{_libdir}/ocaml/cryptokit/stublibs \
  %{buildroot}%{_libdir}/ocaml/stublibs

sed 's/@VERSION@/%{version}/' < %{SOURCE1} \
  > %{buildroot}%{_libdir}/ocaml/cryptokit/META

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%dir %{_libdir}/ocaml/cryptokit
%{_libdir}/ocaml/cryptokit/META
%{_libdir}/ocaml/cryptokit/*.cma
%{_libdir}/ocaml/cryptokit/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc LICENSE Changes doc
%{_libdir}/ocaml/cryptokit/*.a
%{_libdir}/ocaml/cryptokit/*.cmxa
%{_libdir}/ocaml/cryptokit/*.cmx
%{_libdir}/ocaml/cryptokit/*.mli


%changelog
* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-2mdv2010.0
+ Revision: 390038
- rebuild

* Thu Jun 11 2009 Florent Monnier <blue_prawn@mandriva.org> 1.3-1mdv2010.0
+ Revision: 385289
- import ocaml-cryptokit


