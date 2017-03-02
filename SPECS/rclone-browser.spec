Name:           rclone-browser
Version:        1.1
Release:        1%{?dist}
Summary:        Simple cross platform GUI for rclone

License:        Unlicense
URL:            https://mmozeiko.github.io/RcloneBrowser
Source0:        https://github.com/mmozeiko/RcloneBrowser/archive/1.1.tar.gz

BuildRequires:  cmake qt5-devel

%description
Simple cross platform GUI for rclone

%prep
%autosetup

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
