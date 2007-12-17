Name: x11-driver-video-s3virge
Version: 1.9.1
Release: %mkrel 5
Summary: The X.org driver for S3 Virge Cards
Group: Development/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-s3virge  xorg/drivers/xf86-video-s3virge
# cd xorg/drivers/xf86-video/s3virge
# git-archive --format=tar --prefix=xf86-video-s3virge-1.1.0/ master | bzip2 -9 > xf86-video-s3virge-1.1.0.tar.bz2
########################################################################
Source0: xf86-video-s3virge-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

########################################################################
# git-format-patch master..origin/mandriva+gpl
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
