find . -name "*.pyc"|xargs rm -f 
SVNVERSION=`svnversion`

echo "procexp (1.6.$SVNVERSION-0ubuntu1) precise; urgency=low

  * Release 1.6 (Closes: #nnnn)  <nnnn is the bug number of your ITP>

 -- Carl Wolff <procexp@wolff-online.nl>  Sat, 14 Dec 2013 22:10:05 +0100" > ./debian/changelog

tar -cvzf  ../procexp_1.6.$SVNVERSION.orig.tar.gz ./procexp
debuild -us -uc --source-option=--include-binaries
