
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)
%define _prefix /usr/X11R6
%define gimp_plugin_dir %{_prefix}/lib/gimp/1.2/plug-ins

%define module pygimp

Summary:	A python extension allowing you to write Gimp plugins in Python
Summary(pl):	Rozszerzenie Pythona pozwalaj±ce na pisanie wtyczek do Gimpa w Pythonie
Name:		python-%{module}
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.daa.com.au/pub/james/pygimp/%{module}-%{version}.tar.gz
Requires:	gimp
Requires:	python
BuildRequires:	gimp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pygimp allows you to write Gimp plugins with the python language.
Unlike script-fu scripts which only have access to functions in the
PDB (procedural database), pygimp plugins have access to all
functionality that C plugins have, including direct pixel manipulation
that is required for many plugins.

%description -l pl
Modu³ ten umo¿liwia tworzenie wtyczek dla Gimpa za pomoc± jêzyka
Python.

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	pysitedir=%{python_sitepkgsdir}/%{module} \
	pyexecdir=%{python_sitepkgsdir}/%{module}

echo %{module} > $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}.pth

gzip -9nf README NEWS COPYING
install -d html
install doc/*.html html

%files
%defattr(644,root,root,755)

%{python_sitepkgsdir}/%{module}.pth
%dir %{python_sitepkgsdir}/%{module}

%attr(755,root,root) %{python_sitepkgsdir}/%{module}/gimpmodule.so
%{python_sitepkgsdir}/%{module}/gimpenums.py?
%{python_sitepkgsdir}/%{module}/gimpfu.py?
%{python_sitepkgsdir}/%{module}/gimpplugin.py?
%{python_sitepkgsdir}/%{module}/gimpshelf.py?
%{python_sitepkgsdir}/%{module}/gimpui.py?

%attr(755,root,root) %{gimp_plugin_dir}/clothify.py
%attr(755,root,root) %{gimp_plugin_dir}/foggify.py
%attr(755,root,root) %{gimp_plugin_dir}/gimpcons.py
%attr(755,root,root) %{gimp_plugin_dir}/gtkcons.py
%attr(755,root,root) %{gimp_plugin_dir}/pdbbrowse.py
%attr(755,root,root) %{gimp_plugin_dir}/shadow_bevel.py
%attr(755,root,root) %{gimp_plugin_dir}/sphere.py
%attr(755,root,root) %{gimp_plugin_dir}/whirlpinch.py

%doc {README,NEWS,COPYING}.gz html

%clean
rm -rf $RPM_BUILD_ROOT
