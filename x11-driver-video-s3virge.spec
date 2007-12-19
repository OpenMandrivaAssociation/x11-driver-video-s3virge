Name: x11-driver-video-s3virge
Version: 1.9.1
Release: %mkrel 5
Summary: The X.org driver for S3 Virge Cards
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-s3virge-1.9.1@mandriva suggested on upstream
# Tag at git checkout e3833f9ae20f5bc25918a1f95216246711bbdf4e
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-s3virge  xorg/drivers/xf86-video-s3virge
# cd xorg/drivers/xf86-video/s3virge
# git-archive --format=tar --prefix=xf86-video-s3virge-1.9.1/ xf86-video-s3virge-1.9.1@mandriva | bzip2 -9 > xf86-video-s3virge-1.9.1.tar.bz2
########################################################################
Source0: xf86-video-s3virge-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-s3virge-1.9.1@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0
%description
The X.org driver for S3 Virge Cards

%prep
%setup -q -n xf86-video-s3virge-%{version}

%patch1 -p1

%build
autoreconf -ifs
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
