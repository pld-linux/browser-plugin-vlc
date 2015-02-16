# TODO: rename to browser-plugin-vlc?
%define	snap	20131028
Summary:	NPAPI plugin for libvlc
Summary(pl.UTF-8):	Wtyczka NPAPI do libvlc
Name:		npapi-vlc
Version:	2.1.0
Release:	0.%{snap}.1
License:	GPL v2+
Group:		Applications/Networking
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	beb2922f9c18b5f531f26cfb441741f0
URL:		http://git.videolan.org/?p=npapi-vlc.git;a=summary
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	vlc-devel >= 2.1.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xulrunner-devel >= 1.9.2
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Obsoletes:	browser-plugin-vlc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NPAPI plugin for libvlc.

%description -l pl.UTF-8
Wtyczka NPAPI do libvlc.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-mozilla-pkg=mozilla-plugin
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	npvlcdir=%{_browserpluginsdir} \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_browserpluginsdir}/libvlcplugin.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins

%postun
if [ "$1" = 0 ]; then
        %update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_browserpluginsdir}/libvlcplugin.so
