%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml library of cryptographic and hash functions
Name:		ocaml-cryptokit
Version:	1.9
Release:	2
License:	LGPLv2+ with linking exception
Group:		Development/Other
Url:		https://forge.ocamlcore.org/projects/cryptokit/
Source0:	http://forge.ocamlcore.org/frs/download.php/1229/cryptokit-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(zlib)

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

%files
%doc README.txt LICENSE.txt AUTHORS.txt Changes
%dir %{_libdir}/ocaml/cryptokit
%{_libdir}/ocaml/cryptokit/META
%{_libdir}/ocaml/cryptokit/*.cma
%{_libdir}/ocaml/cryptokit/*.cmi
%{_libdir}/ocaml/cryptokit/*.cmxs
%{_libdir}/ocaml/stublibs/*.so*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Requires:	pkgconfig(zlib)

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%{_libdir}/ocaml/cryptokit/*.a
%{_libdir}/ocaml/cryptokit/*.cmxa
%{_libdir}/ocaml/cryptokit/*.cmx
%{_libdir}/ocaml/cryptokit/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n cryptokit-%{version}

%build
ocaml setup.ml -debug -configure --libdir %{_libdir}
ocaml setup.ml -build

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p %{buildroot}%{_libdir}/ocaml/cryptokit
mkdir -p %{buildroot}%{_libdir}/ocaml/stublibs
ocaml setup.ml -debug -install

%check
# This opens /dev/random but never reads from it.
ocaml setup.ml -test
