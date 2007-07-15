Summary:	OpenMoko application manager applet
Summary(pl.UTF-8):	Aplet zarządcy aplikacji dla OpenMoko
Name:		openmoko-appmanager
Version:	0.0.0.2360
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	e69521f65edcd27aa71005bfa3d97a0b
URL:		http://openmoko.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
# TODO
BuildRequires:	libipkg-devel
BuildRequires:	libtool
BuildRequires:	openmoko-libs-devel >= 0.0.1
BuildRequires:	pkgconfig
Requires:	openmoko-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenMoko application (ipk packages) manager applet.

%description -l pl.UTF-8
Aplet zarządcy aplikacji (pakietów ipk) dla OpenMoko.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/openmoko-appmanager
%{_datadir}/openmoko-appmanager
%{_desktopdir}/openoko-appmanager.desktop
%{_pixmapsdir}/application-manager.png
