Summary:	Boson: a Real-Time Strategy Game (RTS) for the KDE project
Summary(pl):	Boson: gra strategiczna w czasie rzeczywistym dla KDE
Name:		boson
Version:	0.10
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/boson/%{name}-all-%{version}.tar.bz2
# Source0-md5:	e54b1a3f1f140412597d4df296522bde
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-python.patch
Icon:		boson.xpm
URL:		http://boson.sourceforge.net/
BuildRequires:	arts-devel
BuildRequires:	kdegames-devel >= 3.0.3
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	lib3ds-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	arts-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boson is a real-time strategy game, like Command&Conquer(tm) or
StarCraft(tm). It is designed to run on Unix (Linux) computers and
uses the Qt Toolkit and QwSpriteField. A minimum of two players is
required, since there is no artificial intelligence (yet?). Boson is
still in very early development and not playable yet.

%description -l pl
Boson jest gr± strategiczn± rozgrywan± w czasie rzeczywistym, tak jak
Command&Conquer czy StarCraft. Zosta³ zaprojektowany dla maszyn
uniksowych (linuksowych); u¿ywa biblioteki Qt i QwSpriteField. Wymaga
siê co najmniej dwóch graczy, poniewa¿ brak (jeszcze?) sztucznej
inteligencji. Boson jest wci±¿ w fazie wczesnego rozwoju i nie da siê
jeszcze w niego graæ.

%prep
%setup -q -n %{name}-all-%{version}
%patch0	-p1
%patch1 -p1

%build
kde_htmldir=%{_kdedocdir}; export kde_htmldir
%configure \
	--disable-rpath \
	--with-xinerama

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Games/TacticStrategy/boson \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/boson
%{_desktopdir}/*.desktop
%{_datadir}/config/*
%{_iconsdir}/hicolor/*/*/*
%dir %{_libdir}/kde3/plugins/boson
%attr(755,root,root) %{_libdir}/kde3/plugins/boson/*.so*
%{_libdir}/kde3/plugins/boson/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/*.so
%{_libdir}/kde3/plugins/designer/*.la
