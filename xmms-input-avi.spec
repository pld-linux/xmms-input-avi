Summary:	avi/asf video playing plugin for xmms
Summary(pl):	Wtyczka odtwarzaj±ca filmy avi/asf dla xmms
Name:		xmms-input-avi
Version:	1.2.2
Release:	1
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	http://www.xmms.org/files/plugins/smpeg-xmms/smpeg-xmms-%{version}.tar.gz
Source0:	ftp://ftp.xmms.org/xmms/plugins/avi-xmms/avi-xmms-%{version}.tar.gz
Patch0:		avi-xmms-avifile.patch
Requires:	xmms
BuildRequires:	SDL-devel >= 1.1.6
BuildRequires:	libstdc++-devel
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	avifile-devel >= 0.6.0
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This plugin allows xmms to play avi/asf movies.

%description -l pl
Ta wtyczka pozwala xmms'owi odtwarzaæ filmy w formacie avi/asf.

%prep
%setup -q -n avi-xmms-%{version}
%patch0 -p1

%build
%configure 

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS TODO NEWS README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/Input/*.so
