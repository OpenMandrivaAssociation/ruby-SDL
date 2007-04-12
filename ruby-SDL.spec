%define real_name rubysdl
%define name ruby-SDL
%define version 1.0.0
%define release 1mdk

Summary: Wrapper around the cross platform Simple DirectMedia Layer game library
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPL
Source: http://www.kmc.gr.jp/~ohai/rubysdl/%{real_name}-%{version}.tar.bz2
Source1: http://www.kmc.gr.jp/~ohai/rubysdl_doc.en.html.bz2
Group: Development/Other
URL: http://www.kmc.gr.jp/~ohai/index.en.html
BuildRequires: XFree86-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libsmpeg-devel ruby-devel
Provides: %{real_name} = %{version}-%{release}
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot/
# Author: ohai@kmc.kyoto-u.ac.jp

%{expand:%%define ruby_libdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}
%{expand:%%define ruby_archdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

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
%{ruby_libdir}/*.rb
%{ruby_archdir}/*.so

