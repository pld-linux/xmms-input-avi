Summary:	avi/asf video playing plugin for XMMS
Summary(pl):	Wtyczka odtwarzaj±ca filmy avi/asf dla XMMS
Name:		xmms-input-avi
Version:	1.2.2
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.xmms.org/xmms/plugins/avi-xmms/avi-xmms-%{version}.tar.gz
Patch0:		avi-xmms-avifile.patch
Patch1:		avi-xmms-thread.patch
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
%define		_mandir		%{_prefix}/man

%description
This plugin allows XMMS to play avi/asf movies.

%description -l pl
Ta wtyczka pozwala XMMS-owi odtwarzaæ filmy w formacie avi/asf.

%prep
%setup -q -n avi-xmms-%{version}
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure

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
