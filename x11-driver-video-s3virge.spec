%define _disable_ld_no_undefined 1

Summary:	X.org driver for S3 Virge Cards
Name:		x11-driver-video-s3virge
Version:	1.10.6
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3virge-%{version}.tar.gz

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-s3virge is the X.org driver for S3 Virge Cards.

%prep
%setup -qn xf86-video-s3virge-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/s3virge_drv.so
%{_mandir}/man4/s3virge.*

