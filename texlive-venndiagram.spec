# revision 28069
# category Package
# catalog-ctan /macros/latex/contrib/venndiagram
# catalog-date 2012-10-24 15:36:13 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-venndiagram
Version:	1.0
Release:	6
Summary:	Creating Venn diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/venndiagram
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package assists generation of simple two- and three-set
Venn diagrams for lectures or assignment sheets. The package
requires the TikZ package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/venndiagram/venndiagram.sty
%doc %{_texmfdistdir}/doc/latex/venndiagram/CHANGES
%doc %{_texmfdistdir}/doc/latex/venndiagram/INSTALL
%doc %{_texmfdistdir}/doc/latex/venndiagram/README
%doc %{_texmfdistdir}/doc/latex/venndiagram/samples/venn-sample.pdf
%doc %{_texmfdistdir}/doc/latex/venndiagram/samples/venn-sample.tex
%doc %{_texmfdistdir}/doc/latex/venndiagram/venndiagram.pdf
#- source
%doc %{_texmfdistdir}/source/latex/venndiagram/venndiagram.dtx
%doc %{_texmfdistdir}/source/latex/venndiagram/venndiagram.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
