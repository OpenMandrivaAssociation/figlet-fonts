%define _fontdir %{_datadir}/figlet

Name: figlet-fonts
Version: 2010018
Release: %mkrel 1
Summary: Additional fonts for FIGlet
URL: https://github.com/cmatsuoka/figlet-fonts
Group: Toys
License: Public domain
Source: contributed.tar.gz
Source2: jave.tar.gz 
Source3: international.tar.gz
Source4: cjkfonts.tar.gz
Source5: bdffonts.tar.gz
BuildRequires: zip
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains additional fonts for figlet.

%package -n figlet-more-fonts
Summary: More fonts for FIGlet
Requires: figlet
Requires: figlet-fonts-contributed
Requires: figlet-fonts-international
Requires: figlet-fonts-bdf

%description -n figlet-more-fonts
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package is a metapackage that installs many fonts for FIGlet.

%package contributed
Summary: Contributed fonts for FIGlet
Requires: figlet
Obsoletes: figlet-more-fonts <= 20110110

%description contributed
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains many fonts for FIGlet including classic contributed
fonts from ftp.figlet.org and fonts collected by Markus Gebhard for the
JavE project.

%package international
Summary: International fonts for FIGlet
Requires: figlet
Obsoletes: figlet-more-fonts <= 20110110

%description international
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains international fonts for figlet, including
CJK fonts, Hebrew, Cyrillic, Greek, Cherokee, Futhark, Tengwar
and Morse code.

%package c64
Summary: Commodore 64 fonts for FIGlet
Requires: figlet
Obsoletes: figlet-more-fonts <= 20110110

%description c64
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains Commodore 64 fonts converted for FIGlet by
by David Proper.

%package bdf
Summary: X Window System fonts for FIGlet
License: MIT
Requires: figlet
Obsoletes: figlet-more-fonts <= 20110110

%description bdf
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains fonts converted from the BDF format distributed by
the X Consortium, including Lucida Bright, Charter, Courier, Helvetica,
Lucida Sans, New Century Schoolbook, Times Roman, Lucida Sans Typewriter,
Utopia and fixed-width fonts.

%prep
%setup -q -b0 -c %{name}-%{version} 
%setup -q -b2 -c %{name}-%{version} -D
%setup -q -b3 -c %{name}-%{version} -D
%setup -q -b4 -c %{name}-%{version} -D
%setup -q -b5 -c %{name}-%{version} -D

%build
mv jave/*.fl[fc] contributed/
mv cjkfonts/*.fl[fc] international/

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_fontdir}

rm contributed/banner.flf
#(cd C64-fonts; for i in *.flf; do mv $i c64-$i; done)
for i in contributed international bdffonts; do
  find $i -name "*.fl[cf]" | sed "s!.*/!%{_fontdir}/!" > $i.list
  find $i -name "*.fl[cf]" -exec cp {} %{buildroot}%{_fontdir}/ \;
done

# Compress fonts
(cd %{buildroot}%{_fontdir}/
chmod 644 *  
for i in *; do
  zip -m $i.zip $i
  mv $i.zip $i
done)

%clean
rm -rf %{buildroot}

%files -n figlet-more-fonts

%files contributed -f contributed.list
%defattr(0644,root,root,0755)

%files international -f international.list
%defattr(0644,root,root,0755)

#%files fonts-c64 -f C64-fonts.list
#%defattr(0644,root,root,0755)

%files bdf -f bdffonts.list
%defattr(0644,root,root,0755)
%doc bdffonts/bdffont1.txt bdffonts/bdf2flf.pl

