%define slipperver         1.0
%define slipperminorver    1
%define _prefix            /usr/local/bin 

Name:           ruby_slipper
Version:        %{slipperver}%{slipperminorver}
Release:        1%{?dist}
License:        GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ruby
Source0:        %{name}-%{version}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages

%description
ruby_slipper is a simple script to switch your environment between versions of ruby.

%prep
%setup -n %{name}-%{slipperver}-%{slipperminorver}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}
install %{name} $RPM_BUILD_ROOT/%{_prefix}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755, root, root)
%{_prefix}/%{name}

%changelog
* Wed Aug 17 2011 Brian Butler <brian@tumblr.com> - 1.0-1
- Created initial spec for ruby_slipper script
