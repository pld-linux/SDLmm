Summary:	C++ glue to SDL (Simple DirectMedia Layer)
Summary(pl):	Interfejs C++ do SDL
Name:		SDLmm
Version:	0.1.8
Release:	4
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/sdlmm/%{name}-%{version}.tar.bz2
# Source0-md5:	0a05d27d1aed72af3c7a37b6378f50e5
URL:		http://sdlmm.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a C++ glue to SDL (Simple DirectMedia Layer) library- a
low-level, cross-platform multimedia library. SDLmm will utilize C++
features while still being close to SDL in syntax (and naming).

%description -l pl
Jest to ³±cznik miêdzy C++ a SDL (Simple DirectMedia Layer),
niskopoziomow± bibliotek± multimedialn±. SDLmm wykorzysta cechy C++
wci±¿ bêd±c w sk³adni (i w nazewnictwie) blisko SDL.

%package devel
Summary:	Header files and more to develop SDLmm applications
Summary(pl):	Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDLmm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDLmm applications.

%description devel -l pl
Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDLmm.

%package static
Summary:	Static SDLmm libraries
Summary(pl):	Statyczne biblioteki SDLmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_image libraries.

%description static -l pl
Statyczne biblioteki SDL_image.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS AUTHORS
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
