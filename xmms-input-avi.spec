Summary:	avi/asf video playing plugin for XMMS
Summary(pl):	Wtyczka odtwarzaj±ca filmy avi/asf dla XMMS
Name:		xmms-input-avi
Version:	1.2.3
Release:	0.10
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.xmms.org/xmms/plugins/avi-xmms/avi-xmms-%{version}.tar.gz
# Source0-md5:	1eb3ce58d21ec00b38d7786363ff271c
Patch0:		avi-xmms-avifile.patch
Patch2:		avi-xmms-am.patch
URL:		http://www.xmms.org/plugins_input.html#122
BuildRequires:	SDL-devel >= 1.2.0
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	avifile-devel >= 0.6
BuildRequires:	libstdc++-devel
#BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AVI player is a plug-in for XMMS, giving it the ability to play
Windows AVI (including DivX ;-)), ASF and WMA files on your Linux or
FreeBSD box. You can simply add movies to your playlist and the
plug-in will call aviplay to play the movie files. Many aviplay
options are supported, such as fullscreen playback and true hardware
acceleration on XFree86 4.x.x.

%description -l pl
AVI player to wtyczka dla XMMS daj±ca mo¿liwo¶æ odtwarzania plików AVI
(w³±cznie z DivX ;-)), ASF i WMA z Windows pod Linuksem i FreeBSD.
Mo¿na ³atwo dodawaæ filmy do listy, a wtyczka uruchomi aviplay, aby
odtworzy³ te pliki. Obs³ugiwanych jest wiele opcji aviplaya, takich
jak fullscreen i akceleracja sprzêtowa pod XFree86 4.x.x.

%prep
%setup -q -n avi-xmms-%{version}
#%patch0 -p1
#%patch2 -p1

%build
#rm -f missing
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__automake}
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO NEWS README ChangeLog
%attr(755,root,root) %{xmms_input_plugindir}/*.so
