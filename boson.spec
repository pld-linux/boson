Summary:	Boson : a Real-Time Strategy Game (RTS) for the KDE project
Name:		boson 
Version:	0.2
Release:	1
License:	GPL
Group:		X11/KDE/Games
Source0:	boson-%{version}.tgz
Source1:	boson-pics-%{version}.tgz
Icon:		boson.xpm
URL:		http://aquila.rezel.enst.fr/boson/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Boson is a real-time strategy game, like Command&Conquer(tm) or
StarCraft(tm). It is designed to run on Unix (Linux) computers and uses the
Qt Toolkit and QwSpriteField. A minimum of two players is required, since
there is no artifical intelligence (yet?). Boson is still in very early
development and not playable yet.

Boson's Code and Graphics are published under the GNU General Public License.

If you want to know more about Boson, have a look at the Web site.

%description
Boson jest gr� strategiczn� rozgrywan� w czsie rzeczywistym, tak jak
Command&Conquer czy StarCraft. Zosta� zaprojektowany dla maszyn uniksowych
(linuksowych); uzywa biblioteki Qt i QwSpriteField. Wymaga si� co najmniej
dw�ch graczy, poniewa� brak (jeszcze?) sztucznej inteligencji. Boson jest
wci�� w fazie wczesnego rozwoju i nie da si� jeszcze w niego gra�.
Kod i grafika Bosona s� na powszechnej licencji GNU.
Aby dowiedzie� si� wi�cej na temat Bosona, nale�y zajrze� na stron� WWW:
http://aquila.rezel.enst.fr/boson/.

%prep
%setup -q
%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
              --prefix=$KDEDIR \
              --libdir=%{buildroot}/$KDEDIR/lib \
 --with-install-root=%{buildroot}
make


%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT ; fi
make prefix=$RPM_BUILD_ROOT%{prefix} install

## install textures and resources files :
mkdir $RPM_BUILD_ROOT%{prefix}/share/apps/
cd $RPM_BUILD_ROOT%{prefix}/share/apps/
cp $RPM_SOURCE_DIR/boson-pics-%{version}.tgz . 
gunzip boson-pics-%{version}.tgz
tar xvf boson-pics-%{version}.tar
rm boson-pics-%{version}.tar

%clean
rm -rf %{builddir}
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
#rm -f $RPM_SOURCE_DIR/boson*

%files 
%{prefix}/bin/
%{prefix}/share/applnk/
%{prefix}/share/apps/
%{prefix}/share/icons/
%doc %{prefix}/share/doc/HTML/en/Boson/
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
