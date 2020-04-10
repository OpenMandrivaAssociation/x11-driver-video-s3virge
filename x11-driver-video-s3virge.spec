%define _disable_ld_no_undefined 1

Summary:	X.org driver for S3 Virge Cards
Name:		x11-driver-video-s3virge
Version:	1.11.0
Release:	1
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3virge-%{version}.tar.gz
Patch0:		s3virge-1.11.0-compile.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-s3virge is the X.org driver for S3 Virge Cards.

%prep
%autosetup -p1 -n xf86-video-s3virge-%{version}

%build
%configure
%make

%install
%make_install

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/s3virge_drv.so
%{_mandir}/man4/s3virge.*

