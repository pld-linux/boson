Summary:	Boson: a Real-Time Strategy Game (RTS) for the KDE project
Summary(pl):	Boson: gra strategiczna w czasie rzeczywistym dla KDE
Name:		boson
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://telia.dl.sourceforge.net/sourceforge/boson/%{name}-all-%{version}.tar.bz2
Icon:		boson.xpm
URL:		http://boson.sourceforge.net/
BuildRequires:	arts-devel
BuildRequires:	kdegames-devel >= 3.0.3
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	%{_docdir}/kde/HTML

%description
Boson is a real-time strategy game, like Command&Conquer(tm) or
StarCraft(tm). It is designed to run on Unix (Linux) computers and
uses the Qt Toolkit and QwSpriteField. A minimum of two players is
required, since there is no artifical intelligence (yet?). Boson is
still in very early development and not playable yet.

Boson's Code and Graphics are published under the GNU General Public
License.

If you want to know more about Boson, have a look at the Web site.

%description -l pl
Boson jest gr± strategiczn± rozgrywan± w czasie rzeczywistym, tak jak
Command&Conquer czy StarCraft. Zosta³ zaprojektowany dla maszyn
uniksowych (linuksowych); uzywa biblioteki Qt i QwSpriteField. Wymaga
siê co najmniej dwóch graczy, poniewa¿ brak (jeszcze?) sztucznej
inteligencji. Boson jest wci±¿ w fazie wczesnego rozwoju i nie da siê
jeszcze w niego graæ. Kod i grafika Bosona s± na powszechnej licencji
GNU. Aby dowiedzieæ siê wiêcej na temat Bosona, nale¿y zajrzeæ na
stronê WWW: http://aquila.rezel.enst.fr/boson/.

%prep
%setup -q -n %{name}

%build
kde_icondir=%{_pixmapsdir}; export kde_icondir
kde_htmldir=%{_htmldir}; export kde_htmldir
%configure \
	--with-install-root=%{buildroot}
	
# %{__make} Fails becuse after including many QT headers gcc is unable to find <map> :/
mv map map.foo
cd boson
%{__make}
cd ..
mv map.foo map
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

## install textures and resources files :
#install -d $RPM_BUILD_ROOT%{_datadir}/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_htmldir}/en/boson
%{_applnkdir}/Games/TacticStrategy/*.desktop
%{_datadir}/apps/boson/bosonui.rc
%{_datadir}/apps/boson/themes
%{_datadir}/apps/boson/map
%{_datadir}/apps/boson/music/*/*
%{_datadir}/apps/boson/pics/*.png
%{_pixmapsdir}/*/*/apps/boson.png
