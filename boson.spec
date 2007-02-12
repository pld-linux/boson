#
# TODO:
# - fix icon installation (probably somewhere in KDE3Macros.cmake)
#
Summary:	Boson: a Real-Time Strategy Game (RTS) for the KDE project
Summary(pl.UTF-8):	Boson: gra strategiczna w czasie rzeczywistym dla KDE
Name:		boson
Version:	0.13
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/boson/%{name}-all-%{version}.tar.bz2
# Source0-md5:	1b91bbdda1ff81d4d60f80c8175d974b
Patch0:		%{name}-ugly_install_workround.patch
URL:		http://boson.sourceforge.net/
BuildRequires:	arts-devel
BuildRequires:	cmake >= 2.4.0
BuildRequires:	kdegames-devel >= 8:3.2
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	lib3ds-devel
BuildRequires:	rpmbuild(macros) >= 1.293
Requires:	arts-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boson is a real-time strategy game, like Command&Conquer(tm) or
StarCraft(tm). It is designed to run on Unix (Linux) computers and
uses the Qt Toolkit and QwSpriteField. A minimum of two players is
required, since there is no artificial intelligence (yet?). Boson is
still in very early development and not playable yet.

%description -l pl.UTF-8
Boson jest grą strategiczną rozgrywaną w czasie rzeczywistym, tak jak
Command&Conquer czy StarCraft. Został zaprojektowany dla maszyn
uniksowych (linuksowych); używa biblioteki Qt i QwSpriteField. Wymaga
się co najmniej dwóch graczy, ponieważ brak (jeszcze?) sztucznej
inteligencji. Boson jest wciąż w fazie wczesnego rozwoju i nie da się
jeszcze w niego grać.

%prep
%setup -q -c
%patch0 -p1

%build
%cmake \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	%{name}-all-%{version}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{32x32,48x48}/apps
install %{name}-all-%{version}/code/boson/data/hi32-app-boeditor.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/boeditor.png
install %{name}-all-%{version}/code/boson/data/hi32-app-boson.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/boson.png
install %{name}-all-%{version}/code/boson/data/hi48-app-boeditor.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/boeditor.png
install %{name}-all-%{version}/code/boson/data/hi48-app-boson.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/boson.png
mv -f boson-all-0.13/data/{AUTHORS,ChangeLog,README} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/boson
%{_desktopdir}/*.desktop
%{_datadir}/config/*
%{_iconsdir}/hicolor/*/*/*
%dir %{_libdir}/kde3/plugins/boson
%attr(755,root,root) %{_libdir}/kde3/plugins/boson/*.so*
