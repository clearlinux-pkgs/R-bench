#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bench
Version  : 1.1.2
Release  : 15
URL      : https://cran.r-project.org/src/contrib/bench_1.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bench_1.1.2.tar.gz
Summary  : High Precision Timing of R Expressions
Group    : Development/Tools
License  : MIT
Requires: R-bench-lib = %{version}-%{release}
Requires: R-glue
Requires: R-pillar
Requires: R-profmem
Requires: R-rlang
Requires: R-tibble
BuildRequires : R-glue
BuildRequires : R-mockery
BuildRequires : R-pillar
BuildRequires : R-profmem
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
R expressions.

%package lib
Summary: lib components for the R-bench package.
Group: Libraries

%description lib
lib components for the R-bench package.


%prep
%setup -q -c -n bench
cd %{_builddir}/bench

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640978407

%install
export SOURCE_DATE_EPOCH=1640978407
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bench
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bench
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bench
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bench || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bench/DESCRIPTION
/usr/lib64/R/library/bench/INDEX
/usr/lib64/R/library/bench/LICENSE
/usr/lib64/R/library/bench/Meta/Rd.rds
/usr/lib64/R/library/bench/Meta/features.rds
/usr/lib64/R/library/bench/Meta/hsearch.rds
/usr/lib64/R/library/bench/Meta/links.rds
/usr/lib64/R/library/bench/Meta/nsInfo.rds
/usr/lib64/R/library/bench/Meta/package.rds
/usr/lib64/R/library/bench/NAMESPACE
/usr/lib64/R/library/bench/NEWS.md
/usr/lib64/R/library/bench/R/bench
/usr/lib64/R/library/bench/R/bench.rdb
/usr/lib64/R/library/bench/R/bench.rdx
/usr/lib64/R/library/bench/examples/exprs.R
/usr/lib64/R/library/bench/help/AnIndex
/usr/lib64/R/library/bench/help/aliases.rds
/usr/lib64/R/library/bench/help/bench.rdb
/usr/lib64/R/library/bench/help/bench.rdx
/usr/lib64/R/library/bench/help/figures/README-autoplot-1.png
/usr/lib64/R/library/bench/help/figures/README-custom-plot-1.png
/usr/lib64/R/library/bench/help/figures/README-pressure-1.png
/usr/lib64/R/library/bench/help/paths.rds
/usr/lib64/R/library/bench/html/00Index.html
/usr/lib64/R/library/bench/html/R.css
/usr/lib64/R/library/bench/tests/testthat.R
/usr/lib64/R/library/bench/tests/testthat/test-bench_process_memory.R
/usr/lib64/R/library/bench/tests/testthat/test-bench_time.R
/usr/lib64/R/library/bench/tests/testthat/test-bytes.R
/usr/lib64/R/library/bench/tests/testthat/test-expression.R
/usr/lib64/R/library/bench/tests/testthat/test-hires_time.R
/usr/lib64/R/library/bench/tests/testthat/test-mark.R
/usr/lib64/R/library/bench/tests/testthat/test-press.R
/usr/lib64/R/library/bench/tests/testthat/test-time.R
/usr/lib64/R/library/bench/tests/testthat/test-workout.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bench/libs/bench.so
/usr/lib64/R/library/bench/libs/bench.so.avx2
/usr/lib64/R/library/bench/libs/bench.so.avx512
