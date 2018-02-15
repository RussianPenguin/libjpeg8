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

# We need only shared library for this compat package, so we will remove
# all other installed by default make sequence files.
rm -f %{buildroot}%{_bindir}/{cjpeg,djpeg,jpegtran,rdjpgcom,wrjpgcom}
rm -f %{buildroot}%{_libdir}/libjpeg.so
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_mandir}

%ldconfig_scriptlets

%files
%doc README.md ChangeLog.md
%license LICENSE.md README.ijg
%{_libdir}/libjpeg.so.8*

%changelog
* Thu Feb 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.3-3
- Created compat package with API/ABI version 8 support. Based on libjpeg-turbo.
