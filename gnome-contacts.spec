Summary:	Contacts manager for GNOME
Name:		gnome-contacts
Version:	3.14.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-contacts/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	e54eccf46739b075e6b1b0ffbd4f6262
URL:		https://live.gnome.org/ThreePointOne/Features/Contacts
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cheese-devel >= 3.14.0
BuildRequires:	folks-devel >= 0.10.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 3.14.0
BuildRequires:	gnome-online-accounts-devel >= 3.14.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	intltool
BuildRequires:	libgee-devel >= 0.16.0
BuildRequires:	libnotify-devel >= 0.7.6
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	telepathy-glib-devel
Requires(post,postun):	glib-gio-gsettings
Requires:	evolution-data-server >= 3.12.0
Requires:	folks
Requires:	gnome-online-accounts >= 3.14.0
Requires:	telepathy-mission-control
Suggests:	cheese >= 3.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnome-contacts

%description
gnome-contacts is a standalone contacts manager for GNOME desktop.

%package shell-search-provider
Summary:	GNOME Shell search provider
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-shell

%description shell-search-provider
Search result provider for GNOME Shell.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4 -I libgd
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS ChangeLog
%attr(755,root,root) %{_bindir}/gnome-contacts
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_desktopdir}/org.gnome.Contacts.desktop

%files shell-search-provider
%defattr(644,root,root,755)
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini

