Name: x11-driver-video-s3virge
Version: 1.10.2
Release: %mkrel 2
Summary: X.org driver for S3 Virge Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3virge-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-s3virge is the X.org driver for S3 Virge Cards.

%prep
%setup -q -n xf86-video-s3virge-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/s3virge_drv.la
%{_libdir}/xorg/modules/drivers/s3virge_drv.so
%{_mandir}/man4/s3virge.*
