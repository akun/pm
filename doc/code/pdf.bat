if "%1" == "pdf" (
	%SPHINXBUILD% -b pdf %ALLSPHINXOPTS% %BUILDDIR%/pdf
	echo.
echo.Build finished. The PDF files are in %BUILDDIR%/pdf
	goto end
)
