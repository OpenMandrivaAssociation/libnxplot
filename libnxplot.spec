%define	version 0.2
%define release %mkrel 9

%define major 0
%define libname %mklibname nxplot %{major}

Summary:	NumExp plotting library
Name:		libnxplot
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Sciences/Mathematics
URL:		https://numexp.sf.net/
Source:		%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgnomeprintui2-2-devel
BuildRequires:	pygtk2.0-devel >= 2.4.0
BuildRequires:	gnome-python >= 2.6.0


%description
%{name} is a 2D vector drawing library, splitted from gNumexp (a graphical
frontend of NumExp). It has an API very similar to libplot, from GNU plotting
utilities. There are implementations, or drivers:

- nxplot-artft: this is a nxplot driver that uses libart_lgpl and
freetype to render a pixel buffer.  The pixel buffer can be either associated
to a widget (a GtkDrawingArea, usually), or it can be created without widget
with an explicit size and later retrieved as a GdkPixbuf.

- nxplot-gp: this is a libgnomeprint based driver, to enable you to send
2D vector drawings directly to a printer without rasterization, thus preserving
all quality.


%package	-n %{libname}
Summary:	NumExp plotting library
Group:		Sciences/Mathematics
Provides:	%{name} = %{version}-%{release}

%description	-n %{libname}
%{name} is a 2D vector drawing library, splitted from gNumexp (a graphical
frontend of NumExp). It has an API very similar to libplot, from GNU plotting
utilities. There are implementations, or drivers:

- nxplot-artft: this is a nxplot driver that uses libart_lgpl and
freetype to render a pixel buffer.  The pixel buffer can be either associated
to a widget (a GtkDrawingArea, usually), or it can be created without widget
with an explicit size and later retrieved as a GdkPixbuf.

- nxplot-gp: this is a libgnomeprint based driver, to enable you to send
2D vector drawings directly to a printer without rasterization, thus preserving
all quality.


%package	python
Summary:	Python binding for NumExp plotting library
Group:		Sciences/Mathematics
Requires:	%{libname} = %{version}

%description	python
%{name} is a 2D vector drawing library, splitted from gNumexp (a graphical
frontend of NumExp). It has an API very similar to libplot, from GNU plotting
utilities.

This package contains a python implementation of %{name} drawing library.


%package	-n %{libname}-devel
Summary:	Development related files for %{name}
Group:		Sciences/Mathematics
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description	-n %{libname}-devel
%{name} is a 2D vector drawing library, splitted from gNumexp (a graphical
frontend of NumExp). It has an API very similar to libplot, from GNU plotting
utilities.

This package contains all development related files, necessary for
compiling or developing applications related to numexp.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove files not bundled
rm -f %{buildroot}%{_libdir}/python?.?/site-packages/*.{a,la}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/lib*.so.*

%files python
%defattr(-,root,root)
%{py_platsitedir}/*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc ChangeLog
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*


