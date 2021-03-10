#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-lua
Version  : 2.0.7
Release  : 8
URL      : https://pecl.php.net/get/lua-2.0.7.tgz
Source0  : https://pecl.php.net/get/lua-2.0.7.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-lua-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : lua-dev

%description
No detailed description available

%package lib
Summary: lib components for the php-lua package.
Group: Libraries

%description lib
lib components for the php-lua package.


%prep
%setup -q -n lua-2.0.7
cd %{_builddir}/lua-2.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/lua.so
