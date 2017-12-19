Summary:	Stop relying on NFS for horizontal scaling. Speed up Git access using caching
Name:		gitaly
Version:	0.52.1
Release:	1
License:	MIT
Group:		Networking/Daemons/HTTP
Source0:	https://gitlab.com/gitlab-org/gitaly/repository/archive.tar.bz2?ref=v%{version}&/%{name}-%{version}.tar.bz2
# Source0-md5:	4969571c7accfd57b460f08b6fe34a75
URL:		https://gitlab.com/gitlab-org/gitaly
BuildRequires:	cmake
BuildRequires:	golang >= 1.8
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	ruby > 1:2.3
BuildRequires:	ruby-bundler
BuildRequires:	ruby-devel
BuildRequires:	ruby-io-console
BuildRequires:	ruby-rubygems >= 2.6.9
BuildRequires:	zlib-devel
Requires:	git-core >= 2.13.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gitaly is a Git RPC service for handling all the git calls made by
GitLab.

%prep
%setup -qc
mv %{name}-v%{version}-*/* .

%build
# enable-gems to workaround
RUBYOPT=--enable-gems \
%{__make} \
	VERSION=%{version}

# verify
./gitaly --version > v
grep "%{version}" v

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE
%attr(755,root,root) %{_bindir}/gitaly
%attr(755,root,root) %{_bindir}/gitaly-ssh
