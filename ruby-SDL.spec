%define real_name rubysdl
%define name ruby-SDL
%define version 2.0.1
%define release %mkrel 2

Summary: Wrapper around the cross platform Simple DirectMedia Layer game library
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPLv2+
Source: http://www.kmc.gr.jp/~ohai/rubysdl/%{real_name}-%{version}.tar.gz
Source1: http://www.kmc.gr.jp/~ohai/rubysdl_ref_2.en.html.bz2
Group: Development/Ruby
URL: http://www.kmc.gr.jp/~ohai/index.en.html
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libsmpeg-devel ruby-devel
Provides: %{real_name} = %{version}-%{release}
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot/

%description
Ruby-SDL is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in Ruby,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%setup -q -n %{real_name}-%{version}
bzcat %{SOURCE1} > reference_manual.html

%build
ruby extconf.rb --enable-opengl
make
sed -i 's|/usr/local/bin/ruby|/usr/bin/ruby|' sample/*.rb
chmod 0755 sample/kanji.rb

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README.* sample rubysdl_const_list.txt reference_manual.html
%{ruby_sitelibdir}/*.rb
%{ruby_sitearchdir}/*.so



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0.1-2mdv2010.0
+ Revision: 433550
- rebuild

* Sun Jul 06 2008 Funda Wang <fundawang@mandriva.org> 2.0.1-1mdv2009.0
+ Revision: 232194
- New version 2.0.1

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.3.0-1mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 1.3.0-1mdv2008.0
+ Revision: 16990
- 1.3.0
- Use mkrel
- Use Development/Ruby group
- Use std macros


* Fri Oct 28 2005 Pascal Terjan <pterjan@mandriva.org> 1.0.0-1mdk
- New release 1.0.0

* Mon Jul 11 2005 Pascal Terjan <pterjan@mandriva.org> 0.9.5-1mdk
- 0.9.5

* Fri Apr 01 2005 Pascal Terjan <pterjan@mandrake.org> 0.9.3-2mdk
- lib64 fix

* Mon Jul 26 2004 Pascal Terjan <pterjan@mandrake.org> 0.9.3-1mdk
- new release

* Tue Jun 01 2004 Pixel <pixel@mandrakesoft.com> 0.9.2-1mdk
- new release

* Thu Aug 07 2003 Pixel <pixel@mandrakesoft.com> 0.8.3-2mdk
- rebuild for ruby 1.8.0

* Tue Feb 18 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.3-1mdk
- update code and doc

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.7-4mdk
- rebuild

* Sun Jul 21 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.7-3mdk
- recompile against new vorbis stuff

* Mon Apr 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.7-2mdk
- rebuild for new alsa

* Sat Mar 09 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.7-1mdk
- first mandrake package

