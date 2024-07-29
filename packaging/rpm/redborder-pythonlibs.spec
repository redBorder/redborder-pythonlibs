%undefine __brp_mangle_shebangs
%global debug_package %{nil}

Name: redborder-pythonlibs
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: x86_64
Summary: Main package for redborder python3 libs

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-pythonlibs

BuildRequires:  python3.9 python3.9-setuptools python3.9-pip
BuildRequires:  wget

%description
This package installs specified pip packages for Python 3.9 and extracts them to /usr/lib/python3.9.

%prep
%setup -c -T
mkdir -p %{_builddir}/pip-packages

%build


# Install additional pip packages
/usr/bin/pip3 install --target=%{_builddir}/pip-packages pyattck

%install
mkdir -p %{buildroot}/usr/lib/python3.9/site-packages
rm -rf %{_builddir}/pip-packages/__pycache__/six*
rm -rf %{_builddir}/pip-packages/six*
cp -r %{_builddir}/pip-packages/* %{buildroot}/usr/lib/python3.9/site-packages/

%files
/usr/lib/python3.9

%changelog
* Mon Jul 29 Miguel Álvarez <malvarez@redborder.com> -
- first spec version
