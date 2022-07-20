Name:           python-ddtrace
Version:        1.2.2
Release:        1
License:        BSD
Summary:        Datadog tracing code
Url:            https://github.com/DataDog/dd-trace-py
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/ddtrace/ddtrace-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools-scm)
# SECTION test requirements
#BuildRequires:  %{python_module intervaltree}
BuildRequires:  python3dist(protobuf)
#BuildRequires:  python3dist(tenacity)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
# /SECTION
BuildRequires:  fdupes
#Requires:       python-intervaltree
Requires:       python-protobuf >= 3
#Requires:       python-tenacity >= 5
Suggests:       python-enum34
Suggests:       python-funcsigs >= 1.0.0
#Suggests:       python-opentracing >= 2.0.0


%description
Datadog tracing code

%prep
%setup -q -n ddtrace-%{version}
#rm tox.ini

%build
%py_build

%install
%py_install

%check
%pytest_arch

%files
%doc CHANGELOG.md README.md
%license LICENSE LICENSE.Apache LICENSE.BSD3
%python3_only %{_bindir}/ddtrace-run
%python3_only %{_bindir}/pyddprofile
%{python_sitearch}/*
