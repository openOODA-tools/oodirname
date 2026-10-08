Name:           oodirname
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign POSIX dirname and path directory stripper in pure openOODA.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodirname
Source0:        oodirname-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodirname is a sovereign, capability-bounded POSIX dirname utility written
in pure openOODA, featuring zero ambient authority, IEEE Std 1003.1 compliance,
JSON Lines streaming, synthetic showcases, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodirname
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodirname-uninstall

%files
/usr/bin/oodirname
/usr/bin/oodirname-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign pure openOODA elevation with dual-surface CLI and MCP
