Name:           oodirname
Version:        0.1.0
Release:        1%{?dist}
Summary:        Extracts parent directory portion from path strings adhering to POSIX standards.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodirname
Source0:        oodirname-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodirname is a sovereign, capability-bounded DIRECTORY STRIPPER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodirname
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodirname-uninstall

%files
/usr/bin/oodirname
/usr/bin/oodirname-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
