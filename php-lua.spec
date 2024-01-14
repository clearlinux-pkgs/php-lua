#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-lua
Version  : 2.0.7
Release  : 51
URL      : https://pecl.php.net/get/lua-2.0.7.tgz
Source0  : https://pecl.php.net/get/lua-2.0.7.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-lua-lib = %{version}-%{release}
Requires: php-lua-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : lua-dev
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: PHP-8.patch

%description
No detailed description available

%package lib
Summary: lib components for the php-lua package.
Group: Libraries
Requires: php-lua-license = %{version}-%{release}

%description lib
lib components for the php-lua package.


%package license
Summary: license components for the php-lua package.
Group: Default

%description license
license components for the php-lua package.


%prep
%setup -q -n lua-2.0.7
cd %{_builddir}/lua-2.0.7
%patch -P 1 -p1
pushd ..
cp -a lua-2.0.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-lua
cp %{_builddir}/lua-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-lua/a1858e1db242bfbb45d60188d32289465bdc3c59 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/lua.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-lua/a1858e1db242bfbb45d60188d32289465bdc3c59
