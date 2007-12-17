%define name    xmms-normalize
%define version 0.8.1
%define release %mkrel 7

Summary: Normalizing plugin for XMMS
Name: %{name}
Version: %{version}
Release: %{release}
Group: Sound
URL: http://volnorm.sourceforge.net/ 
Source: volnorm-%{version}.tar.bz2 
License: GPL
Requires: xmms >= 1.0.1
BuildRequires: xmms-devel 
BuildRequires: xmms
Provides: volnorm
Obsoletes: volnorm

%description
Volume Normalizer is an XMMS plugin that will set the volume of any played
song to some preset level. It ensures that all songs will have the same
volume and you will not need to hit the volume knob for each song.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n volnorm-%{version}/

%build

%configure2_5x --enable-one-plugin-dir
%make

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xmms/Effect/
install -m 755 src/.libs/*.so $RPM_BUILD_ROOT%{_libdir}/xmms/Effect/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL README RELEASE TODO NEWS ChangeLog BUGS 
%doc COPYING 
%{_libdir}/xmms/*/*.so

