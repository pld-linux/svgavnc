Summary:	VNC viewer for svgalib
Summary(pl):	Klient VNC dla svgalib
Name:		svgavnc
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://republika.pl/rkd/%{name}-%{version}.tar.bz2
# Source0-md5:	c444151d587fe368f6ad55b5e8cae2a9
BuildRequires:	libjpeg-devel
BuildRequires:	svgalib-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-imake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVGALIB version of vncviewer using tight extensions.

%description -l pl
Klient VNC dla SVGALIB dla protoko³u 3.3.7t.

%prep
%setup -q

%build
xmkmf -a
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install svgavnc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.old
%attr(755,root,root) %{_bindir}/*
