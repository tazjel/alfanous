# to complete
Summary: The desktop interface of alfanous project 
Name: alfanousDesktop
Version: 0.4.3
URL: www.alfanous.org
Release: Al-Assas
Copyright: AGPL
Group: Applications/Internet
#Source: http://alfanous.sourceforge.net
#Patch: eject-2.0.2-buildroot.patch
BuildRoot: /var/tmp/%{name}-buildroot

BuildRequires: gettext
Requires:   python  python-qt4

%description
Alfanous is a search engine API provide the simple and advanced search in the Holy Qur'an and more features... 

%prep
%setup -q
%patch -p1 -b .buildroot

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cp -R ./usr $RPM_BUILD_ROOT



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO COPYING ChangeLog AUTHORS




%changelog
* Sun May 21 2010 Assem Chelli <assem.ch@gmail.com> 
- Initial release of alfanous for redhat distro





