Name:           waydroid-vendor17.1-treltexx
Version:        1.0.0
Release:        1
Summary:        Waydroid-vendor17.1-treltexx installs the latest waydroid 17.1 vendor image with added the Galaxy Note 4 (treltexx) specific drivers.
License:        GPLv3
URL:            https://github.com/edp17/waydroid-vendor17.1-treltexx
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  systemd
BuildRequires:  desktop-file-utils
Requires:       dnsmasq
Requires:       python3-gbinder
Requires:       python3-gobject
Requires:       waydroid-sensors
Requires:       waydroid-gbinder-config-hybris
Requires:       waydroid-1.2-treltexx

%description
Waydroid uses Linux namespaces (user, pid, uts, net, mount, ipc) to run a full Android system in a container and provide Android applications on any GNU/Linux-based platform.

The Android system inside the container has direct access to any needed hardware.

The Android runtime environment ships with a minimal customized Android system image based on LineageOS. The image is currently based on Android 10.

Waydroid-vendor17.1-treltexx installs the latest waydroid 17.1 vendor image with added the Galaxy Note 4 (treltexx) specific drivers.

%prep
%setup

%install
mkdir -p %{buildroot}/home/waydroid/images

tar xvjf config/vendor.img.tar.bz2 -C %{buildroot}/home/waydroid/images/

%clean
rm -rf $RPM_BUILD_ROOT

%post
systemctl daemon-reload
systemctl-user daemon-reload
systemctl restart waydroid-container
chmod 777 /home/waydroid

%files
%defattr(-,root,root,-)
%attr(-, defaultuser, users)/home/waydroid
/home/waydroid/images/vendor.img
