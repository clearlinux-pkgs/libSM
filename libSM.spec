#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libSM
Version  : 1.2.2
Release  : 4
URL      : http://xorg.freedesktop.org/releases/individual/lib/libSM-1.2.2.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libSM-1.2.2.tar.gz
Summary  : X Session Management Library
Group    : Development/Tools
License  : MIT
Requires: libSM-lib
Requires: libSM-doc
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xtrans)
BuildRequires : xmlto

%description
libSM - X Session Management Library
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libSM package.
Group: Development
Requires: libSM-lib

%description dev
dev components for the libSM package.


%package doc
Summary: doc components for the libSM package.
Group: Documentation

%description doc
doc components for the libSM package.


%package lib
Summary: lib components for the libSM package.
Group: Libraries

%description lib
lib components for the libSM package.


%prep
%setup -q -n libSM-1.2.2

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/SM/SM.h
/usr/include/X11/SM/SMlib.h
/usr/include/X11/SM/SMproto.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libSM/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
