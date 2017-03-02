Name:           rclone-browser
Version:        1.1
Release:        1%{?dist}
Summary:        Simple cross platform GUI for rclone

%global commit0 b86e821f435b957a5a456fcaeb0a2c0f61b3e43a
%global gittag0 HEAD
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

License:        Unlicense
URL:            https://mmozeiko.github.io/RcloneBrowser
Source0:        https://github.com/mmozeiko/RcloneBrowser/archive/%{version}.tar.gz
# Source0:  https://github.com/mmozeiko/RcloneBrowser/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake qt5-devel

%description
Simple cross platform GUI for rclone

%prep
%autosetup -n %{name}-%{version}
# %autosetup -n %{name}-%{commit0}

%build
%cmake .
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%check
ctest -V %{?_smp_mflags}

%files
%license LICENSE
%doc add-docs-here

%changelog
* Thu Mar  2 2017 Isaac Fischer <xwaver@xwaver.net>
- Initial build
