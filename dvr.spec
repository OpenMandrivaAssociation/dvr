%define name	dvr
%define version	3.0
%define release  %mkrel 1

Name: 	 	%{name}
Summary: 	Digital video recorder
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://dvr.sourceforge.net
License:	GPL
Group:		Video
BuildRequires:	libavifile-devel qt3-devel flex

%description
DVR stands for Digital Video Recorder.  In a few words DVR is a simple and
efficient software aiming at recording digital video on a Linux computer. DVR
runs on computers equipped with one or more video capture cards.
    * records simultaneously video and audio streams
    * uses standard AVI file format for data storage
    * uses common codecs
    * writes segmented files, in order to split large files
    * threaded : take profit of multi-processors computers
    * horizontal margin removal during capture

%prep
%setup -q

%build
%make
										
%install
rm -rf $RPM_BUILD_ROOT
export version=%version
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}-qtgui
Icon=%{name}
Name=DVR
Comment=Digital Video Recorder
Categories=AudioVideo;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/*
%{_datadir}/dvr-%{version}
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

