Summary:	C++ glue to SDL (Simple DirectMedia Layer)
Summary(pl):	Interfejs C++ do SDL
Name:		SDLmm
Version:	0.1.8
Release:	6
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/sdlmm/%{name}-%{version}.tar.bz2
# Source0-md5:	0a05d27d1aed72af3c7a37b6378f50e5
Patch0:		%{name}-am18.patch
URL:		http://sdlmm.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
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
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel
Requires:	libstdc++-devel

%description devel
Header files and more to develop SDLmm applications.

%description devel -l pl
Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDLmm.

%package static
Summary:	Static SDLmm libraries
Summary(pl):	Statyczne biblioteki SDLmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Statis SDL_image libraries.

%description static -l pl
Statyczne biblioteki SDL_image.

%prep
%setup -q
%patch0 -p1

# kill sinclude and copy of libtool.m4
tail -n +3 acinclude.m4 | head -n 176 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CXXFLAGS="-I`pwd`/src -pipe %{rpmcflags} -Woverloaded-virtual -fno-exceptions -fno-rtti -W -Wall -Wno-unused -Wcast-align -I/usr/include/SDL -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/html/*.html docs/html/*.gif docs/html/*.css
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDLmm
%{_aclocaldir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
