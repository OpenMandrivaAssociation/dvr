Name: 	 	dvr
Summary: 	Digital video recorder
Version: 	3.99.3
Release: 	%mkrel 5

Source:		http://www.pierrox.net/dvr/releases/%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
# From upstream SVN: fixes a code error that breaks build
# - AdamW 2007/02
Patch0:		dvr-3.99.3-build.patch
URL:		http://www.pierrox.net/dvr/
License:	GPLv2+
Group:		Video
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgstreamer-devel >= 0.10
BuildRequires:	qt3-devel

%description
DVR stands for Digital Video Recorder.  In a few words DVR is a simple and
efficient software aiming at recording digital video on a Linux computer. DVR
runs on computers equipped with one or more video capture cards.
    * records simultaneously video and audio streams
    * uses standard AVI file format for data storage
    * uses common codecs
    * writes segmented files, in order to split large files
    * threaded: take profit of multi-processors computers
    * horizontal margin removal during capture

%prep
%setup -q
%patch0 -p1 -b .build

%build
pushd src
sed -i -e 's,/usr/local,%{buildroot}%{_prefix},g' Makefile
sed -i -e 's,/usr/lib/qt,%{qt3lib},g' Makefile
sed -i -e 's,/usr/include/qt,%{qt3include},g' Makefile
sed -i -e 's.-g.%{optflags}.g' Makefile
export PATH=$PATH:%{qt3dir}/bin
%make
popd
										
%install
rm -rf %{buildroot}
pushd src
export PATH=$PATH:%{qt3dir}/bin
%makeinstall
popd

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Name=DVR
Comment=Digital Video Recorder
Categories=Qt;AudioVideo;Recorder;
EOF

#icons
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m 644 %{SOURCE1} %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 644 %{SOURCE3} %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif
		
%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/*
%{_datadir}/dvr-%{version}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

