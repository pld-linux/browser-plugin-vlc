%define	snap	20131028
Summary:	NPAPI plugin for libvlc
Name:		npapi-vlc
Version:	2.1.0
Release:	0.%{snap}.1
License:	LGPL v2+
Group:		Applications/Networking
URL:		http://git.videolan.org/?p=npapi-vlc.git;a=summary
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	beb2922f9c18b5f531f26cfb441741f0
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	vlc-devel >= 2.1.0
BuildRequires:	xulrunner-devel
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Obsoletes:	browser-plugin-vlc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NPAPI plugin for libvlc.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	npvlcdir=%{_browserpluginsdir} \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_browserpluginsdir}/libvlcplugin.la

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
%doc AUTHORS ChangeLog COPYING NEWS
%attr(755,root,root) %{_browserpluginsdir}/libvlcplugin.so
