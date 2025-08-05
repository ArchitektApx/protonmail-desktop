%global debug_package %{nil}
%global _app_name proton-mail
%global _desktop_name Proton Mail
%global _version 1.8.1

Name          : protonmail-desktop
Version       : %{_version}
Release       : 1%{?dist}
Summary       : Proton official desktop application for Proton Mail and Proton Calendar
License       : GPL-3.0-or-later
URL           : https://proton.me
Source0       : https://github.com/ArchitektApx/%{name}/releases/download/%{_version}/%{_app_name}_%{_version}_arm64.deb
Source1       : https://github.com/ArchitektApx/%{name}/releases/download/%{_version}/%{_app_name}_%{_version}_amd64.deb
Requires       : alsa-lib
Requires       : gtk3
Requires       : gvfs
Requires       : libdrm
Requires       : libnotify
Requires       : nss
Requires       : xdg-utils
Suggests       : kde-cli-tools
Suggests       : libgnome-keyring
Suggests       : lsb-release
Suggests       : trash-cli

%description
Proton official desktop application for Proton Mail and Proton Calendar.

Bugs related to Proton Mail Desktop should be reported directly to the Upstream GitHub repo: 
<https://github.com/ProtonMail/WebClients>

Bugs related to this package should be reported at this Git project:
<https://github.com/ArchitektApx/protonmail-desktop>

%prep
# We are not building from source, just repackaging the .deb by extracting the .deb contents
%ifarch aarch64
ar p %{SOURCE0} data.tar.zst > data.tar.zst
%endif
%ifarch x86_64
ar p %{SOURCE1} data.tar.zst > data.tar.zst
%endif
tar xf data.tar.zst

%install
%__rm -rf %{buildroot}
%__install -d %{buildroot}{%{_bindir},%{_datadir}/applications,%{_datadir}/pixmaps,%{_datadir}/doc/%{_app_name},/opt}
# Move main application files to /opt/proton-mail
mv usr/lib/%{_app_name} %{buildroot}/opt
# Move desktop file to /usr/share/applications
mv usr/share/applications/%{_app_name}.desktop %{buildroot}%{_datadir}/applications
# Move license to /usr/share/doc
mv usr/share/doc/%{_app_name}/copyright %{buildroot}%{_datadir}/doc/%{_app_name}
# Move icon to /usr/share/pixmaps
mv usr/share/pixmaps/%{_app_name}.png %{buildroot}%{_datadir}/pixmaps
# Create a symlink for the executable
%__ln_s /opt/%{_app_name}/Proton\ Mail %{buildroot}%{_bindir}/%{_app_name}

%files
%license %{_datadir}/doc/%{_app_name}/copyright
%{_datadir}/applications/%{_app_name}.desktop
%{_datadir}/pixmaps/%{_app_name}.png
%{_bindir}/%{_app_name}
/opt/%{_app_name}

%changelog
* Tue Aug 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.1
- Update to upstream release 1.8.1

* Fri Mar 28 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.0
- Update to upstream release 1.8.0

* Tue Dec 17 2024 ArchitektApx <architektapx@gehinors.ch> - 1.6.0
- Initial Release
