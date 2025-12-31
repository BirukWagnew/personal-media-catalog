<xsl:stylesheet version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<body>
<h1>Movies Only</h1>
<ul>
<xsl:for-each select="catalog/media[type='movie']">
<li><xsl:value-of select="title"/></li>
</xsl:for-each>
</ul>
</body>
</html>
</xsl:template>

</xsl:stylesheet>
