# revision 22426
# category Package
# catalog-ctan /fonts/esstix
# catalog-date 2011-05-10 11:05:00 +0200
# catalog-license ofl
# catalog-version 1.0
Name:		texlive-esstix
Version:	1.0
Release:	2
Summary:	PostScript versions of the ESSTIX, with macro support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/esstix
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esstix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esstix.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These fonts represent translation to PostScript Type 1 of the
ESSTIX fonts. ESSTIX seem to have been a precursor to the STIX
project, and were donated by Elsevier to that project. The
accompanying virtual fonts with customized metrics and LaTeX
support files allow their use as calligraphic, fraktur and
double-struck (blackboard bold) in maths mode.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX10.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX10.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX11.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX11.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX12.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX12.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX13.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX13.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX14.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX14.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX15.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX15.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX16.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX16.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX17.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX17.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX1_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX1_.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX2_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX2_.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX3_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX3_.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX4_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX4_.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX5_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX5_.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX6_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX6_.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX7_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX7_.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX8_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX8_.afm
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX9_.PFM
%{_texmfdistdir}/fonts/afm/esstix/ESSTIX9_.afm
%{_texmfdistdir}/fonts/map/dvips/esstix/ESSTIX.map
%{_texmfdistdir}/fonts/tfm/public/esstix/esstixbb.tfm
%{_texmfdistdir}/fonts/tfm/public/esstix/esstixcal.tfm
%{_texmfdistdir}/fonts/tfm/public/esstix/esstixfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/esstix/rESSTIX13.tfm
%{_texmfdistdir}/fonts/tfm/public/esstix/rESSTIX14.tfm
%{_texmfdistdir}/fonts/tfm/public/esstix/rESSTIX15.tfm
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX10.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX11.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX12.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX13.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX14.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX15.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX16.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX17.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX1_.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX2_.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX3_.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX4_.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX5_.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX6_.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX7_.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX8_.pfb
%{_texmfdistdir}/fonts/type1/public/esstix/ESSTIX9_.pfb
%{_texmfdistdir}/fonts/vf/public/esstix/esstixbb.vf
%{_texmfdistdir}/fonts/vf/public/esstix/esstixcal.vf
%{_texmfdistdir}/fonts/vf/public/esstix/esstixfrak.vf
%{_texmfdistdir}/tex/latex/esstix/esstixbb.sty
%{_texmfdistdir}/tex/latex/esstix/esstixcal.sty
%{_texmfdistdir}/tex/latex/esstix/esstixfrak.sty
%{_texmfdistdir}/tex/latex/esstix/uesstixbb.fd
%{_texmfdistdir}/tex/latex/esstix/uesstixcal.fd
%{_texmfdistdir}/tex/latex/esstix/uesstixfrak.fd
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX10.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX11.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX12.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX13.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX14.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX15.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX16.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX17.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX1_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX2_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX3_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX4_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX5_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX6_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX7_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX8_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/ESSTIX9_.tfm
%doc %{_texmfdistdir}/doc/fonts/esstix/Esstix.pdf
%doc %{_texmfdistdir}/doc/fonts/esstix/Esstix.tex
%doc %{_texmfdistdir}/doc/fonts/esstix/README
%doc %{_texmfdistdir}/doc/fonts/esstix/esstixOther.map

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
