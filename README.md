RPMBUILD for go-swagger
=========================

go-swagger rpm

How to Build
=========
    git clone https://github.com/allanhung/rpm_go-swagger
    cd rpm_go-swagger
    docker run --name=go-swagger_build --rm -ti -v $(pwd)/rpms:/root/rpmbuild/RPMS/x86_64 -v $(pwd)/rpms:/root/rpmbuild/RPMS/noarch -v $(pwd)/scripts:/usr/local/src/build centos /bin/bash -c "/usr/local/src/build/build_go-swagger.sh 0.13.0"

# check
    docker run --name=go-swagger_check --rm -ti -v $(pwd)/rpms:/root/rpmbuild/RPMS centos /bin/bash -c "yum localinstall -y /root/rpmbuild/RPMS/go-swagger-*.rpm"
