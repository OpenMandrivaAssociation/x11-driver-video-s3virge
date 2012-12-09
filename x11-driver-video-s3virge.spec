Name: x11-driver-video-s3virge
Version: 1.10.6
Release: 2
Summary: X.org driver for S3 Virge Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3virge-%{version}.tar.gz

BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(xorg-server)
BuildRequires: pkgconfig(xorg-macros)
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-s3virge is the X.org driver for S3 Virge Cards.

%prep
%setup -q -n xf86-video-s3virge-%{version}

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



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.10.6-1
+ Revision: 810702
- version update 1.10.6

* Mon May 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.10.5-1
+ Revision: 798707
- version update 1.10.5

* Thu Mar 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.10.4-8.20120324.1
+ Revision: 788201
- added new snapshot from git
- includes 30 commits since 2009-07-30
- Rebuild for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.10.4-7
+ Revision: 748454
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.4-6
+ Revision: 703713
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.10.4-5
+ Revision: 683584
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10.4-4
+ Revision: 671165
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.10.4-3mdv2011.0
+ Revision: 595726
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.10.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.10.4-1mdv2010.0
+ Revision: 407723
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.10.3-1mdv2010.0
+ Revision: 391901
- update to new version 1.10.3

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.10.2-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.10.2-1mdv2009.1
+ Revision: 317850
- New version 1.10.2

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 1.10.1-3mdv2009.1
+ Revision: 308174
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.10.1-2mdv2009.0
+ Revision: 265927
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.10.1-1mdv2009.0
+ Revision: 211783
- New version

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.10.0-1mdv2009.0
+ Revision: 194164
- Update to version 1.10.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.9.1-7mdv2008.1
+ Revision: 165590
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.9.1-6mdv2008.1
+ Revision: 156617
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.9.1-5mdv2008.1
+ Revision: 154821
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-s3virge-1.9.1@mandriva suggested on upstream
  Tag at git checkout e3833f9ae20f5bc25918a1f95216246711bbdf4e
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.9.1-4mdv2008.1
+ Revision: 99044
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.9.1-3mdv2008.0
+ Revision: 75785
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

