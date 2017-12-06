GOSWAGGERVER=${1:-'0.13.0'}
RPMVER="${GOSWAGGERVER/-/_}"
export RPMBUILDROOT=/root/rpmbuild
export GOPATH=/usr/share/gocode
export PATH=$GOPATH/bin:$PATH

# go repo
rpm --import https://mirror.go-repo.io/centos/RPM-GPG-KEY-GO-REPO
curl -s https://mirror.go-repo.io/centos/go-repo.repo | tee /etc/yum.repos.d/go-repo.repo
# epel
yum install -y epel-release
yum -y install golang git rpm-build make which
mkdir -p $RPMBUILDROOT/SOURCES && mkdir -p $RPMBUILDROOT/SPECS && mkdir -p $RPMBUILDROOT/SRPMS
# fix rpm marcos
sed -i -e "s#.centos##g" /etc/rpm/macros.dist

# go-swagger
mkdir -p $GOPATH/src/github.com/go-swagger
cd $GOPATH/src/github.com/go-swagger
git clone --depth=10 -b $GOSWAGGERVER https://github.com/go-swagger/go-swagger.git

# build
cd $GOPATH/src/github.com/go-swagger/go-swagger
go build ./cmd/swagger

/bin/cp -f /usr/local/src/build/go-swagger.spec $RPMBUILDROOT/SPECS/
rpmbuild -bb $RPMBUILDROOT/SPECS/go-swagger.spec --define "_version $RPMVER"
