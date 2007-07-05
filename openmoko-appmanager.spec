#
Summary:	OpenMoko appplication manager applet
Name:		openmoko-appmanager
Version:	0.0.0.2360
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	e69521f65edcd27aa71005bfa3d97a0b
URL:		http://openmoko.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libmatchbox-devel >= 1.8
BuildRequires:	openmoko-libs-devel
Requires:	openmoko-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define openmokoname %(echo %{name} | sed -e 's/openmoko-//')

%description
OpenMoko appplication manager applet

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
