Summary:	NPAPI plugin for libvlc
Summary(pl.UTF-8):	Wtyczka NPAPI do libvlc
Name:		browser-plugin-vlc
Version:	2.1.3
Release:	1
License:	GPL v2+
Group:		Applications/Networking
#Source0:	http://download.videolan.org/pub/videolan/vlc-webplugins/%{version}/npapi-vlc-%{version}.tar.xz
Source0:	npapi-vlc-%{version}.tar.xz
# Source0-md5:	f43be0bb87fa2f5d1e48a8840e6afba0
URL:		http://git.videolan.org/?p=npapi-vlc.git;a=summary
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vlc-devel >= 2.1.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xulrunner-devel >= 1.9.2
BuildRequires:	xz
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Obsoletes:	npapi-vlc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NPAPI plugin for libvlc.

%description -l pl.UTF-8
Wtyczka NPAPI do libvlc.

%prep
%setup -q -n npapi-vlc-%{version}

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
