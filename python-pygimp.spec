%define	module	pygimp
Summary:	A Python extension allowing you to write Gimp plugins in Python
Summary(pl.UTF-8):   Rozszerzenie Pythona pozwalające na pisanie wtyczek do Gimpa w Pythonie
Name:		python-%{module}
Version:	1.2
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.daa.com.au/pub/james/pygimp/%{module}-%{version}.tar.gz
# Source0-md5:	b6fbbc05a9defc7a66a42e3cd63b9bcb
BuildRequires:	gimp-devel
Requires:	gimp
Requires:	python
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimp_plugin_dir	%(gimptool --gimpplugindir)/plug-ins

%description
pygimp allows you to write Gimp plugins with the Python language.
Unlike script-fu scripts which only have access to functions in the
PDB (procedural database), pygimp plugins have access to all
functionality that C plugins have, including direct pixel manipulation
that is required for many plugins.

%description -l pl.UTF-8
Moduł pygimp umożliwia tworzenie wtyczek dla Gimpa za pomocą języka
Python. W przeciwieństwie do skryptów script-fu, które mają dostęp
tylko do funkcji w PDB (bazie danych procedur), wtyczki pygimpa mają
dostęp do całej funkcjonalności dostępnej wtyczkom w C, włącznie z
bezpośrednimi operacjami na pikselach, wymaganymi w wielu wtyczkach.

%prep
%setup -q -n %{module}-%{version}

%build
%configure2_13
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	pysitedir=%{python_sitepkgsdir}/%{module} \
	pyexecdir=%{python_sitepkgsdir}/%{module}

echo %{module} > $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}.pth

install -d html
install doc/*.html html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS html
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
