%global debug_package %{nil}

Name: python-setuptools-rust
Epoch: 100
Version: 1.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Setuptools Rust extension plugin
License: MIT
URL: https://github.com/PyO3/setuptools-rust/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Setuptools helpers for Rust Python extensions. Compile and distribute
Python extensions written in Rust as easily as if they were written in
C.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-setuptools-rust
Summary: Setuptools Rust extension plugin
Requires: python3
Requires: python3-semantic_version >= 2.6
Requires: python3-setuptools >= 46.1
Requires: python3-tomli >= 1.2.1
Requires: python3-typing-extensions >= 3.7.4.3
Provides: python3-setuptools-rust = %{epoch}:%{version}-%{release}
Provides: python3dist(setuptools-rust) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-setuptools-rust = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(setuptools-rust) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-setuptools-rust = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(setuptools-rust) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-setuptools-rust
Setuptools helpers for Rust Python extensions. Compile and distribute
Python extensions written in Rust as easily as if they were written in
C.

%files -n python%{python3_version_nodots}-setuptools-rust
%license LICENSE
%{python3_sitelib}/setuptools_rust*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-setuptools-rust
Summary: Setuptools Rust extension plugin
Requires: python3
Requires: python3-semantic_version >= 2.6
Requires: python3-setuptools >= 46.1
Requires: python3-tomli >= 1.2.1
Requires: python3-typing-extensions >= 3.7.4.3
Provides: python3-setuptools-rust = %{epoch}:%{version}-%{release}
Provides: python3dist(setuptools-rust) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-setuptools-rust = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(setuptools-rust) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-setuptools-rust = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(setuptools-rust) = %{epoch}:%{version}-%{release}

%description -n python3-setuptools-rust
Setuptools helpers for Rust Python extensions. Compile and distribute
Python extensions written in Rust as easily as if they were written in
C.

%files -n python3-setuptools-rust
%license LICENSE
%{python3_sitelib}/setuptools_rust*
%endif

%changelog
