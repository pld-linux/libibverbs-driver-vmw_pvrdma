Summary:	Userspace driver for the VMware Paravirtual RDMA devices
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla urządzeń VMware Paravirtual RDMA
Name:		libibverbs-driver-vmw_pvrdma
Version:	1.0.0
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/libvmw_pvrdma/libvmw_pvrdma-%{version}.tar.gz
# Source0-md5:	7335fafdee1796a0642ead96a7698218
URL:		http://openib.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	libibverbs-devel >= 1.1.7
BuildRequires:	libtool >= 2:2
Requires:	libibverbs >= 1.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
libvmw_pvrdma is a userspace driver for VMware Paravirtual RDMA. It
works as a plug-in module for libibverbs that allows programs to use
the VMware Paravirtual RDMA device directly from user space.

%description -l pl.UTF-8
libvmw_pvrdma to sterownik przestrzeni użytkownika dla VMware
Paravirtual RDMA. Działa jako moduł ładowany przez libibverbs,
pozwalający programom na dostęp z przestrzeni użytkownika do
urządzeń VMware Paravirtual RDMA.

%package static
Summary:	Static version of vmw_pvrdma driver
Summary(pl.UTF-8):	Statyczna wersja sterownika vmw_pvrdma
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of vmw_pvrdma driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika vmw_pvrdma, którą można wbudować
bezpośrednio w aplikację.

%prep
%setup -q -n libvmw_pvrdma-%{version}

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rdmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvmw_pvrdma.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libvmw_pvrdma-rdmav2.so
%{_sysconfdir}/libibverbs.d/vmw_pvrdma.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libvmw_pvrdma.a
