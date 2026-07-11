%global tl_name yquant
%global tl_revision 77263

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	Typesetting quantum circuits in a human-readable language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/yquant
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yquant.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yquant.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package allows to quickly draw quantum circuits. It bridges
the gap between the two groups of packages that already exist: those
that use a logic-oriented custom language, which is then translated into
TeX by means of an external program; and the pure TeX versions that
mainly provide some macros to allow for an easier input. yquant is a
pure-LaTeX solution -- i.e., it requires no external program -- that
introduces a logic oriented language and thus brings the best of both
worlds together. It builds on and interacts with TikZ, which brings an
enourmous flexibility for customization of individual circuits.

