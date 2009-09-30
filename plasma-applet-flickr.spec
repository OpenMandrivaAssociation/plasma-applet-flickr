%define		oname  flickrop
Summary:	Flickr On Plasma
Name:		plasma-applet-flickr
Version: 	0.7
Release: 	%mkrel 1
Source0:	%oname-%version.tar.bz2
License: 	GPLv3
Group: 		Graphical desktop/KDE
Url: 		http://kde-look.org/content/show.php/Flickr+On+Plasma?content=94800
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
#BuildRequires:  kde4-macros
BuildRequires:  kdelibs4-devel


%description 
The Plasma applet showing:
- the most interesting pictures on Flickr
- your favorite photos
- a particular photoset
- a set of photos based on a tag

%files -f %{oname}.lang
%defattr(-,root,root)
%{_kde_libdir}/kde4/*
%{_kde_datadir}/kde4/services/*

%prep
%setup -q -n %oname-%version

%build
%cmake_kde4
%make

%install
%find_lang %{oname}

rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -

%clean
rm -rf %{buildroot}

