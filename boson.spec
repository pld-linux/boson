Summary:	Boson: a Real-Time Strategy Game (RTS) for the KDE project
Summary(pl):	Boson: gra strategiczna w czasie rzeczywistym dla KDE
Name:		boson
Version:	0.6.1
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://telia.dl.sourceforge.net/sourceforge/boson/%{name}-all-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
Icon:		boson.xpm
URL:		http://boson.sourceforge.net/
BuildRequires:	arts-devel
BuildRequires:	kdegames-devel >= 3.0.3
BuildRequires:	kdelibs-devel >= 3.0.3
Requires:	arts-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
Boson is a real-time strategy game, like Command&Conquer(tm) or
StarCraft(tm). It is designed to run on Unix (Linux) computers and
uses the Qt Toolkit and QwSpriteField. A minimum of two players is
required, since there is no artifical intelligence (yet?). Boson is
still in very early development and not playable yet.

%description -l pl
Boson jest gr± strategiczn± rozgrywan± w czasie rzeczywistym, tak jak
Command&Conquer czy StarCraft. Zosta³ zaprojektowany dla maszyn
uniksowych (linuksowych); uzywa biblioteki Qt i QwSpriteField. Wymaga
siê co najmniej dwóch graczy, poniewa¿ brak (jeszcze?) sztucznej
inteligencji. Boson jest wci±¿ w fazie wczesnego rozwoju i nie da siê
jeszcze w niego graæ.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
kde_icondir=%{_pixmapsdir}; export kde_icondir
kde_htmldir=%{_htmldir}; export kde_htmldir
%configure \
	--disable-rpath \
	--enable-final
	
# %{__make} Fails becuse after including many QT headers gcc is unable to find <map> :/
mv map map.foo
cd boson
%{__make}
cd ..
mv map.foo map
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

## install textures and resources files :
#install -d $RPM_BUILD_ROOT%{_datadir}/apps

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Games/{TacticStrategy,Strategy}
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/{hicolor/48x48/apps/,}boson.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/Strategy/*.desktop
%{_datadir}/apps/boson
%{_pixmapsdir}/boson.png
