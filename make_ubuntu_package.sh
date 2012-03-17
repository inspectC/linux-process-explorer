SVNVERSION=`svnversion`

echo "procexp (1.0.$SVNVERSION-0ubuntu1) precise; urgency=low

  * Initial release (Closes: #nnnn)  <nnnn is the bug number of your ITP>

 -- Carl Wolff <carl@wolff-online.nl>  Thu, 15 Mar 2012 22:10:05 +0100" > ./debian/changelog

tar -cvzf  ../procexp_1.0.$SVNVERSION.orig.tar.gz ./procexp
debuild -us -uc
