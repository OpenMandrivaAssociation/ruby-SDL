%define real_name rubysdl

Summary: Wrapper around the cross platform Simple DirectMedia Layer game library
Name:    ruby-SDL
Version: 2.0.1
Release: 4
License: LGPLv2+
Source:  http://www.kmc.gr.jp/~ohai/rubysdl/%{real_name}-%{version}.tar.gz
Source1: http://www.kmc.gr.jp/~ohai/rubysdl_ref_2.en.html.bz2
Group:   Development/Ruby
URL:     http://www.kmc.gr.jp/~ohai/index.en.html
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_ttf-devel
BuildRequires: libsmpeg-devel
BuildRequires: ruby-devel

Provides: %{real_name} = %{version}-%{release}

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
%makeinstall_std

%files
%doc README.* sample rubysdl_const_list.txt reference_manual.html
%{ruby_sitelibdir}/*.rb
%{ruby_sitearchdir}/*.so

