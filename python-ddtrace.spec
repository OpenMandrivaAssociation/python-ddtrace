Name:           python-ddtrace
Version:        0.41.0
Release:        0
License:        BSD (FIXME:No SPDX)
Summary:        Datadog tracing code
Url:            https://github.com/DataDog/dd-trace-py
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/ddtrace/ddtrace-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools_scm}
# SECTION test requirements
BuildRequires:  %{python_module intervaltree}
BuildRequires:  %{python_module protobuf >= 3}
BuildRequires:  %{python_module tenacity >= 5}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-intervaltree
Requires:       python-protobuf >= 3
Requires:       python-tenacity >= 5
Suggests:       python-enum34
Suggests:       python-funcsigs >= 1.0.0
Suggests:       python-opentracing >= 2.0.0

%python_subpackages

%description
Datadog tracing code

%prep
%setup -q -n ddtrace-%{version}
rm tox.ini

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE LICENSE.Apache LICENSE.BSD3
%python3_only %{_bindir}/ddtrace-run
%python3_only %{_bindir}/pyddprofile
%{python_sitearch}/*
