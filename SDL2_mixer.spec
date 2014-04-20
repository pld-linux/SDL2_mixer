#
# Conditional build:
%bcond_with	modplug	# use modplug for MOD support (mikmod is used by default)
#
Summary:	Simple DirectMedia Layer - Sample Mixer Library
Summary(pl.UTF-8):	Simple DirectMedia Layer - biblioteka miksująca próbki dźwiękowe
Summary(pt_BR.UTF-8):	SDL2 - Biblioteca para mixagem
Name:		SDL2_mixer
Version:	2.0.0
Release:	1
License:	Zlib-like
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_mixer/release/%{name}-%{version}.tar.gz
# Source0-md5:	65f6d80df073a1fb3bb537fbda031b50
URL:		http://www.libsdl.org/projects/SDL_mixer/
BuildRequires:	SDL2-devel >= 2.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.3.0
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libmikmod-devel >= 3.1.10
%{?with_modplug:BuildRequires:	libmodplug-devel >= 0.8.7}
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	smpeg-devel >= 0.4.4-11
Requires:	SDL2 >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Due to popular demand, here is a simple multi-channel audio mixer. It
supports 4 channels of 16 bit stereo audio, plus a single channel of
music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%description -l pl.UTF-8
SDL2_mixer to prosty wielokanałowy mikser audio. Obsługuje 4 kanały
16-bitowego dźwięku stereo plus jeden kanał dla muzyki miksowanej
przez popularne biblioteki MikMod MOD, Timitity MIDI i SMPEG MP3.

%description -l pt_BR.UTF-8
Biblioteca que suporta 4 canais de áudio estéreo 16 bit, mais um canal
de música, mixado pelo populares bibliotecas MOD MikMod, MIDI timidity
e SMPEG MP3.

%package devel
Summary:	Header files and more to develop SDL_mixer applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwoju aplikacji używających SDL_mixer
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SDL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL2-devel >= 2.0.0

%description devel
Header files and more to develop SDL2_mixer applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwoju aplikacji używających SDL2_mixer

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
SDL2.

%package static
Summary:	Static SDL2_mixer library
Summary(pl.UTF-8):	Statyczna biblioteka SDL2_mixer
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com SDL2_mixer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL2_mixer library.

%description static -l pl.UTF-8
Statyczna biblioteka SDL2_mixer.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com SDL2_mixer.

%prep
%setup -q

%build
#%{__libtoolize}
%{__aclocal} -I acinclude
%{__autoconf}
%configure \
	--enable-music-midi-fluidsynth \
	%{?with_modplug:--enable-music-mod-modplug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-bin \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/%{_bindir}/playmus $RPM_BUILD_ROOT/%{_bindir}/playmus2
mv $RPM_BUILD_ROOT/%{_bindir}/playwave $RPM_BUILD_ROOT/%{_bindir}/playwave2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.txt COPYING.txt README.txt
%attr(755,root,root) %{_bindir}/playmus2
%attr(755,root,root) %{_bindir}/playwave2
%attr(755,root,root) %{_libdir}/libSDL2_mixer-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL2_mixer-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL2_mixer.so
%{_libdir}/libSDL2_mixer.la
%{_includedir}/SDL2/SDL_mixer.h
%{_pkgconfigdir}/SDL2_mixer.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL2_mixer.a
