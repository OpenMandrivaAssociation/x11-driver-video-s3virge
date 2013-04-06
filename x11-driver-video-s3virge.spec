%define _disable_ld_no_undefined 1

Summary:	X.org driver for S3 Virge Cards
Name:		x11-driver-video-s3virge
Version:	1.10.6
Release:	5
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3virge-%{version}.tar.gz
Patch0:		xf86-video-s3virge-1.10.6-remove-miInitializeBackingStore.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-s3virge is the X.org driver for S3 Virge Cards.

%prep
%setup -qn xf86-video-s3virge-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/s3virge_drv.so
%{_mandir}/man4/s3virge.*

