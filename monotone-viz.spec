%define name monotone-viz
%define version 1.0.1
%define release %mkrel 1

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


