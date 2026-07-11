%global tl_name venndiagram
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Creating Venn diagrams with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/venndiagram
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/venndiagram.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package assists generation of simple two- and three-set Venn
diagrams for lectures or assignment sheets. The package requires the
TikZ package.

