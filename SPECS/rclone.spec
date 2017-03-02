Name:           rclone
Version:        1.35
Release:        1%{?dist}
Summary:        rsync for cloud storage. Sync files to and from many cloud storage providers.

License:        MIT
URL:            http://rclone.org/
Source0:        https://github.com/ncw/rclone/archive/%{name}-%{version}.tar.gz
ExclusiveArch:	%{go_arches}

BuildRequires:  compiler(go-compilers)

%description
Rclone is a command line program to sync files and directories to and from:
Google Drive, Amazon S3, Openstack Swift / Rackspace cloud files / Memset Memstore,
Dropbox, Google Cloud Storage, Amazon Drive, Microsoft One Drive, Hubic,
Backblaze B2, Yandex Disk, & The local filesystem

%prep
%autosetup


%build
mkdir -p src/github.com/ncw
ln -s ../../../ src/github.com/ncw/rclone

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
echo "Unable to build from bundled deps. No Godeps nor vendor directory"
exit 1
%endif

%gobuild -o bin/rclone %{import_path}

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_bindir}
install -p -m 755 bin/rclone %{buildroot}%{_bindir}


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Sun Feb 12 2017 Isaac Fischer <xwaver@xwaver.net>
- Initial build
