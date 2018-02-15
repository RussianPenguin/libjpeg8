Name:           compat-libjpeg8
Version:        1.5.3
Release:        3%{?dist}
Summary:        The MMX/SSE accelerated JPEG compression/decompression library
License:        IJG
URL:            http://sourceforge.net/projects/libjpeg-turbo

Source0:        http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-%{version}.tar.gz
Patch0:         libjpeg-turbo14-noinst.patch
Patch1:         libjpeg-turbo-header-files.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  gcc

%description
The compat-libjpeg8 package contains a library of functions for manipulating JPEG
images.

%package devel
Summary:        Headers for the compat-libjpeg8 library
Conflicts:      libjpeg-turbo-devel

%description devel
This package contains header files necessary for developing programs which will
manipulate JPEG files using the compat-libjpeg8 library.

%prep
%autosetup -n libjpeg-turbo-%{version} -p1
chmod -x README.md

%build
autoreconf -vif
%configure --disable-static --without-turbojpeg --with-jpeg8
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

# We need only library for this compat package, so we need to remove all
# installed by default make sequence executables.
rm -f %{buildroot}%{_bindir}/{cjpeg,djpeg,jpegtran,rdjpgcom,wrjpgcom}
rm -rf %{buildroot}%{_mandir}*

%ldconfig_scriptlets

%files
%doc README.md README.ijg ChangeLog.md
%{_libdir}/libjpeg.so.8*

%files devel
%doc coderules.txt jconfig.txt libjpeg.txt structure.txt example.c
%{_includedir}/jconfig*.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpegint.h
%{_includedir}/jpeglib.h
%{_libdir}/libjpeg.so
%{_libdir}/pkgconfig/libjpeg.pc

%changelog
* Thu Feb 15 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Created compat package with API/ABI version 8 support. Based on libjpeg-turbo.
