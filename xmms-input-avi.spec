Summary:	avi/asf video playing plugin for XMMS
Summary(pl):	Wtyczka odtwarzaj±ca filmy avi/asf dla XMMS
Name:		xmms-input-avi
Version:	1.2.3
Release:	0.9
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.xmms.org/xmms/plugins/avi-xmms/avi-xmms-%{version}.tar.gz
Patch0:		avi-xmms-avifile.patch
Patch2:		avi-xmms-am.patch
URL:		http://www.xmms.org/plugins_input.html#122
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel >= 0.6
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
The AVI player is a plug-in for XMMS, giving it the ability to play Windows AVI
(including DivX ;-)) and ASF files on your Linux or FreeBSD box. You can simply
add movies to your playlist and the plug-in will call aviplay to play the movie
files. Many aviplay options are supported, such as fullscreen playback and true
hardware acceleration on XFree86 4.x.x.
It plays .wma files too.

%prep
%setup -q -n avi-xmms-%{version}
#%patch0 -p1
#%patch2 -p1

%build
#rm -f missing
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__automake}
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/xmms/Input/*.so
