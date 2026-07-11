%global tl_name esstix
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	PostScript versions of the ESSTIX, with macro support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/esstix
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esstix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esstix.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These fonts represent translation to PostScript Type 1 of the ESSTIX
fonts. ESSTIX seem to have been a precursor to the STIX project, and
were donated by Elsevier to that project. The accompanying virtual fonts
with customized metrics and LaTeX support files allow their use as
calligraphic, fraktur and double-struck (blackboard bold) in maths mode.

