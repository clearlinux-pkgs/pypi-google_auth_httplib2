#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-google_auth_httplib2
Version  : 0.1.0
Release  : 31
URL      : https://files.pythonhosted.org/packages/c6/b5/a9e956fd904ecb34ec9d297616fe98fa4106fc12f3b0a914dec983c267b9/google-auth-httplib2-0.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c6/b5/a9e956fd904ecb34ec9d297616fe98fa4106fc12f3b0a914dec983c267b9/google-auth-httplib2-0.1.0.tar.gz
Summary  : Google Authentication Library: httplib2 transport
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-google_auth_httplib2-license = %{version}-%{release}
Requires: pypi-google_auth_httplib2-python = %{version}-%{release}
Requires: pypi-google_auth_httplib2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(google_auth)
BuildRequires : pypi(httplib2)
BuildRequires : pypi(six)

%description
======================================
        
        |pypi|
        
        This library provides an `httplib2`_ transport for `google-auth`_.

%package license
Summary: license components for the pypi-google_auth_httplib2 package.
Group: Default

%description license
license components for the pypi-google_auth_httplib2 package.


%package python
Summary: python components for the pypi-google_auth_httplib2 package.
Group: Default
Requires: pypi-google_auth_httplib2-python3 = %{version}-%{release}

%description python
python components for the pypi-google_auth_httplib2 package.


%package python3
Summary: python3 components for the pypi-google_auth_httplib2 package.
Group: Default
Requires: python3-core
Provides: pypi(google_auth_httplib2)
Requires: pypi(google_auth)
Requires: pypi(httplib2)
Requires: pypi(six)

%description python3
python3 components for the pypi-google_auth_httplib2 package.


%prep
%setup -q -n google-auth-httplib2-0.1.0
cd %{_builddir}/google-auth-httplib2-0.1.0
pushd ..
cp -a google-auth-httplib2-0.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656402855
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-google_auth_httplib2
cp %{_builddir}/google-auth-httplib2-0.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-google_auth_httplib2/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-google_auth_httplib2/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
