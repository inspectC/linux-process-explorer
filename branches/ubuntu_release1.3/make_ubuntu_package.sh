find . -name "*.pyc"|xargs rm -f 
SVNVERSION=`svnversion`

echo "procexp (1.3.$SVNVERSION-0ubuntu1) precise; urgency=low

  * Release 1.3 (Closes: #nnnn)  <nnnn is the bug number of your ITP>

 -- Carl Wolff <procexp@wolff-online.nl>  Thu, 11 Nov 2012 22:10:05 +0100" > ./debian/changelog

tar -cvzf  ../procexp_1.3.$SVNVERSION.orig.tar.gz ./procexp
debuild -us -uc --source-option=--include-binaries
