# This file is part of the Linux Process Explorer
# See www.sourceforge.net/projects/procexp
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA


Summary: %{_projectname}
Name: %{_projectname}
Version: %{_versionprefix} 
Release: %_svnversion
Vendor: Carl Wolff
License: GPL
Group: System Environment/Libraries
BuildRoot: %{_builddir}
Packager: Carl.Wolff


#Requires: GAIUS_prerequisites >= 2.0

#No automatic dependency stuff
Autoprov: 0
Autoreq: 0

#No automatic bytecompile and packaging stuff
%define __os_install_post %{nil}

%description
This package contains a process explorer.

###############################################################################
%prep
#No preparation needed to create this RPM


###############################################################################
%build
#No build needed to create this RPM

###############################################################################
%install
# Copy all relevant files
if [[ ! -d $RPM_BUILD_ROOT ]]; then
  mkdir $RPM_BUILD_ROOT
fi
if [[ ! -d $RPM_BUILD_ROOT/opt ]]; then
  mkdir $RPM_BUILD_ROOT/opt
fi
if [[ ! -d $RPM_BUILD_ROOT/opt/%{_projectname}-%{version}-%{release} ]]; then
  mkdir $RPM_BUILD_ROOT/opt/%{_projectname}-%{version}-%{release}
fi

#delete old RPM files, if exist
rm -f ../../*.rpm

#unpack prerequisites for the process explorer
pwd
cp -a ../../../procexp $RPM_BUILD_ROOT/opt/%{_projectname}-%{version}-%{release}


###############################################################################
%clean
#No clean after creating this RPM

###############################################################################
%files
/opt/%{_projectname}-%{version}-%{release}

###############################################################################
%pre
# Executed before installation on target, nothing to prepare before installing


###############################################################################
%post
chmod +x /opt/%{_projectname}-%{version}-%{release}/procexp/procexp.py
ln -s /opt/%{_projectname}-%{version}-%{release}/procexp/procexp.py /usr/bin/procexp

###############################################################################
%postun
#No actions needed after the RPM is uninstalled from the target system
rm -rf /opt/%{_projectname}-%{version}-%{release}
rm -f /usr/bin/procexp
