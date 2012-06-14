# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       meegotouchcp-connman
Summary:    MeegoTouchControlPanel wifi Plugin
Version:    0.2.0
Release:    1
Group:      System/GUI/Other
License:    Apache License
URL:        http://www.meego.com
Source0:    %{name}-%{version}.tar.bz2
Source100:  meegotouchcp-connman.yaml
Requires:   connman-qt-declarative


%description
This is a plugin for meegotouch-controlpanel that does wifi




%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
export PATH=$PATH:/usr/lib/qt4/bin
qmake install_prefix=/usr
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
export INSTALL_ROOT=%{buildroot}
# << install pre
%make_install

# >> install post
# << install post






%files
%defattr(-,root,root,-)
%{_libdir}/duicontrolpanel/meegotouchcp-connman.desktop
%{_datadir}/duicontrolpanel/wifi/mainpage.qml
%{_libdir}/qt4/imports/Connman/js/mustache.js
# >> files
# << files


