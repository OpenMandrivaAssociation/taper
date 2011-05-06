Summary:	A menu-driven file backup system
Name:		taper
Version:	7.0
Release:	%mkrel 0.pre1.13
License:	GPL
Group:		Archiving/Backup
BuildRequires:	ncurses-devel
Source0:	http://switch.dl.sourceforge.net/sourceforge/taper/%{name}-%{version}pre1.tar.bz2
URL:		http://taper.sourceforge.net/
Patch0:		taper-7.0pre1-sparc.patch
Patch1:		taper-7.0pre1-remove-conflicting-type.patch
Patch2:		taper-7.0pre-1-umode_t.patch
Patch3:		taper-7.0pre1-LDFLAGS.diff
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Taper is a backup and restoration program with a friendly user
interface.  Files may be backed up to a tape drive or to a hard disk.
The interface for selecting files to be backed up/restored is very
similar to the Midnight Commander interface, and allows easy traversal
of directories.  Taper supports recursive selection of directories.
Taper also supports backing up SCSI, ftape, zftape and removable drives.
By default, taper is set for incremental backups and automatic most
recent restore.

Install the taper package if you need a user friendly file backup and
restoration program.

%prep
%setup -q -n %{name}-%{version}pre-1

%ifarch %{sunsparc}
%patch0 -p1 -b .sparc
%endif
%patch1 -p1 -b .type_conflict
%patch2 -p1 -b .umode_t
%patch3 -p0 -b .LDFLAGS

find . -name CVS -type d | xargs rm -rf

%build
%make CFLAGS="%{optflags} -O3 -fno-strength-reduce -Wall" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_sbindir},%{_bindir},%{_mandir}/man8}
%{makeinstall_std} 	BINDIR=%{buildroot}%{_sbindir} \
	ALTBIN=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}/man8
ln -sf %{_sbindir}/taper %{buildroot}%{_bindir}/taper
ln -sf %{_sbindir}/bg_restore %{buildroot}%{_bindir}/bg_restore
ln -sf %{_sbindir}/bg_backup %{buildroot}%{_bindir}/bg_backup

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man8/taper.8*

