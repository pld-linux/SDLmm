Summary:	C++ glue to SDL (Simple DirectMedia Layer)
Summary(pl):	Interfejs C++ do SDL
Name:		SDLmm
Version:	0.1.8
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/sdlmm/%{name}-%{version}.tar.bz2
URL:		http://sdlmm.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is a C++ glue to SDL (Simple DirectMedia Layer) library- a
low-level, cross-platform multimedia library. SDLmm will utilize C++
features while still being close to SDL in syntax (and naming).

%description -l pl
Jest to ≥±cznik miÍdzy C++ a SDL (Simple DirectMedia Layer),
niskopoziomow± bibliotek± multimedialn±. SDLmm wykorzysta cechy C++
wci±ø bÍd±c w sk≥adni (i w nazewnictwie) blisko SDL.

%package devel
Summary:	Header files and more to develop SDLmm applications
Summary(pl):	Pliki nag≥Ûwkowe do rozwijania aplikacji uøywaj±cych SDLmm
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDLmm applications.

%description -l pl devel
Pliki nag≥Ûwkowe do rozwijania aplikacji uøywaj±cych SDLmm.

%package static
Summary:	Static SDLmm libraries
Summary(pl):	Statyczne biblioteki SDLmm
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_image libraries.

%description -l pl static
Statyczne biblioteki SDL_image.

%prep
%setup -q 

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

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
%{_includedir}/SDLmm
%{_aclocaldir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
