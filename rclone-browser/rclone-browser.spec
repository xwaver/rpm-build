%global commit0 b86e821f435b957a5a456fcaeb0a2c0f61b3e43a
%global gittag0 HEAD
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global checkout 20170302git%{shortcommit0}

Name:           rclone-browser
Version:        1.1
Release:        1.%{shortcommit0}%{?dist}
Summary:        Simple cross platform GUI for rclone

License:        Unlicense
URL:            https://mmozeiko.github.io/RcloneBrowser
Source0:  https://github.com/mmozeiko/RcloneBrowser/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz

BuildRequires:  cmake pkgconfig(Qt)

%description
Simple cross platform GUI for rclone

%prep
# %autosetup -n %{name}-%{version}
%autosetup -n RcloneBrowser-%{commit0}

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
* Thu Mar 02 2017 Isaac Fischer <xwaver@xwaver.net> 1.1-1
- new package built with tito
