%define gitdate 20120324

Name: x11-driver-video-s3virge
Version: 1.10.4
Release: 8.%{gitdate}.1
Summary: X.org driver for S3 Virge Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3virge-%{gitdate}.tar.xz

BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(xorg-server)
BuildRequires: pkgconfig(xorg-macros)
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-s3virge is the X.org driver for S3 Virge Cards.

%prep
%setup -qn xf86-video-s3virge

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/s3virge_drv.so
%{_mandir}/man4/s3virge.*

