# Generated from jruby-rack-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(jruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(jruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname jruby-rack
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Rack adapter for JRuby and Servlet Containers
Name: %{gemname}
Version: 1.0.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://jruby.org
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: jruby
BuildRequires: jruby
BuildArch: noarch
Provides: %{gemname} = %{version}

%description
JRuby-Rack is a combined Java and Ruby library that adapts the Java Servlet
API to Rack. For JRuby only.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
jgem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Oct 15 2010 : Sergio Rubio <rubiojr@frameos.org> - 1.0.3-1
- Initial package
