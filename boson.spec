#
# Spec file for package Boson
#
# Please send bugfixes or comments to the packager
#


#
# Thomas : Every packager should change only those four lines
#

# THe number of your attempt to build the rpm
%define release          1
# The name of your distribution : ex "SuSe Linux 6.0 (i386)", or "RedHat 5.1 (alpha)"
%define distro           LinuxPPC R5/Q3
# THe place where kde is installed in your distro (probably /opt/kde/)
%define prefix           /usr
# Your name
%define packager         Thomas Capricelli <capricel@enst.fr>

#
# Thomas : shouldn't be altered after this line
#

%define version          0.2

# Directory-related Tags
%define builddir         $RPM_BUILD_DIR/boson-%{version}
BuildRoot:               /var/tmp/boson-%{version}-root
Prefix:                  %{prefix}

# Package Naming Tags
Name:                    boson 
Version:                 %{version}
Release:                 %{release}
Distribution:            %{distro}
Packager:                %{packager}
Group:                   X11/KDE/Games

# 
Icon:                    boson.xpm
Source0:                 boson-%{version}.tgz
Source1:                 boson-pics-%{version}.tgz

# Dependancy Tags
Provides:                boson
Serial:                  %{release}
AutoReqProv:             Yes

# Descriptive Tags
Summary:                 Boson : a Real-Time Strategy Game (RTS) for the KDE project
Vendor:                  Thomas Capricelli <capricel@enst.fr>, Benjamin Adler <BenAdler@gmx.net>
Copyright:               GPL
URL:                     http://aquila.rezel.enst.fr/boson/

%description
Boson is a real-time strategy game, like Command&Conquer(tm) or StarCraft(tm).
It is designed to run on Unix (Linux) computers and uses the Qt
Toolkit and QwSpriteField. A minimum of two players is required, since there is
no artifical intelligence (yet?). Boson is still in very early development
and not playable yet. 

Boson's Code and Graphics are published under the GNU General Public License.

If you want to know more about Boson, have a look at the Web site.

%prep
%setup -n boson-%{version}
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

%changelog
* Tue Sep 21 1999 Thomas Capricelli <capricel@enst.fr>
-  making it the way I want it..
-  adapted to boson-0.2 (Games/Boson)
* Thu Sep 17 1999 Guillaume Assire <alphagolf@rocketmail.com>
-  Initial packaging version 0.1
