Summary:	Boson: a Real-Time Strategy Game (RTS) for the KDE project
Summary(pl):	Boson: gra strategiczna w czasie rzeczywistym dla KDE
Name:		boson
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Aplikacje/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/boson/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.sourceforge.net/pub/sourceforge/boson/%{name}-pics-%{version}.tgz
Icon:		boson.xpm
URL:		http://boson.sourceforge.net/
BuildRequires:	kdelibs-devel
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
%setup -q

%build
kde_icondir=%{_pixmapsdir}; export kde_icondir
kde_htmldir=%{_htmldir}; export kde_htmldir
%configure2_13 \
	--with-install-root=%{buildroot}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

## install textures and resources files :
install -d $RPM_BUILD_ROOT%{_datadir}/apps
tar xzf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/apps

gzip -9nf AUTHORS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/*
%{_datadir}/apps/*
%{_pixmapsdir}/*
%doc %{_htmldir}/en/Boson
