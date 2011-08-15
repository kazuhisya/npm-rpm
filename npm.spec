Name:          npm
Version:       1.0.23
Release:       1%{?dist}
Summary:       A package manager for Node.js
Packager:      Kazuhisa Hara <kazuhisya@gmail.com>
Group:         Development/Libraries
License:       MIT License
URL:           http://npmjs.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
Source0:       npm-%{version}.tgz
BuildRequires: nodejs
Requires:      nodejs
BuildArch:     noarch

%description
NPM is a package manager for Node.js.
You can use it to install and publish your node programs.
It manages dependencies and does other cool stuff.

%prep
%setup -q -c
install_module() {
    tar --transform "s|^package|node_modules/$1|g" --show-transformed -zxf $2
}

%build

%install
cd package
rm -rf $RPM_BUILD_ROOT
npm_config_prefix=$RPM_BUILD_ROOT/usr \
npm_config_root=$RPM_BUILD_ROOT/usr/lib/node \
npm_config_binroot=$RPM_BUILD_ROOT%{_bindir} \
npm_config_manroot=$RPM_BUILD_ROOT%{_mandir} \
node ./cli.js install -g

%files
%defattr(-,root,root,-)
%{_prefix}/lib/node_modules/npm
%{_bindir}/npm*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Aug  8 2011 Kazuhisa Hara <kazuhisya@gmail.com>
- Updated to mpn version 1.0.23
* Fri Jul 29 2011 Kazuhisa Hara <kazuhisya@gmail.com>
- Initial version
