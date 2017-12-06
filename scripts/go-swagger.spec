%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.13.0
%endif

Name:           goswagger
Version:        %{_verstr}
Release:        1%{?dist}
Summary:        Swagger is a simple yet powerful representation of your RESTful API.

Group:          Development/Libraries
License:        MPLv2.0
URL:            https://goswagger.io
#Source0:        https://releases.go-swagger.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Swagger is a simple yet powerful representation of your RESTful API.
With the largest ecosystem of API tooling on the planet, thousands of developers are supporting Swagger
in almost every modern programming language and deployment environment.
With a Swagger-enabled API, you get interactive documentation, client SDK generation and discoverability. 
We created Swagger to help fulfill the promise of APIs.
Swagger helps companies like Apigee, Getty Images, Intuit, LivingSocial, McKesson, Microsoft, Morningstar,
and PayPal build the best possible services with RESTful APIs.
Now in version 2.0, Swagger is more enabling than ever. And it's 100% open source software.


%prep
export GOPATH=/usr/share/gocode
export PATH=$GOPATH/bin:$PATH

%build


%install
cd $GOPATH/src/github.com/go-swagger/go-swagger
mkdir -p %{buildroot}/%{_bindir}
cp ./swagger %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}


%files
%attr(755, root, root) %{_bindir}/swagger


%changelog
* Fri Dec 06 2017 allanhung hungallan@gmail.com
- version 0.13.0
