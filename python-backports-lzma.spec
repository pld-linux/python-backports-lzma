# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module	lzma
Summary:	Backport of Python 3.3's standard library module lzma for LZMA/XY compressed files
Name:		python-backports-%{module}
Version:	0.0.12
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	https://github.com/peterjc/backports.lzma/archive/backports.lzma.v%{version}.tar.gz
# Source0-md5:	98851bc45dd410b9bb3d8a37770dc750
URL:		https://github.com/peterjc/backports.lzma
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel < 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backport of Python 3.3's standard library module lzma for LZMA/XY
compressed files.

%package -n python3-%{module}
Summary:	Backport of Python 3.3's standard library module lzma for LZMA/XY compressed files
Group:		Libraries/Python
Requires:	python3-modules < 1:3.3

%description -n python3-%{module}
Backport of Python 3.3's standard library module lzma for LZMA/XY
compressed files

%prep
%setup -q -n backports.%{module}-backports.%{module}.v%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitedir}/backports/%{module}
%{py_sitedir}/backports/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/backports/%{module}/*.so
%{py_sitedir}/backports.%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/backports/%{module}
%{py3_sitedir}/backports/%{module}/*.py
%attr(755,root,root) %{py3_sitedir}/backports/%{module}/*.so
%{py3_sitedir}/backports/%{module}/__pycache__
%{py3_sitedir}/backports.%{module}-%{version}-py*.egg-info
%endif
