Summary:	C++ glue to SDL (Simple DirectMedia Layer)
Summary(pl):	Interfejs C++ do SDL
Name:		SDLmm
Version:	0.1.8
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/sdlmm/%{name}-%{version}.tar.bz2
URL:		http://sdlmm.sourceforge.net/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is a C++ glue to SDL (Simple DirectMedia Layer) library- a
low-level, cross-platform multimedia library. SDLmm will utilize C++
features while still being close to SDL in syntax (and naming).

%description -l pl
Jest to ≥±cznik miÍdzy C++ a SDL (Simple DirectMedia Layer),
niskopoziomow± bibliotek± multimedialn±. SDLmm wykoøysta cechy C++
wci±ø bÍd±c w sk≥adni (i w nazewnictwie) blisko SDL.

%package devel
Summary:	Header files and more to develop SDLmm applications
Summary(pl):	Pliki nag≥Ûwkowe do rozwijania aplikacji uøywaj±cych SDLmm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDLmm applications.

%description -l pl devel
Pliki nag≥Ûwkowe do rozwijania aplikacji uøywaj±cych SDLmm.

%package static
Summary:	Static SDLmm libraries
Summary(pl):	Statyczne biblioteki SDLmm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_image libraries.

%description -l pl static
Statyczne biblioteki SDL_image.

%prep
%setup -q 

%build
aclocal
automake -a
autoconf
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README THANKS AUTHORS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/html/*.html docs/html/*.gif docs/html/*.css
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/SDLmm/*
%{_aclocaldir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
