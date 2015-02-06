%define name monotone-viz
%define version 1.0.1
%define release 4

Summary: A small GTK+ application that visualizes monotone ancestry graphs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-nolablgtk.tar.gz
Patch0:         monotone-viz-1.0.1-gio.patch
License: GPL
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://oandrieu.nerim.net/monotone-viz/
BuildRequires: ocaml ocaml-lablgtk2-devel camlp4 libgnomecanvas2-devel monotone
Requires: monotone graphviz

%description
Monotone-viz is a small GTK+ application that visualizes monotone ancestry
graphs. Monotone is a free distributed version control system. Montone-viz
is developed in the Objective Caml language, using the GTK+ and
libgnomecanvas libraries (via LablGTK, an OCaml binding for GTK+), and it
uses the dot program from the Graphviz package.

%prep
%setup -q
%patch0 -p1 -b .gio

%build
%configure --without-local-lablgtk
%make

%install
rm -rf %buildroot
%makeinstall

mkdir -p %buildroot/%{_datadir}/applications
cat > %buildroot/%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Monotone-viz
Comment=Visualizes monotone ancestry graphs
Exec=%{_bindir}/%{name}
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Development-Tools;Development;RevisionControl;
EOF

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/*
%doc COPYING NEWS README




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2011.0
+ Revision: 620390
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2010.0
+ Revision: 440089
- rebuild

* Thu Mar 05 2009 Jérôme Soyer <saispo@mandriva.org> 1.0.1-1mdv2009.1
+ Revision: 348932
- New upstream release

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 252727
- rebuild
- fix no-buildroot-tag
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 20 2007 Nicholas Brown <nickbrown@mandriva.org> 1.0-1mdv2008.1
+ Revision: 135614
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Feb 02 2007 Nicholas Brown <nickbrown@mandriva.org> 0.15-4mdv2007.0
+ Revision: 115971
- another attempt at fixing dependancies
- fix dependancies

* Thu Oct 19 2006 Nicholas Brown <nickbrown@mandriva.org> 0.15-3mdv2007.1
+ Revision: 71018
- add xdg menu
- bump release
- fix buildrequires properly again
- fix buildrequires properly
- fix buildrequires
- new release
- Import monotone-viz

* Mon Jun 19 2006 Pascal Terjan <pterjan@mandriva.org> 0.14-2mdv2007.0
- mkrel

* Mon Apr 17 2006 Nick Brown <nickbrown@mandriva.org> 0.14-1mdk
- 0.14

* Wed Feb 08 2006 Nick Brown <nickbrown@mandriva.org> 0.13-1mdk
- new release

* Sat Nov 05 2005 Nick Brown <nickbrown@mandriva.org> 0.12-1mdk
- First Mandriva package release

