Name:		texlive-yquant
Version:	63255
Release:	2
Summary:	Typesetting quantum circuits in a human-readable language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yquant
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yquant.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yquant.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package allows to quickly draw quantum circuits. It
bridges the gap between the two groups of packages that already
exist: those that use a logic-oriented custom language, which
is then translated into TeX by means of an external program;
and the pure TeX versions that mainly provide some macros to
allow for an easier input. yquant is a pure-LaTeX solution --
i.e., it requires no external program -- that introduces a
logic oriented language and thus brings the best of both worlds
together. It builds on and interacts with TikZ, which brings an
enourmous flexibility for customization of individual circuit.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/yquant
%doc %{_texmfdistdir}/doc/latex/yquant

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
