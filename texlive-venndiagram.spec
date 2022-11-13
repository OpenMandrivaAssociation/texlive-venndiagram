Name:		texlive-venndiagram
Version:	47952
Release:	1
Summary:	Creating Venn diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/venndiagram
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/venndiagram
%doc %{_texmfdistdir}/doc/latex/venndiagram
#- source
%doc %{_texmfdistdir}/source/latex/venndiagram

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
