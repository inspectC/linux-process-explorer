find . -name "*.pyc"|xargs rm -f 
SVNVERSION=`svnversion`

echo "procexp (1.5.$SVNVERSION-0ubuntu1) precise; urgency=low

  * Release 1.5 (Closes: #nnnn)  <nnnn is the bug number of your ITP>

 -- Carl Wolff <procexp@wolff-online.nl>  Mon, 10 Dec 2012 22:10:05 +0100" > ./debian/changelog

tar -cvzf  ../procexp_1.5.$SVNVERSION.orig.tar.gz ./procexp
debuild -us -uc --source-option=--include-binaries
