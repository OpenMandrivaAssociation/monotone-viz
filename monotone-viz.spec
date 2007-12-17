%define name monotone-viz
%define version 0.15
%define release %mkrel 4

Summary: A small GTK+ application that visualizes monotone ancestry graphs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://oandrieu.nerim.net/monotone-viz/
BuildRequires: ocaml-lablgtk2-devel camlp4 libgnomecanvas2-devel libopenssl-static-devel monotone
BuildRequires: libsqlite3-devel
Requires: monotone graphviz

%description
Monotone-viz is a small GTK+ application that visualizes monotone ancestry
graphs. Monotone is a free distributed version control system. Montone-viz
is developed in the Objective Caml language, using the GTK+ and
libgnomecanvas libraries (via LablGTK, an OCaml binding for GTK+), and it
uses the dot program from the Graphviz package. 

%prep
%setup -q

%build
%configure --without-local-lablgtk
%make

%install
rm -rf %buildroot
%makeinstall
install -d -m 0755 %buildroot/%_menudir
cat << EOF > %buildroot/%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" \
needs="X11" section="More Applications/Development/Tools" \
title="Monotone-viz" longtitle="Visualizes monotone ancestry graphs" \
accept_url="false" \
xdg="true"
EOF

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

%post 
%{update_menus} 

%postun 
%{clean_menus} 

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_menudir}/%{name}
%{_datadir}/applications/*
%doc COPYING NEWS README


